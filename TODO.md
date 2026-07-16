# TODO

## Benchmark Candidates

### Analytical or semi-analytical references

Implemented so far: PA-010 (Epstein-Plesset dissolving bubble), PA-011
(Rubinstein binary-alloy solidification), PA-012 (d2-law evaporating
droplet), PA-013 (Nusselt laminar film condensation).

Remaining candidates (IDs assigned at implementation time):

- Stefan problem with kinetic undercooling.
- Stefan problem with Gibbs-Thomson curvature correction.
- Cylindrical vapor bubble growth with Stefan flow.
- Neumann two-phase Stefan problem with unequal conductivities.
- Ivantsov paraboloidal dendrite tip (Peclet-undercooling relation).
- Mullins-Sekerka dispersion relation for a perturbed planar front.
- Landau ablation problem with imposed surface heat flux.
- High-transfer-number d2-law variant (Y_s = 0.5).

### Numerical-reference benchmarks

Implemented so far: PN-001 (film boiling on a horizontal wall).

- Fixed or deforming vapor bubble growth with full hydrodynamic coupling.
- Vapor bubble rise with phase change and buoyancy.
- Melting in a square cavity with natural convection.
- Freezing/melting around a cold or hot cylinder.
- Dendritic solidification with anisotropic surface energy.
- Two bubbles or droplets with phase-change-driven interaction.
- Two-front collision or bubble coalescence topology-change benchmark.
- Thin-film evaporation with a moving contact line.

### Experimental-reference benchmarks

Implemented so far: PE-001 (gallium melting, Gau & Viskanta; melt-front
digitization still pending).

- Bubble detachment from a heated wall.
- Pool boiling single-bubble growth cycle.
- Freezing of water around a cooled cylinder.
- Evaporation of a sessile droplet.
- Leidenfrost droplet lifetime or vapor-film thickness.
- Condensation film on a vertical plate.

### Coherence and numerical-method tests

- PC-003 - Global energy-balance closure for a translating interface.
- PC-004 - Latent-heat conservation under grid refinement.
- PC-005 - Stationary interface with equal heat fluxes on both sides.
- PC-006 - Curvature computation on static circle/sphere interfaces.
- PC-007 - Phase volume conservation for a prescribed moving interface.
- PC-008 - Fresh-cell/dead-cell consistency near a moving front.
- PC-009 - Sharp-interface jump condition test on an oblique interface.

### Pending data work

- Digitize the Gau & Viskanta melt-front traces for PE-001 (state the
  cross-section used; cross-check against Hannoun et al. converged numerics).

## Repository Tasks

- Add a BibTeX lint/check step.
- Add a Markdown link checker.
- Add issue templates for new benchmark proposals and result submissions.
- Add contribution guidance for submitting solver results.
- Decide whether benchmark IDs should leave gaps for historical compatibility.

## Julia Documenter Site

../phase-change-benchmarks.github.io is the home for the documentation site.
