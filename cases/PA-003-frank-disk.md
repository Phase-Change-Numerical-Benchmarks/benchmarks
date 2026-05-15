---
id: PA-005
title: Frank disk
status: draft
benchmark_class: PA

physics:
  - phase-change
  - heat-diffusion
  - radial-symmetry

process:
  - melting
  - solidification

dimension: 2D
geometry: disk
interface_motion: moving

quantities_of_interest:
  - interface_radius
  - temperature_profile
  - phase_area
  - radial_symmetry_error
  - energy_balance
---

# PA-005 — Frank disk

## Purpose

This benchmark verifies a radially symmetric two-dimensional phase-change
problem.

It is useful for testing:

- curved-interface motion in 2D,
- radial similarity solutions,
- area conservation,
- isotropy of the numerical method,
- interface reconstruction on Cartesian grids.

## Physical configuration

A circular phase-change interface moves radially.

```text
2D domain
centered disk of one phase
moving circular interface r = R(t)
surrounding phase outside the disk
```

The benchmark is usually interpreted in radial coordinates, but numerical
methods may solve it in a full two-dimensional Cartesian domain.

## Governing equations

In the thermally active phase:

$$
\rho c_p \partial_t T
=
\frac{1}{r}
\partial_r
\left(
r k \partial_r T
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

The exact configuration must state whether the disk grows or shrinks.

A typical setup is:

- circular initial interface $R(t_0)=R_0$,
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

The Frank disk benchmark is based on a radially symmetric analytical or
similarity solution in two space dimensions.

The interface radius has the form:

$$
R(t) = 2\lambda \sqrt{\alpha t}
$$

or the corresponding shrinking-front form, depending on the selected physical
configuration.

For the disk geometry, the radial temperature profile is expressed using the
two-dimensional radial similarity solution of the heat equation.


## Known difficulties

- inverted material properties,
- initialization from $t_0>0$.
