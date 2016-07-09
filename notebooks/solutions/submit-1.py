### Parallel Version

def slowadd(a, b, delay=1):
    sleep(delay)
    return a + b

def slowsub(a, b, delay=1):
    sleep(delay)
    return a - b

futures = []
for i in range(5):
    for j in range(5):
        if i < j:
            futures.append(e.submit(slowadd, i, j, delay=1))
        elif i > j:
            futures.append(e.submit(slowsub, i, j, delay=1))

results = [f.result() for f in futures]
