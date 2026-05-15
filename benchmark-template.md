---
id: PA-XXX
title: Benchmark title
short_title: Short title
status: draft

benchmark_class: PA

physics:
  - phase-change
  - heat-diffusion

process:
  - melting

dimension: 1D
geometry: planar

interface_motion: moving
interface_representation:
  - front-tracking
  - level-set
  - VOF
  - phase-field
  - enthalpy
  - cut-cell

quantities_of_interest:
  - interface_position
  - temperature_profile
  - phase_volume
  - energy_error

has_exact_solution: true
has_reference_data: false

maintainers:
  - name: Your Name
    affiliation: Your Lab

references:
  - key: AuthorYear
---

# PA-XXX - Benchmark title

## 1. Purpose

Explain what this benchmark tests.

Example:

This benchmark verifies the ability of a numerical method to reproduce the
motion of a phase-change interface driven by heat diffusion. It is intended as
a first verification case before testing hydrodynamic coupling.

## 2. Physical configuration

Describe the physical domain.

- Domain:
- Initial interface position:
- Phases:
- Coordinate system:
- Gravity:
- Surface tension:
- Density change:

## 3. Governing equations

State the equations solved in each phase.

For heat diffusion:

$$
\rho_i c_{p,i} \partial_t T_i = \nabla \cdot (k_i \nabla T_i).
$$

At the interface:

$$
T_\Gamma = T_m,
$$

and the Stefan condition is

$$
\rho L V_\Gamma =
\left[ \left[ k \nabla T \cdot \mathbf n \right] \right].
$$

Adapt signs and normal convention for the benchmark.

## 4. Initial conditions

Specify:

- temperature field,
- interface position,
- velocity field if any,
- phase distribution.

## 5. Boundary conditions

Specify every boundary.

| Boundary | Condition |
|---|---|
| left | ... |
| right | ... |
| top | ... |
| bottom | ... |

## 6. Material parameters

| Parameter | Symbol | Value | Unit |
|---|---:|---:|---|
| density | $\rho$ | ... | kg/m^3 |
| heat capacity | $c_p$ | ... | J/(kg K) |
| conductivity | $k$ | ... | W/(m K) |
| latent heat | $L$ | ... | J/kg |
| melting/saturation temperature | $T_m$ | ... | K |

## 7. Non-dimensional numbers

List useful numbers:

- Stefan number,
- Jakob number,
- Prandtl number,
- Rayleigh number,
- Bond number,
- Reynolds number,
- Capillary number.

## 8. Reference solution

Give the analytical, semi-analytical, numerical, or experimental reference.

For an interface position:

$$
s(t) = ...
$$

For a temperature profile:

$$
T(x,t) = ...
$$

If reference data are provided, store them under:

```text
data/PA-XXX/reference.csv
```

If a reference figure is provided, store it under:

```text
figures/PA-XXX-reference.svg
```

When possible, generate reference CSV files and figures from a script in
`scripts/` instead of editing plotted SVG output by hand.

## 9. Quantities to report

Mandatory:

- interface position or radius,
- error against the reference solution,
- temperature profile at selected times,
- global energy balance,
- phase volume, area, or mass conservation.

Optional:

- convergence rate,
- CPU time,
- nonlinear iterations,
- linear solver iterations.

## 10. Error metrics

For interface position or radius:

$$
E_s(t) = |s_h(t) - s_{\mathrm{ref}}(t)|.
$$

For temperature:

$$
E_T =
\left(
\frac{\int_\Omega |T_h - T_{\mathrm{ref}}|^2 d\Omega}
{\int_\Omega d\Omega}
\right)^{1/2}.
$$

For conservation:

$$
E_{\mathrm{energy}}
=
\frac{|E(t) - E(0) - Q_{\partial \Omega}(t)|}
{|E(0)| + |Q_{\partial \Omega}(t)|}.
$$

## 11. Known difficulties

List common traps:

* wrong Stefan sign convention,
* inconsistent latent heat balance,
* inconsistent initial conditions,
* inconsistent boundary conditions,

## 12. References

Use BibTeX keys from `references.bib`.
