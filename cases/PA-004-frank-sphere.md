---
id: PA-006
title: Frank sphere
status: draft
benchmark_class: PA

physics:
  - phase-change
  - heat-diffusion
  - radial-symmetry

process:
  - melting
  - solidification

dimension: 3D
geometry: sphere
interface_motion: moving

quantities_of_interest:
  - interface_radius
  - temperature_profile
  - phase_volume
  - radial_symmetry_error
  - energy_balance
---

# PA-006 — Frank sphere

## Purpose

This benchmark verifies a radially symmetric three-dimensional phase-change
problem.

It is the 3D counterpart of the Frank disk test and is useful for testing:

- spherical interface motion,
- volume conservation,
- surface heat-flux integration,
- 3D interface reconstruction,
- radial symmetry on Cartesian grids.

## Physical configuration

A spherical phase-change interface moves radially.

```text
3D domain
centered sphere of one phase
moving spherical interface r = R(t)
surrounding phase outside the sphere
```

The reference solution is radial, but numerical methods may solve the full
three-dimensional problem.

## Governing equations

In the thermally active phase:

$$
\rho c_p \partial_t T
=
\frac{1}{r^2}
\partial_r
\left(
r^2 k \partial_r T
\right).
$$

At the interface:

$$
T(R(t),t) = T_m.
$$

The Stefan condition is:

$$
\rho L \frac{dR}{dt}
=
\left[\left[ k \nabla T \cdot \mathbf n \right]\right].
$$

For a one-phase variant, only one side contributes to the heat flux.

## Boundary and initial conditions

The exact configuration must state whether the sphere grows or shrinks.

A typical setup is:

- spherical initial interface $R(t_0)=R_0$,
- temperature initialized from the radial similarity solution,
- outer boundary sufficiently far away,
- fixed far-field or symmetry-compatible condition.

## Material parameters

Use a dimensionless setup first:

| Parameter | Symbol | Value |
|---|---:|---:|
| density | $\rho$ | 1 |
| heat capacity | $c_p$ | 1 |
| conductivity | $k$ | 1 |
| diffusivity | $\alpha$ | 1 |
| latent heat | $L$ | chosen |
| phase-change temperature | $T_m$ | 0 |

## Reference solution

The Frank sphere benchmark is based on a radially symmetric analytical or
similarity solution in three space dimensions.

The interface radius has the form:

$$
R(t) = 2\lambda \sqrt{\alpha t}
$$

or the corresponding shrinking-front form, depending on the selected physical
configuration.

## Known difficulties

- inverted material properties,
- initialization from $t_0>0$.
