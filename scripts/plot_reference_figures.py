#!/usr/bin/env python3
"""Generate analytical reference data and figures for benchmark cases."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
CURVE_POINTS = 401


def write_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def save_figure(path: Path, title: str, xlabel: str, ylabel: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, color="0.88", linewidth=0.8)
    plt.tight_layout()
    plt.savefig(path, format="svg")
    plt.close()


def linspace(start: float, stop: float, count: int) -> list[float]:
    if count < 2:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + index * step for index in range(count)]


def generate_pa001() -> None:
    lambda_ = float(
        mp.findroot(
            lambda value: mp.sqrt(mp.pi)
            * value
            * mp.e** (value * value)
            * mp.erf(value)
            - 1,
            0.6,
        )
    )

    rows: list[list[object]] = []
    for time in [0.01, 0.1, 0.4, 1.0]:
        interface_position = 2 * lambda_ * math.sqrt(time)
        for x_over_s in [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]:
            x = x_over_s * interface_position
            temperature = 1 - math.erf(x / (2 * math.sqrt(time))) / math.erf(lambda_)
            rows.append([time, x_over_s, x, interface_position, temperature])

    write_csv(
        ROOT / "data/PA-001/reference.csv",
        ["time", "x_over_s", "x", "interface_position", "temperature"],
        rows,
    )

    times = linspace(0.01, 1.0, CURVE_POINTS)
    positions = [2 * lambda_ * math.sqrt(time) for time in times]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, positions, color="#1f77b4", linewidth=2.2, label="s(t)")
    plt.legend()
    save_figure(
        ROOT / "figures/PA-001-reference.svg",
        "PA-001 one-phase Stefan reference",
        "time",
        "interface position",
    )


def generate_pa002() -> None:
    xi = float(
        mp.findroot(
            lambda value: value
            - (1 / mp.sqrt(mp.pi))
            * mp.e ** (-value * value)
            * (1 / (1 + mp.erf(value)) - 0.25 / mp.erfc(value)),
            0.25,
        )
    )

    rows: list[list[object]] = []
    for time in [0.01, 0.1, 0.4, 1.0]:
        interface_position = 2 * xi * math.sqrt(time)
        span = 2 * math.sqrt(time)
        for eta in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]:
            x = eta * span
            if x <= interface_position:
                phase = "minus"
                temperature = 1 - (
                    (1 + math.erf(x / (2 * math.sqrt(time)))) / (1 + math.erf(xi))
                )
            else:
                phase = "plus"
                temperature = -0.25 + 0.25 * math.erfc(
                    x / (2 * math.sqrt(time))
                ) / math.erfc(xi)
            rows.append([time, eta, x, interface_position, phase, temperature])

    write_csv(
        ROOT / "data/PA-002/reference.csv",
        ["time", "eta_x_over_2sqrt_t", "x", "interface_position", "phase", "temperature"],
        rows,
    )

    times = linspace(0.01, 1.0, CURVE_POINTS)
    positions = [2 * xi * math.sqrt(time) for time in times]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, positions, color="#d62728", linewidth=2.2, label="s(t)")
    plt.legend()
    save_figure(
        ROOT / "figures/PA-002-reference.svg",
        "PA-002 two-phase Stefan reference",
        "time",
        "interface position",
    )


def frank_disk_f(similarity_radius: float) -> mp.mpf:
    return mp.e1(similarity_radius * similarity_radius / 4)


def frank_disk_f_prime(similarity_radius: float) -> mp.mpf:
    return -2 * mp.e ** (-similarity_radius * similarity_radius / 4) / similarity_radius


def frank_sphere_f(similarity_radius: float) -> mp.mpf:
    return mp.erfc(similarity_radius / 2) / similarity_radius


def frank_sphere_f_prime(similarity_radius: float) -> mp.mpf:
    return -mp.e ** (-similarity_radius * similarity_radius / 4) / (
        mp.sqrt(mp.pi) * similarity_radius
    ) - mp.erfc(similarity_radius / 2) / (similarity_radius * similarity_radius)


def generate_frank_case(
    case_id: str,
    title: str,
    f,
    f_prime,
    color: str,
) -> None:
    stefan_coefficient = -0.4
    similarity_radius_0 = 1.2
    temperature_inf = float(
        similarity_radius_0
        * f(similarity_radius_0)
        / (-2 * stefan_coefficient * f_prime(similarity_radius_0))
    )

    rows: list[list[object]] = []
    for time in [0.1, 0.25, 0.5, 1.0]:
        interface_radius = similarity_radius_0 * math.sqrt(time)
        for r_over_r in [0, 0.5, 1.0, 1.05, 1.25, 1.5, 2.0, 2.5, 3.0]:
            radius = r_over_r * interface_radius
            similarity_radius = radius / math.sqrt(time)
            if similarity_radius <= similarity_radius_0:
                phase = "solid"
                temperature = 0.0
            else:
                phase = "liquid"
                temperature = float(
                    temperature_inf
                    * (1 - f(similarity_radius) / f(similarity_radius_0))
                )
            rows.append(
                [
                    time,
                    r_over_r,
                    radius,
                    interface_radius,
                    similarity_radius,
                    phase,
                    temperature,
                ]
            )

    write_csv(
        ROOT / f"data/{case_id}/reference.csv",
        [
            "time",
            "r_over_R",
            "r",
            "interface_radius",
            "similarity_radius",
            "phase",
            "temperature",
        ],
        rows,
    )

    radii = linspace(0.0, 3.6, CURVE_POINTS)
    temperatures = [
        0.0
        if radius <= similarity_radius_0
        else float(temperature_inf * (1 - f(radius) / f(similarity_radius_0)))
        for radius in radii
    ]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(radii, temperatures, color=color, linewidth=2.2, label="T(r, t=1)")
    plt.axvline(
        similarity_radius_0,
        color="0.35",
        linestyle="--",
        linewidth=1.2,
        label="interface",
    )
    plt.legend()
    save_figure(
        ROOT / f"figures/{case_id}-reference.svg",
        f"{case_id} {title} temperature reference",
        "radius",
        "temperature",
    )


def generate_pa003() -> None:
    generate_frank_case("PA-003", "Frank disk", frank_disk_f, frank_disk_f_prime, "#2ca02c")


def generate_pa004() -> None:
    generate_frank_case(
        "PA-004", "Frank sphere", frank_sphere_f, frank_sphere_f_prime, "#9467bd"
    )


GENERATORS = {
    "PA-001": generate_pa001,
    "PA-002": generate_pa002,
    "PA-003": generate_pa003,
    "PA-004": generate_pa004,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate benchmark reference CSV files and SVG figures."
    )
    parser.add_argument(
        "cases",
        nargs="*",
        help="Case IDs to generate. Omit to generate all cases.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases = args.cases or sorted(GENERATORS)
    unknown_cases = sorted(set(cases) - set(GENERATORS))
    if unknown_cases:
        valid_cases = ", ".join(sorted(GENERATORS))
        raise SystemExit(
            f"unknown case ID(s): {', '.join(unknown_cases)}. "
            f"Valid case IDs: {valid_cases}"
        )
    for case_id in cases:
        GENERATORS[case_id]()
        print(f"generated {case_id}")


if __name__ == "__main__":
    main()
