# Contributing

We welcome contributions of new phase-change benchmarks, corrections,
reference data, and numerical results.

## Proposing a new benchmark

Open an issue using the title:

```text
New benchmark proposal: PC-XXX short title
````

The proposal should include:

* physical process,
* governing equations,
* boundary conditions,
* material properties,
* reference solution or reference data,
* quantities of interest,
* known numerical difficulties,
* bibliography.

## Benchmark quality levels

A benchmark can be merged as `draft` if the physical idea is clear.

It can be marked `ready` only if:

* equations are specified,
* initial and boundary conditions are unambiguous,
* material parameters are listed,
* quantities of interest are defined,
* reference data or reference formula is available.

It can be marked `community-tested` when at least two independent numerical
methods have submitted comparable results.

## File naming

Use:

```text
cases/PC-XXX-short-title.md
```

Examples:

```text
cases/PC-001-planar-one-phase-stefan.md
cases/PC-003-sucking-interface.md
cases/PC-004-scriven-spherical-bubble-growth.md
```

## Result submissions

Numerical results should be submitted in:

```text
data/PC-XXX/submissions/SOLVER_NAME/
```

with:

```text
metadata.yml
interface_position.csv
temperature_profile.csv
figures/
```

## Required metadata

```yaml
solver: Solver name
authors:
  - Name
method: VOF / level-set / front-tracking / cut-cell / phase-field / enthalpy
grid_type: Cartesian / unstructured / adaptive
spatial_resolution: ...
time_step: ...
final_time: ...
interface_method: ...
phase_change_model: ...
date: YYYY-MM-DD
```