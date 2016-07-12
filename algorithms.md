Parallel Data Analysis
----------------------

<img src="images/embarrassing.svg">
<img src="images/shuffle.svg">
<img src="images/reduction.svg">

<hr>

* *Min Ragan-Kelley*:  Simula/Jupyter

* *Matthew Rocklin*:  Continuum/Dask

* *Ben Zaitlen*:  Continuum/Deployment

<hr>

[scipy2016.slack.com/messages/parallelpython](https://scipy2016.slack.com/messages/parallelpython)

[github.com/mrocklin/scipy-2016-parallel/](https://github.com/mrocklin/scipy-2016-parallel/)


## Parallel Algorithms

1.  Map - The simple, common case

2.  Submit - Full freedom

3.  Collections - For common structures


### `map` - The simple, common case

    outputs = []
    for i in inputs:
        outputs.append(f(i))

    # or

    outputs = [f(i) for i in inputs]

    # or

    outputs = map(f, inputs)

<img src="images/embarrassing.svg">

Implemented by *many* frameworks

    concurrent.futures, dask, ipyparallel, joblib, MR, multiprocessing, spark


### `map` - The simple, common case

Frameworks provide a function `map` that takes a function and a sequence and
applies that function in parallel.

    from framework import System

    system = System(initialization_parameters)

    # outputs = map(function, inputs)
    outputs = system.map(function, inputs)


### `submit` - Unstructured

    for a in L1:
        for b in L2:
            if a > b:
                outputs.add(f(a, b))
            else:
                outputs.add(g(a, b))

<img src="images/unstructured.svg">

No restrictions here, but also no magic.  Developer retains full control.

    concurrent.futures, dask, ipyparallel, multiprocessing


### `submit` - Unstructured

*  Submit tasks to framework one-by-one.
*  Run tasks in the background and collect when finished.

<hr>

    future = system.submit(function, *args, **kwargs)

    ... # Do other things

    result = future.result()  # block until done


### `submit` - Unstructured

*  Submit tasks to framework one-by-one.
*  Run tasks in the background and collect when finished.

<hr>

    futures = []
    for i in inputs:
        futures.append(system.submit(function, i))

    results = [f.result() for f in futures]  # block until done


### `submit` - Unstructured

*  Submit tasks to framework one-by-one.
*  Run tasks in the background and collect when finished.

<hr>

    outputs = set()                     # Sequential
    for a in L1:
        for b in L2:
            if a > b:
                outputs.add(f(a, b))
            else:
                outputs.add(g(a, b))

<hr>

    futures = set()                     # Parallel
    for a in L1:
        for b in L2:
            if a > b:
                outputs.add(system.submit(f, a, b))
            else:
                outputs.add(system.submit(g, a, b))

    results = {f.result() for f in futures}


### Collections - Semi-structured

    (x.T.dot(x) + 1).sum()                  # big arrays
    df.groupby(df.time).value.mean()        # big tables
    collection.map(f).groupby(key).count()  # big lists

<img src="images/embarrassing.svg">
<img src="images/shuffle.svg">
<img src="images/reduction.svg">


### Collections provide a fixed set of operations

*  `collection.map(function)`
*  `collection.filter(predicate)`
*  `collection.groupby(key)`
*  `collection.join(other_collection)`

Chain operations together for complex computations

    collection.map(function)
              .filter(predicate)
              .groupby(key)
              .reduction()

Implemented by

    dask, spark, big array libraries, parallel databases, etc..


### Compare algorithm types

*  Map
    *  Most common problem type
    *  Easy to find a good framework to match
    *  Really consistent API
*  Submit
    *  Most flexible solution type
    *  Less common for frameworks, but available
*  Collections
    *  Good fit when they're a good fit
    *  Frameworks abound, some awkwardness in rewriting
