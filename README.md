# Phase-Change Numerical Benchmarks

This repository contains benchmark definitions for phase-change numerical methods.

The repository is organized around stable benchmark identifiers:

```text
PC-001  Planar one-phase Stefan problem
PC-002  Planar two-phase Stefan problem
PC-003  Sucking interface problem
PC-004  Scriven spherical vapor bubble growth
PC-005  Frank disk
PC-006  Frank sphere
...
````

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

## Benchmark classes

Benchmarks are classified into four levels.

| Level | Type                         | Purpose                                                   |
| ----- | ---------------------------- | --------------------------------------------------------- |
| L1    | Analytical verification      | Check implementation against exact or similarity solution |
| L2    | Semi-analytical verification | Compare against reduced model or ODE solution             |
| L3    | Numerical reference          | Compare against high-resolution reference data            |
| L4    | Experimental validation      | Compare against experimental measurements                 |

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
