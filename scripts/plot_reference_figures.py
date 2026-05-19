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


def generate_pa005() -> None:
    rho_l = 958.4
    rho_g = 0.597
    k_l = 0.679
    k_g = 0.025
    cp_l = 4216.0
    cp_g = 2030.0
    h_lg = 2.26e6
    t_sat = 373.15
    t_bulk = 378.15
    alpha_l = k_l / (rho_l * cp_l)
    alpha_g = k_g / (rho_g * cp_g)

    def residual(beta: mp.mpf) -> mp.mpf:
        beta = mp.mpf(beta)
        density_diffusion_ratio = (
            rho_g * mp.sqrt(alpha_g) / (rho_l * mp.sqrt(alpha_l))
        )
        return beta - (
            (t_bulk - t_sat)
            * cp_g
            * k_l
            * mp.sqrt(alpha_g)
            * mp.e
            ** (
                -(beta * beta)
                * rho_g
                * rho_g
                * alpha_g
                / (rho_l * rho_l * alpha_l)
            )
        ) / (
            h_lg
            * k_g
            * mp.sqrt(mp.pi * alpha_l)
            * mp.erfc(beta * density_diffusion_ratio)
        )

    beta = float(mp.findroot(residual, 0.8))

    def interface_position(time: float) -> float:
        return 2 * beta * math.sqrt(alpha_g * time)

    def liquid_velocity(time: float) -> float:
        return (1 - rho_g / rho_l) * beta * math.sqrt(alpha_g / time)

    def temperature(x: float, time: float) -> float:
        density_diffusion_ratio = rho_g * math.sqrt(alpha_g) / (
            rho_l * math.sqrt(alpha_l)
        )
        argument = x / (2 * math.sqrt(alpha_l * time)) + beta * (
            rho_g - rho_l
        ) / rho_l * math.sqrt(alpha_g / alpha_l)
        return t_bulk - (t_bulk - t_sat) / math.erfc(
            beta * density_diffusion_ratio
        ) * math.erfc(argument)

    rows: list[list[object]] = []
    for time in [0.1, 0.25, 0.5, 1.0]:
        delta = interface_position(time)
        velocity = liquid_velocity(time)
        for x_over_delta in [0, 0.5, 1.0, 1.05, 1.25, 1.5, 2.0, 3.0, 4.0]:
            x = x_over_delta * delta
            phase = "vapor" if x <= delta else "liquid"
            temp = t_sat if x <= delta else temperature(x, time)
            rows.append([time, x_over_delta, x, delta, velocity, phase, temp])

    write_csv(
        ROOT / "data/PA-005/reference.csv",
        [
            "time",
            "x_over_delta",
            "x",
            "interface_position",
            "liquid_velocity",
            "phase",
            "temperature",
        ],
        rows,
    )

    times = linspace(0.1, 1.0, CURVE_POINTS)
    positions = [interface_position(time) for time in times]
    velocities = [liquid_velocity(time) for time in times]

    figure, axis_position = plt.subplots(figsize=(7.2, 4.3))
    axis_velocity = axis_position.twinx()

    position_line = axis_position.plot(
        times,
        positions,
        color="#8c564b",
        linewidth=2.2,
        label="delta(t)",
    )[0]
    velocity_line = axis_velocity.plot(
        times,
        velocities,
        color="#17becf",
        linewidth=2.2,
        label="u_l(t)",
    )[0]

    axis_position.set_title("PA-005 sucking-interface reference")
    axis_position.set_xlabel("time")
    axis_position.set_ylabel("vapor-layer thickness")
    axis_velocity.set_ylabel("liquid velocity")
    axis_position.grid(True, color="0.88", linewidth=0.8)
    axis_position.legend(
        [position_line, velocity_line],
        [position_line.get_label(), velocity_line.get_label()],
        loc="best",
    )
    figure.tight_layout()
    figure.savefig(ROOT / "figures/PA-005-reference.svg", format="svg")
    plt.close(figure)


def scriven_integral(
    lower: float,
    beta: float,
    rho_l: float,
    rho_g: float,
) -> mp.mpf:
    if lower >= 1:
        return mp.mpf("0")
    lower = max(0.0, lower)

    def integrand(x: mp.mpf) -> mp.mpf:
        return mp.e ** (
            -(beta * beta)
            * ((1 - x) ** -2 - 2 * (1 - rho_g / rho_l) * x - 1)
        )

    points = [lower]
    for point in [0.5, 0.9, 0.99, 0.999, 1.0]:
        if point > lower:
            points.append(point)
    return mp.quad(integrand, points)


def generate_pa006() -> None:
    rho_l = 958.0
    rho_g = 0.59
    k_l = 0.6
    cp_l = 4216.0
    cp_g = 2034.0
    h_lg = 2.257e6
    t_sat = 373.0
    jakob = 3.0
    t_bulk = t_sat + h_lg * rho_g * jakob / (rho_l * cp_l)
    alpha_l = k_l / (rho_l * cp_l)

    lhs = rho_l * cp_l * (t_bulk - t_sat) / (
        rho_g * (h_lg + (cp_l - cp_g) * (t_bulk - t_sat))
    )

    def residual(beta: mp.mpf) -> mp.mpf:
        return 2 * beta * beta * scriven_integral(0.0, float(beta), rho_l, rho_g) - lhs

    beta = float(mp.findroot(residual, (3.0, 4.0)))

    def radius(time: float) -> float:
        return 2 * beta * math.sqrt(alpha_l * time)

    energy_scale = rho_g * (h_lg + (cp_l - cp_g) * (t_bulk - t_sat)) / (
        rho_l * cp_l
    )

    def temperature(r: float, time: float) -> float:
        interface_radius = radius(time)
        if r <= interface_radius:
            return t_sat
        lower = 1 - interface_radius / r
        return float(
            t_bulk
            - 2
            * beta
            * beta
            * energy_scale
            * scriven_integral(lower, beta, rho_l, rho_g)
        )

    rows: list[list[object]] = []
    for time in [0.152088195917732, 0.25, 0.5, 1.0]:
        interface_radius = radius(time)
        for r_over_r in [0, 0.5, 1.0, 1.05, 1.25, 1.5, 2.0, 3.0, 4.0]:
            r = r_over_r * interface_radius
            phase = "vapor" if r <= interface_radius else "liquid"
            rows.append(
                [
                    time,
                    r_over_r,
                    r,
                    interface_radius,
                    phase,
                    temperature(r, time),
                ]
            )

    write_csv(
        ROOT / "data/PA-006/reference.csv",
        ["time", "r_over_R", "r", "bubble_radius", "phase", "temperature"],
        rows,
    )

    times = linspace(0.152088195917732, 1.0, CURVE_POINTS)
    radii = [radius(time) for time in times]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, radii, color="#e377c2", linewidth=2.2, label="R(t)")
    plt.legend()
    save_figure(
        ROOT / "figures/PA-006-reference.svg",
        "PA-006 Scriven spherical bubble reference",
        "time",
        "bubble radius",
    )


def generate_pc001() -> None:
    speed = 1.0

    def interface_position(time: float) -> float:
        return speed * time

    def temperature(x: float, time: float) -> float:
        if x <= interface_position(time):
            return 0.0
        return -1.0 + math.exp(-speed * (x - interface_position(time)))

    rows: list[list[object]] = []
    for time in [0.0, 0.05, 0.1, 0.2]:
        position = interface_position(time)
        for x in linspace(0.0, 0.5, 11):
            phase = "solid" if x <= position else "active"
            rows.append([time, x, position, phase, temperature(x, time)])

    write_csv(
        ROOT / "data/PC-001/reference.csv",
        ["time", "x", "interface_position", "phase", "temperature"],
        rows,
    )

    xs = linspace(0.0, 0.5, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    for time, color in [(0.0, "#1f77b4"), (0.1, "#ff7f0e"), (0.2, "#2ca02c")]:
        plt.plot(
            xs,
            [temperature(x, time) for x in xs],
            color=color,
            linewidth=2.0,
            label=f"T(x,{time:g})",
        )
    plt.legend()
    save_figure(
        ROOT / "figures/PC-001-reference.svg",
        "PC-001 constant-speed solidification reference",
        "x",
        "temperature",
    )


def generate_pa007() -> None:
    h0 = 1.0
    domain_height = 10.0
    diffusivity = 1.0
    mu = 0.001 * 0.8
    t_shift = 0.05
    quasi_static_speed = -mu * diffusivity / (domain_height - h0)

    def h_quasi_static(time: float) -> float:
        return h0 + quasi_static_speed * time

    def h_transient(time: float) -> float:
        return h0 + 2 * mu * (
            math.sqrt(t_shift / math.pi) - math.sqrt((time + t_shift) / math.pi)
        )

    def v_transient(time: float) -> float:
        return -mu * math.sqrt(diffusivity / (math.pi * (time + t_shift)))

    rows: list[list[object]] = []
    for time in [0.0, 1.0, 10.0, 25.0, 50.0, 100.0]:
        rows.append(
            [
                time,
                h_quasi_static(time),
                quasi_static_speed,
                h_transient(time),
                v_transient(time),
            ]
        )

    write_csv(
        ROOT / "data/PA-007/reference.csv",
        [
            "time",
            "quasi_static_thickness",
            "quasi_static_velocity",
            "transient_thickness",
            "transient_velocity",
        ],
        rows,
    )

    times = linspace(0.0, 100.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [h_quasi_static(t) for t in times], label="quasi-static")
    plt.plot(times, [h_transient(t) for t in times], label="early transient")
    plt.legend()
    save_figure(
        ROOT / "figures/PA-007-reference.svg",
        "PA-007 static evaporating film reference",
        "time",
        "film thickness",
    )


def generate_pc002() -> None:
    initial_radius = 1.0
    density_dispersed = 0.001
    mass_transfer_rate = -1.0e-3

    def radius(time: float) -> float:
        return initial_radius + mass_transfer_rate / density_dispersed * time

    rows: list[list[object]] = []
    for time in [0.0, 0.25, 0.5, 0.75, 0.9]:
        r = radius(time)
        rows.append([time, r, math.pi * r * r, 4 * math.pi * r**3 / 3])

    write_csv(
        ROOT / "data/PC-002/reference.csv",
        ["time", "radius", "area_2d", "volume_3d"],
        rows,
    )

    times = linspace(0.0, 0.95, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [radius(t) for t in times], label="R(t)", color="#7f7f7f")
    plt.legend()
    save_figure(
        ROOT / "figures/PC-002-reference.svg",
        "PC-002 constant-rate bubble reference",
        "time",
        "radius",
    )


def generate_pa008() -> None:
    diffusivity = 0.1
    henry = 1.2
    c_sigma = 1.0

    def displacement(time: float) -> float:
        return 2 / henry * math.sqrt(time * diffusivity / math.pi)

    def concentration(distance_from_interface: float, time: float) -> float:
        if time <= 0:
            return 0.0
        return c_sigma * math.erfc(distance_from_interface / (2 * math.sqrt(diffusivity * time)))

    rows: list[list[object]] = []
    for time in [1.0, 10.0, 50.0, 175.0]:
        ell = displacement(time)
        for eta in [0, 0.25, 0.5, 1.0, 2.0, 4.0]:
            distance = eta * 2 * math.sqrt(diffusivity * time)
            rows.append([time, ell, eta, distance, concentration(distance, time)])

    write_csv(
        ROOT / "data/PA-008/reference.csv",
        ["time", "interface_displacement", "eta", "distance_from_interface", "concentration"],
        rows,
    )

    times = linspace(0.0, 175.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [displacement(t) for t in times], label="ell(t)", color="#17becf")
    plt.legend()
    save_figure(
        ROOT / "figures/PA-008-reference.svg",
        "PA-008 species-diffusion Stefan reference",
        "time",
        "interface displacement",
    )


def generate_pa009() -> None:
    radius = 0.5
    diffusivity = 1.0 / 0.0526
    c_sigma = 0.2
    c_bulk = 0.0

    def concentration(r: float, time: float) -> float:
        if r <= radius:
            return c_sigma
        return c_bulk + (c_sigma - c_bulk) * radius / r * math.erfc(
            (r - radius) / (2 * math.sqrt(diffusivity * time))
        )

    rows: list[list[object]] = []
    for time in [1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2]:
        for r_over_r in [1.0, 1.1, 1.2, 1.5, 2.0, 3.0]:
            r = r_over_r * radius
            rows.append([time, r_over_r, r, concentration(r, time)])

    write_csv(
        ROOT / "data/PA-009/reference.csv",
        ["time", "r_over_R", "r", "concentration"],
        rows,
    )

    radii = linspace(radius, 2.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    for time, color in [(1.0e-4, "#1f77b4"), (1.0e-3, "#ff7f0e"), (1.0e-2, "#2ca02c")]:
        plt.plot(
            radii,
            [concentration(r, time) for r in radii],
            label=f"t={time:g}",
            color=color,
        )
    plt.legend()
    save_figure(
        ROOT / "figures/PA-009-reference.svg",
        "PA-009 Epstein-Plesset concentration reference",
        "radius",
        "concentration",
    )


GENERATORS = {
    "PA-001": generate_pa001,
    "PA-002": generate_pa002,
    "PA-003": generate_pa003,
    "PA-004": generate_pa004,
    "PA-005": generate_pa005,
    "PA-006": generate_pa006,
    "PA-007": generate_pa007,
    "PA-008": generate_pa008,
    "PA-009": generate_pa009,
    "PC-001": generate_pc001,
    "PC-002": generate_pc002,
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
