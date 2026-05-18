\# Mercor Performance Engineering Trial Notes



\## Repository Selection

Repository: python-rapidjson

Reason:

\- Native C++ extension with Python bindings

\- Existing benchmark infrastructure

\- Real-world JSON parsing workloads

\- Stable test suite

\- Reproducible CPU-bound benchmark behavior



\## Environment

OS: Windows 11

Python: 3.11

Benchmark target environment: Google Colab CPU runtime



\## Build Validation

\- pip install . -> PASS

\- pytest tests -> 935 passed, 17 skipped, 2 xfailed



\## Benchmark Workload

Dataset:

\- benchmarks/json/canada.json



Reason for selection:

\- Large real-world JSON payload

\- Stable deterministic workload

\- Existing upstream benchmark dataset

\- Suitable for repeated deserialization performance testing



\## Benchmark Methodology

Warmup runs: 3

Measured runs: 7

Metric:

\- Median runtime

\- IQR



\## Baseline Benchmark Results

Median runtime:

\~14.25s



IQR:

\~0.24s



\## Profiling Summary

Primary hotspot:

rapidjson.loads()



Observation:

\- Runtime dominated by native deserialization path

\- Python-side overhead minimal

\- Benchmark setup overhead negligible



\## Optimization Direction

Goal:

\- Reduce repeated deserialization overhead

\- Minimize temporary allocation / conversion overhead where safely possible

\- Preserve correctness and existing test behavior



\## Important Constraints

\- No parser semantic changes

\- No dependency swaps

\- No unsafe threading/SIMD rewrites

\- Maintain reproducibility and correctness

