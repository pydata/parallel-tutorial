from concurrent.futures import ThreadPoolExecutor
e = ThreadPoolExecutor()

futures = []

parameters = list(param_samples)

for split in cv_splits:
    for params in parameters:
        future = e.submit(evaluate_one, SVC, params, split)
        futures.append(future)

results = [f.result() for f in futures]
