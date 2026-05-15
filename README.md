# Phase-Change Numerical Benchmarks

This repository contains benchmark definitions for phase-change numerical methods.

The repository is organized around stable benchmark identifiers:

```text
PA-001  Planar one-phase Stefan problem
PA-002  Planar two-phase Stefan problem
PA-003  Sucking interface problem
PA-004  Scriven spherical vapor bubble growth
PA-005  Frank disk
PA-006  Frank sphere
...
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

## Benchmark identifiers

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
PC-001  Energy-balance coherence test

## Repository structure

```text
cases/       Benchmark descriptions
data/        Reference data
figures/     Problem sketches and reference plots
scripts/     Utilities for plotting/checking data
schemas/     Metadata schema
```

## Minimal result submission

A submitted result should contain:

* solver name,
* numerical method,
* grid/time step,
* material parameters,
* interface representation,
* error metrics,
* CSV data for quantities of interest,
* plots if useful.

See `benchmark-template.md`.
