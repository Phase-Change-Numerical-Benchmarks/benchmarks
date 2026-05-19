# TODO

## Benchmark Candidates

### Analytical or semi-analytical references

- PA-010 - Shrinking evaporating droplet with gas-phase diffusion reference.
- PA-011 - Epstein-Plesset moving-radius dissolution benchmark.
- PA-012 - Stefan problem with kinetic undercooling.
- PA-013 - Stefan problem with Gibbs-Thomson curvature correction.
- PA-014 - Cylindrical vapor bubble growth with Stefan flow.

### Numerical-reference benchmarks

- PN-001 - Film boiling over a hot horizontal wall.
- PN-002 - Fixed or deforming vapor bubble growth with full hydrodynamic coupling.
- PN-003 - Vapor bubble rise with phase change and buoyancy.
- PN-004 - Melting in a square cavity with natural convection.
- PN-005 - Freezing/melting around a cold or hot cylinder.
- PN-006 - Dendritic solidification with anisotropic surface energy.
- PN-007 - Two bubbles or droplets with phase-change-driven interaction.
- PN-008 - Two-front collision or bubble coalescence topology-change benchmark.
- PN-009 - Thin-film evaporation with a moving contact line.

### Experimental-reference benchmarks

- PE-001 - Bubble detachment from a heated wall.
- PE-002 - Pool boiling single-bubble growth cycle.
- PE-003 - Melting of gallium in a rectangular cavity.
- PE-004 - Freezing of water around a cooled cylinder.
- PE-005 - Evaporation of a sessile droplet.
- PE-006 - Leidenfrost droplet lifetime or vapor-film thickness.
- PE-007 - Condensation film on a vertical plate.

### Coherence and numerical-method tests

- PC-003 - Global energy-balance closure for a translating interface.
- PC-004 - Latent-heat conservation under grid refinement.
- PC-005 - Stationary interface with equal heat fluxes on both sides.
- PC-006 - Curvature computation on static circle/sphere interfaces.
- PC-007 - Phase volume conservation for a prescribed moving interface.
- PC-008 - Fresh-cell/dead-cell consistency near a moving front.
- PC-009 - Sharp-interface jump condition test on an oblique interface.

## Repository Tasks

- Add `data/README.md` describing reference CSV column conventions.
- Add `figures/README.md` describing how plots are generated.
- Add a validation script that checks every case frontmatter path exists.
- Add a BibTeX lint/check step.
- Add a Markdown link checker.
- Add issue templates for new benchmark proposals and result submissions.
- Add contribution guidance for submitting solver results.
- Decide whether benchmark IDs should leave gaps for historical compatibility.

## Julia Documenter Site

../phase-change-benchmarks.github.io is the home for the documentation site.
