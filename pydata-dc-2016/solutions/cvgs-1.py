from concurrent.futures import ThreadPoolExecutor
e = ThreadPoolExecutor()

futures = []

for split in cv_splits:
    for params in param_samples:
        future = e.submit(evaluate_one, SVC, params, split)
        futures.append(future)
        
results = [f.result() for f in futures]
