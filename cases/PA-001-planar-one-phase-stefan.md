---
id: PA-001
title: Planar one-phase Stefan problem
status: draft
benchmark_class: PA

physics:
  - phase-change
  - heat-diffusion

process:
  - melting
  - solidification

dimension: 1D
geometry: planar
interface_motion: moving

quantities_of_interest:
  - interface_position
  - temperature_profile
  - energy_balance
  - convergence_rate
---

# PA-001 — Planar one-phase Stefan problem

## Purpose

This benchmark verifies the motion of a planar phase-change front driven by
one-sided heat diffusion.

It is the minimal verification case for:

- the Stefan condition,
- the interface temperature condition,
- the interfacial heat flux,
- interface-position convergence,
- global energy balance.

## Physical configuration

A semi-infinite material initially at the phase-change temperature is heated
from one side. A liquid layer grows from the heated wall and is separated from
the solid by a moving planar interface.

The problem is one-dimensional:

```text
x = 0                        x = s(t)
| heated wall | liquid phase | interface | solid at T_m |
```

The active phase is the liquid phase. The solid phase is assumed to remain at
the phase-change temperature.

## Governing equations

In the liquid phase $0 < x < s(t)$:

$$
\rho c_p \partial_t T = \partial_x \left(k \partial_x T\right).
$$

At the moving interface:

$$
T(s(t),t) = T_m.
$$

The Stefan condition is:

$$
\rho L \frac{ds}{dt}
=
- k \partial_x T(s(t)^-,t).
$$

The sign convention assumes that the liquid occupies $0 < x < s(t)$ and that
the interface moves toward positive $x$ during melting.

## Boundary and initial conditions

At the heated wall:

$$
T(0,t) = T_h, \qquad T_h > T_m.
$$

At the interface:

$$
T(s(t),t) = T_m.
$$

Initial condition:

$$
s(0) = 0.
$$

For numerical computations, one may start at a small time $t_0 > 0$ to avoid
the initial singularity.

## Material parameters

Use a dimensionless setup by default:

| Parameter | Symbol | Value |
|---|---:|---:|
| density | $\rho$ | 1 |
| heat capacity | $c_p$ | 1 |
| thermal conductivity | $k$ | 1 |
| thermal diffusivity | $\alpha=k/(\rho c_p)$ | 1 |
| latent heat | $L$ | chosen from Stefan number |
| melting temperature | $T_m$ | 0 |
| hot-wall temperature | $T_h$ | 1 |

The Stefan number is:

$$
\mathrm{Ste} = \frac{c_p (T_h-T_m)}{L}.
$$

A recommended first value is:

$$
\mathrm{Ste}=1.
$$

## Reference solution

The similarity solution is:

$$
s(t) = 2\lambda \sqrt{\alpha t},
$$

with

$$
T(x,t)
=
T_h
-
(T_h-T_m)
\frac{
\operatorname{erf}\left(x/(2\sqrt{\alpha t})\right)
}{
\operatorname{erf}(\lambda)
}.
$$

The parameter $\lambda$ is determined by:

$$
\mathrm{Ste}
=
\sqrt{\pi}\lambda
\exp(\lambda^2)
\operatorname{erf}(\lambda).
$$




## Known issues

- initial singularity at $t=0$,
- wrong sign in the Stefan condition
