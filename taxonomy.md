# Benchmark taxonomy

## By physical process

- melting
- solidification
- evaporation
- condensation
- boiling
- sublimation
- dissolution with phase-equilibrium analogy

## By coupling level

### Diffusion-only phase change

The interface motion is driven only by heat or mass diffusion.

Examples:

- planar Stefan problem
- Frank disk
- Frank sphere

### Phase change with Stefan flow

The interface motion induces a velocity field because of density change.

Examples:

- sucking interface problem
- vaporization with density ratio

### Phase change with hydrodynamics

The full flow field is coupled to the phase-change rate.

Examples:

- growing vapor bubble
- film boiling
- boiling bubble detachment

### Phase change with capillarity

Surface tension affects the interface dynamics.

Examples:

- evaporating droplet
- boiling bubble with surface tension
- capillary-controlled melting/freezing

### Phase change with buoyancy

Natural convection modifies heat transfer.

Examples:

- melting in a cavity
- film boiling
- Rayleigh-Benard-like melting

## By reference type

- exact solution
- similarity solution
- reduced ODE solution
- high-resolution numerical solution
- experimental data

## Current benchmark coverage

| ID | Process | Geometry | Reference type | Primary numerical challenge |
|---|---|---|---|---|
| PA-001 | melting/solidification | 1D planar | exact similarity | one-sided gradient and latent-heat balance |
| PA-002 | melting/solidification | 1D planar | exact similarity | two-sided heat-flux jump |
| PA-003 | solidification | 2D disk | exact radial similarity | curvature, isotropy, and area conservation |
| PA-004 | solidification | 3D sphere | exact radial similarity | surface integration, isotropy, and volume conservation |
| PA-005 | boiling/evaporation | 1D planar | exact similarity | Stefan flow and phase-volume expansion |
| PA-006 | boiling/evaporation | 3D sphere | exact spherical similarity | spherical Stefan flow and large density ratio |
| PA-007 | evaporation | 1D planar film | asymptotic solution | diffusion transient and film recession |
| PA-008 | dissolution | 1D planar | exact similarity | species-driven interface displacement |
| PA-009 | dissolution | 3D sphere | exact similarity | early-time spherical diffusion flux |
| PC-001 | solidification | 1D planar | exact kinematic | prescribed moving Dirichlet boundary |
| PC-002 | dissolution | 2D/axisymmetric bubble | exact kinematic | prescribed mass-transfer shrinkage |

## By numerical challenge

- interface tracking
- curvature computation
- jump conditions
- mass conservation
- latent heat conservation
- large density ratio
- topology change
- thin thermal boundary layer
- fresh/dead cells
- moving contact line
