---
id: PE-001
title: Gallium melting in a side-heated cavity
short_title: Gallium melting
status: draft
benchmark_class: PE

physics:
  - phase-change
  - heat-diffusion
  - natural-convection
  - gravity
  - hydrodynamic-coupling

process:
  - melting

dimension: 2D
geometry: rectangular-cavity
interface_motion: moving

reference_type: experimental
has_exact_solution: false
has_reference_data: false

quantities_of_interest:
  - melt_front_position
  - liquid_fraction
  - flow_structure
  - wall_heat_flux

references:
  - GauViskanta1986
  - Brent1988
  - Hannoun2003
---

# PE-001 - Gallium melting in a side-heated cavity

## Purpose

This benchmark tests melting with natural convection in the melt: the
solid-liquid front is advected out of its conduction-dominated shape by a
buoyant recirculation at very low Prandtl number. It is the standard
experimental reference for convection-coupled melting and the first case in
this collection where the reference is a laboratory measurement rather than
an exact or numerical solution.

## Physical Configuration

Solid gallium initially fills a rectangular cavity at (or marginally below)
its melting temperature. At $t = 0$ the left vertical wall is raised to
$T_h$ above the melting point while the right wall is held at $T_c$ slightly
below it; horizontal walls are adiabatic. A melt layer forms at the hot wall
and natural convection progressively tilts the front, melting the top faster
than the bottom.

Gau & Viskanta's cavity is 8.89 cm long and 6.35 cm high (depth 3.81 cm);
the standard two-dimensional model uses the vertical mid-plane.
Following the configuration fixed by Brent, Voller & Reid:

| Quantity | Symbol | Value | Unit |
|---|---:|---:|---|
| cavity length | $W$ | 0.0889 | m |
| cavity height | $H$ | 0.0635 | m |
| hot wall | $T_h$ | 311.0 | K |
| cold wall | $T_c$ | 301.3 | K |
| melting temperature | $T_m$ | 302.78 | K |
| initial temperature | $T_i$ | 301.3 | K |

## Material Parameters

Gallium properties as used in the enthalpy-porosity literature:

| Parameter | Symbol | Value | Unit |
|---|---:|---:|---|
| density | $\rho$ | 6093 | kg/m^3 |
| viscosity | $\mu$ | $1.81\times10^{-3}$ | Pa s |
| conductivity | $k$ | 32 | W/(m K) |
| heat capacity | $c_p$ | 381.5 | J/(kg K) |
| latent heat | $L$ | $80\,160$ | J/kg |
| thermal expansion | $\beta$ | $1.2\times10^{-4}$ | 1/K |
| gravity | $g$ | 9.81 | m/s^2 |

The commonly quoted dimensionless groups for this configuration are
$Pr \approx 0.0216$, $Ste = c_p (T_h - T_m)/L \approx 0.039$, and
$Ra = g\beta(T_h - T_m)H^3 \rho^2 c_p/(\mu k) \approx 6\times10^{5}$
(Boussinesq in the melt only).

## Governing Equations

Incompressible Navier-Stokes with Boussinesq buoyancy in the melt, no slip on
all walls and on the front; energy equation in both phases; melting front at
$T = T_m$ with the Stefan condition

$$
\rho L\,V_\Gamma
=
\big[\![\,k\,\nabla T\cdot\mathbf n\,]\!\big].
$$

Density change on melting and solid motion are neglected.

## Reference Data

The primary reference is the sequence of melt-front shapes measured by
Gau & Viskanta with the pour-out method at approximately
$t = 2,\,6,\,10,\,12.5,\,17$ and $19\ \mathrm{min}$, published as front
traces (their Fig. 7) and reproduced throughout the modelling literature
starting with Brent, Voller & Reid.

Digitized front coordinates are **not yet included** in `data/PE-001/`:
the original data exist only as figures, and a curated digitization (with an
explicit statement of which cross-section is used, see below) is a pending
contribution. Until then, contributors should compare against the published
figures and against the grid-converged fixed-grid simulations of
Hannoun, Alexiades & Mai, which serve as the de facto numerical reference for
the same configuration.

## Recommended Numerical Setup

2D cavity $W \times H$, no-slip walls, isothermal vertical walls, adiabatic
horizontal walls, melt initially absent (or a thin numerical seed layer at
the hot wall). Report the front at the experimental sampling times. Grids
finer than roughly $200\times150$ are needed for front-shape convergence
according to the fixed-grid literature; coarse grids famously agree *better*
with the experiment than converged ones, which is part of what this case
probes (see below).

## Quantities To Report

- melt front position at the experimental times,
- liquid volume fraction history,
- number and evolution of convective rolls in the melt,
- hot-wall Nusselt number history.

## Known Difficulties

- **the experiment itself is contested**: Hannoun et al. showed that
  grid-converged 2D simulations differ from the pour-out fronts, and that
  many early "validations" matched the experiment through under-resolution;
  agreement with converged numerics and with the experiment must be
  discussed separately,
- 3D wall effects: the measured fronts are recorded at a bounding wall, not
  the mid-plane, and 3D simulations show measurable front variation in depth,
- multicellular versus single-cell flow at early times depends on grid,
  scheme, and dimensionality, and changes the front shape,
- low Prandtl number means thick thermal but thin momentum layers,
- results are sensitive to the mushy-zone/porosity constant in fixed-grid
  methods, which sharp-interface methods avoid entirely - one motivation for
  including this case here.

## References

@GauViskanta1986
@Brent1988
@Hannoun2003
