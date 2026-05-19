# Phase-Change Numerical Benchmarks

This repository contains benchmark definitions for phase-change numerical
methods.

The repository is organized around stable benchmark identifiers:

```text
PA-001  Planar one-phase Stefan problem
PA-002  Planar two-phase Stefan problem
PA-003  Frank disk
PA-004  Frank sphere
PA-005  Sucking interface problem
PA-006  Scriven spherical vapor bubble growth
PA-007  Static evaporating film
PA-008  Species-diffusion Stefan problem
PA-009  Epstein-Plesset steady-radius dissolution
PC-001  Constant-speed planar solidification
PC-002  Constant-rate dissolving bubble
```

Each benchmark is described by a Markdown file in `cases/`.

## Goals

The goal is not to promote one numerical method, but to define reproducible
test cases for comparing methods such as:

* sharp-interface methods,
* front tracking,
* level set,
* VOF,
* cut-cell finite volumes,
* ghost-fluid methods,
* immersed-boundary methods,
* enthalpy methods,
* phase-field methods.

## Benchmark Identifiers

Benchmark identifiers follow the convention used in the historical
InterfaceTracking benchmark collection.

| Prefix | Meaning |
|---|---|
| `N` | Purely numerical test-case |
| `P` | Physical test-case |
| `PA` | Physical test-case compared to an analytical solution |
| `PN` | Physical test-case compared to a numerical reference method |
| `PE` | Physical test-case compared to an experiment |
| `PC` | Test of coherence |

For example:

```text
PA-001  Planar one-phase Stefan problem
PN-001  Film boiling benchmark with numerical reference data
PE-001  Bubble detachment benchmark compared to experiment
PC-003  Energy-balance coherence test
```

## Repository Structure

```text
cases/       Benchmark descriptions
data/        Reference data
figures/     Problem sketches and reference plots
scripts/     Reference data and plotting utilities
references.bib  Bibliography
```

See `index.md` and `benchmark-template.md`.
