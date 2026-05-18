\# Performance Engineering Take-Home: python-rapidjson



\## Repository Selection



Repository: `python-rapidjson`



License:

\- MIT License



Repository URL:

\- https://github.com/python-rapidjson/python-rapidjson



Why this repository:

\- Native C++ extension with Python bindings

\- Existing benchmark infrastructure

\- Real-world JSON parsing workloads

\- Mature automated test suite

\- Realistic CPU-bound deserialization performance characteristics



The repository satisfies the assignment requirements:

\- Public open-source repository

\- Permissive license

\- Existing automated tests

\- Existing benchmark workloads

\- Mature Git history



\---



\# Baseline Commit



Baseline repository commit used during experimentation:



(To be filled before submission using final chosen SHA)



\---



\# Workload Selection



The selected workload focuses on repeated JSON deserialization using:



```python

rapidjson.loads()


# Reproducibility Notes

All benchmarks were performed using repeated warmup and measured runs on CPU-only environments.

The investigation prioritized:
- reproducibility
- correctness preservation
- transparent methodology

over unsafe parser modifications or unverifiable benchmark gains.