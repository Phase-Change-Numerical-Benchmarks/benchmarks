# Contributing

We welcome contributions of new phase-change benchmarks, corrections, reference data, and numerical results.

## Proposing a new benchmark

Open an issue using the title:

```text
New benchmark proposal: PA-XXX short title
```

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


## File naming

Use:

```text
cases/PA-XXX-short-title.md
```

Examples:

```text
cases/PA-001-planar-one-phase-stefan.md
cases/PA-002-planar-two-phase-stefan.md
cases/PA-003-frank-disk.md
cases/PA-004-frank-sphere.md
```