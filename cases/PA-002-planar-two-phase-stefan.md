---
id: PA-002
title: Planar two-phase Stefan problem
status: draft
benchmark_class: PA

physics:
  - phase-change
  - heat-diffusion
  - two-phase

process:
  - melting
  - solidification

dimension: 1D
geometry: planar
interface_motion: moving

quantities_of_interest:
  - interface_position
  - temperature_profile
  - heat_flux_jump
  - energy_balance
  - convergence_rate
---

# PA-002 — Planar two-phase Stefan problem

## Purpose

This benchmark verifies a two-sided Stefan problem where both phases solve heat diffusion.

It is intended to test:

- heat diffusion in both phases,
- the two-sided Stefan condition,
- conductivity and diffusivity contrasts,
- accurate interfacial gradients on both sides,
- conservation of latent and sensible heat.

## Physical configuration

A planar interface separates two phases in a one-dimensional domain.

```text
phase -                         phase +
x < s(t)                        x > s(t)

T_-∞ > T_m                      T_+∞ < T_m
hot side                        cold side
```

The interface position is $s(t)$. Both phases are thermally active.

The normal direction is chosen from phase $-$ to phase $+$:

$$
\mathbf n = \mathbf e_x.
$$

For the analytical similarity solution, the infinite-domain convention is used.  
For a finite-domain numerical test, the computational domain should be large enough so that the outer boundaries do not affect the solution during the simulated time.

## Governing equations

In each phase $\Omega_i(t)$, with $i \in \{-,+\}$:

$$
\rho_i c_{p,i} \partial_t T_i
=
\partial_x \left(k_i \partial_x T_i\right).
$$

The thermal diffusivity in each phase is:

$$
\alpha_i = \frac{k_i}{\rho_i c_{p,i}}.
$$

At the interface:

$$
T_-(s(t),t) = T_+(s(t),t) = T_m.
$$

The Stefan condition is:

$$
\rho L V_\Gamma
=
\left[\left[ k \nabla T \cdot \mathbf n \right]\right],
$$

with

$$
V_\Gamma = \frac{ds}{dt}.
$$

With the present one-dimensional convention,

$$
\left[\left[ k \nabla T \cdot \mathbf n \right]\right]
=
k_+ \partial_x T_+(s(t)^+,t)
-
k_- \partial_x T_-(s(t)^-,t).
$$

Therefore,

$$
\rho L \frac{ds}{dt}
=
k_+ \partial_x T_+(s(t)^+,t)
-
k_- \partial_x T_-(s(t)^-,t).
$$

## Boundary and initial conditions

The analytical solution is written for a semi-infinite configuration:

$$
T_-(x,t) \to T_{-\infty}
\qquad \text{as } x \to -\infty,
$$

and

$$
T_+(x,t) \to T_{+\infty}
\qquad \text{as } x \to +\infty.
$$

The far-field temperatures satisfy:

$$
T_{-\infty} > T_m,
\qquad
T_{+\infty} < T_m.
$$

At the interface:

$$
T_\Gamma = T_m.
$$

For a finite-domain numerical test, initialize the solution at a small time $t_0>0$ using the analytical solution. This avoids the singular initial condition at $t=0$.

The initial interface position is then:

$$
s(t_0) = 2 \xi \sqrt{t_0}.
$$

## Material parameters

A simple dimensionless test case is recommended first.

| Parameter | Phase $-$ | Phase $+$ |
|---|---:|---:|
| $\rho$ | 1 | 1 |
| $c_p$ | 1 | 1 |
| $k$ | 1 | 1 |
| $\alpha = k/(\rho c_p)$ | 1 | 1 |

Suggested temperatures:

| Quantity | Value |
|---|---:|
| $T_{-\infty}$ | 1 |
| $T_m$ | 0 |
| $T_{+\infty}$ | -0.25 |

The latent heat $L$ controls the interface velocity. A first recommended choice is:

$$
L = 1.
$$

This asymmetric choice avoids the degenerate case where the heat supplied from the hot side and the heat removed by the cold side exactly balance.

## Reference solution

The two-phase planar Stefan problem admits a similarity solution.

The interface position is:

$$
s(t) = 2 \xi \sqrt{t},
$$

where $\xi$ is a constant determined by the Stefan condition.

Define:

$$
\lambda_- = \frac{\xi}{\sqrt{\alpha_-}},
\qquad
\lambda_+ = \frac{\xi}{\sqrt{\alpha_+}}.
$$

The temperature in phase $-$, for $x < s(t)$, is:

$$
T_-(x,t)
=
T_{-\infty}
+
(T_m-T_{-\infty})
\frac{
1+\operatorname{erf}
\left(
\dfrac{x}{2\sqrt{\alpha_- t}}
\right)
}{
1+\operatorname{erf}(\lambda_-)
}.
$$

The temperature in phase $+$, for $x > s(t)$, is:

$$
T_+(x,t)
=
T_{+\infty}
+
(T_m-T_{+\infty})
\frac{
\operatorname{erfc}
\left(
\dfrac{x}{2\sqrt{\alpha_+ t}}
\right)
}{
\operatorname{erfc}(\lambda_+)
}.
$$

These expressions satisfy:

$$
T_-(s(t),t) = T_+(s(t),t) = T_m,
$$

$$
T_-(x,t) \to T_{-\infty}
\qquad \text{as } x \to -\infty,
$$

and

$$
T_+(x,t) \to T_{+\infty}
\qquad \text{as } x \to +\infty.
$$

## Determination of the similarity parameter

The interface velocity is:

$$
\frac{ds}{dt} = \frac{\xi}{\sqrt{t}}.
$$

The one-sided gradient in phase $-$ at the interface is:

$$
\partial_x T_-(s(t)^-,t)
=
\frac{
T_m-T_{-\infty}
}{
\sqrt{\pi \alpha_- t}
\left[
1+\operatorname{erf}(\lambda_-)
\right]
}
\exp(-\lambda_-^2).
$$

The one-sided gradient in phase $+$ at the interface is:

$$
\partial_x T_+(s(t)^+,t)
=
-
\frac{
T_m-T_{+\infty}
}{
\sqrt{\pi \alpha_+ t}
\operatorname{erfc}(\lambda_+)
}
\exp(-\lambda_+^2).
$$

Injecting these expressions into the Stefan condition gives the scalar equation for $\xi$:

$$
\rho L \xi
=
\frac{
k_- (T_{-\infty}-T_m)
}{
\sqrt{\pi \alpha_-}
\left[
1+\operatorname{erf}(\lambda_-)
\right]
}
\exp(-\lambda_-^2)
-
\frac{
k_+ (T_m-T_{+\infty})
}{
\sqrt{\pi \alpha_+}
\operatorname{erfc}(\lambda_+)
}
\exp(-\lambda_+^2).
$$

with

$$
\lambda_- = \frac{\xi}{\sqrt{\alpha_-}},
\qquad
\lambda_+ = \frac{\xi}{\sqrt{\alpha_+}}.
$$

This nonlinear scalar equation should be solved once before running the benchmark.

## Dimensionless example

For the simple case

$$
\rho = 1,
\qquad
c_{p,-}=c_{p,+}=1,
\qquad
k_- = k_+ = 1,
\qquad
\alpha_-=\alpha_+=1,
$$

the interface position is:

$$
s(t) = 2\xi\sqrt{t}.
$$

The temperature in phase $-$ becomes:

$$
T_-(x,t)
=
T_{-\infty}
+
(T_m-T_{-\infty})
\frac{
1+\operatorname{erf}
\left(
\dfrac{x}{2\sqrt{t}}
\right)
}{
1+\operatorname{erf}(\xi)
}.
$$

The temperature in phase $+$ becomes:

$$
T_+(x,t)
=
T_{+\infty}
+
(T_m-T_{+\infty})
\frac{
\operatorname{erfc}
\left(
\dfrac{x}{2\sqrt{t}}
\right)
}{
\operatorname{erfc}(\xi)
}.
$$

The scalar equation for $\xi$ is:

$$
L \xi
=
\frac{1}{\sqrt{\pi}}
\left[
\frac{
(T_{-\infty}-T_m)\exp(-\xi^2)
}{
1+\operatorname{erf}(\xi)
}
-
\frac{
(T_m-T_{+\infty})\exp(-\xi^2)
}{
\operatorname{erfc}(\xi)
}
\right].
$$

For the suggested values

$$
T_{-\infty}=1,
\qquad
T_m=0,
\qquad
T_{+\infty}=-0.25,
\qquad
L=1,
$$

this equation has a positive solution corresponding to melting toward positive $x$.


## Known difficulties

- sign convention in the two-sided Stefan condition,
- inverted material properties,
- initialization from a nonzero time,