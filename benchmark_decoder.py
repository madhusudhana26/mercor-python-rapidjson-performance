import time
import statistics
from pathlib import Path
import rapidjson

JSON_PATH = Path("benchmarks/json/canada.json")

data = JSON_PATH.read_text(encoding="utf-8")

decoder = rapidjson.Decoder()

WARMUPS = 3
RUNS = 7
ITERATIONS = 250

def workload():
    for _ in range(ITERATIONS):
        decoder(data)

# warmup
for _ in range(WARMUPS):
    workload()

times = []

for i in range(RUNS):
    start = time.perf_counter()
    workload()
    elapsed = time.perf_counter() - start
    times.append(elapsed)
    print(f"Run {i+1}: {elapsed:.4f}s")

median = statistics.median(times)
iqr = statistics.quantiles(times, n=4)[2] - statistics.quantiles(times, n=4)[0]

print("\nRESULTS")
print(f"Median: {median:.4f}s")
print(f"IQR: {iqr:.4f}s")