# TODO

## Benchmark Candidates

### Analytical or semi-analytical references

- PA-005 - Sucking interface problem with Stefan flow.
- PA-006 - Scriven spherical vapor bubble growth.
- PA-007 - One-dimensional evaporation with unequal liquid/vapor densities.
- PA-008 - One-dimensional solidification with imposed heat flux boundary.
- PA-009 - Neumann two-phase Stefan problem with unequal conductivities.
- PA-010 - Stefan problem with kinetic undercooling.
- PA-011 - Stefan problem with Gibbs-Thomson curvature correction.
- PA-012 - Cylindrical bubble or cavity growth by heat diffusion.
- PA-013 - Evaporating spherical droplet in a quiescent gas.
- PA-014 - Diffusion-limited dissolution of a circular/spherical inclusion.

### Numerical-reference benchmarks

- PN-001 - Film boiling over a hot horizontal wall.
- PN-002 - Vapor bubble growth with hydrodynamic coupling.
- PN-003 - Vapor bubble rise with phase change and buoyancy.
- PN-004 - Melting in a square cavity with natural convection.
- PN-005 - Freezing/melting around a cold or hot cylinder.
- PN-006 - Directional solidification with a prescribed thermal gradient.
- PN-007 - Dendritic solidification with anisotropic surface energy.
- PN-008 - Two bubbles or droplets with phase-change-driven interaction.
- PN-009 - Topology-change case: merging or breakup during phase change.
- PN-010 - Thin-film evaporation with a moving contact line.

### Experimental-reference benchmarks

- PE-001 - Bubble detachment from a heated wall.
- PE-002 - Pool boiling single-bubble growth cycle.
- PE-003 - Melting of gallium in a rectangular cavity.
- PE-004 - Freezing of water around a cooled cylinder.
- PE-005 - Evaporation of a sessile droplet.
- PE-006 - Leidenfrost droplet lifetime or vapor-film thickness.
- PE-007 - Condensation film on a vertical plate.

### Coherence and numerical-method tests

- PC-001 - Global energy-balance closure for a translating interface.
- PC-002 - Latent-heat conservation under grid refinement.
- PC-003 - Stationary interface with equal heat fluxes on both sides.
- PC-004 - Curvature computation on static circle/sphere interfaces.
- PC-005 - Phase volume conservation for a prescribed moving interface.
- PC-006 - Fresh-cell/dead-cell consistency near a moving front.
- PC-007 - Sharp-interface jump condition test on an oblique interface.

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

- Create a Julia documentation environment under `docs/`.
- Add `docs/Project.toml` with `Documenter.jl`.
- Add `docs/make.jl` to build the site.
- Add `docs/src/index.md` as the landing page.
- Add generated pages for:
  - benchmark index,
  - taxonomy,
  - contribution guide,
  - each case in `cases/`.
- Add static asset handling for `figures/*.svg`.
- Add links from case pages to reference CSV files.
- Add a small Julia script to convert benchmark Markdown/frontmatter into
  Documenter pages.
- Add local build instructions:

```bash
julia --project=docs docs/make.jl
```

- Add a GitHub Actions workflow to build docs on pull requests.
- Add a GitHub Actions workflow to deploy the site with GitHub Pages.
- Configure Documenter deployment with `deploydocs`.
- Add `docs/build/` to `.gitignore`.
- Add a badge in `README.md` once the docs workflow exists.
