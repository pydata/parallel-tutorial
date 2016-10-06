### Parallel solution

from concurrent.futures import ThreadPoolExecutor
e = ThreadPoolExecutor(4)

def corr(a, b):
    return a.corr(b)

futures = {}

for a in filenames:
    for b in filenames:
        if a != b:
            futures[a, b] = e.submit(corr, series[a], series[b])

results = {k: v.result() for k, v in futures.items()}
