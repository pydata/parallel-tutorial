# Parallel Python: Analyzing Large Datasets

## Student Goals

Students will walk away with a high-level understanding of both parallel problems and how to reason about parallel computing frameworks.
They will also walk away with hands-on experience using a variety of frameworks easily accessible from Python.

## Student Level

Knowledge of Python and general familiarity with the Jupyter notebook are assumed.
This is generally aimed at a beginning to intermediate audience.


## Outline

For the first half, we will cover basic ideas and common patterns encountered when analyzing large
data sets in parallel. We start by diving into a sequence of examples that require increasingly
complex tools. From the most basic parallel API: map, we will cover some general asynchronous
programming with Futures, and high level APIs for large data sets, such as Spark RDDs and Dask
collections, and streaming patterns. For the second half, we focus on traits of particular parallel
frameworks, including strategies for picking the right tool for your job. We will finish with some
common challenges in parallel analysis, such as debugging parallel code when it goes wrong, as well
as deployment and setup strategies.


- Part one
    - Parallel Map
    - Asynchronous Futures
    - High Level Datasets
    - Streaming
- Part two
    - Processes and Threads.  The GIL, inter-worker communication, and contention.
    - Latency and overhead.  Batching, profiling.
    - Communication mechanisms.  Sockets, MPI, Disk, IPC.
    - Stuff that gets in the way.  Serialization, Native vs JVM, Setup, Resource Managers, Sample Configurations
    - Debugging async and parallel code / Historical perspective


## Installation

1. Install [Anaconda](https://www.continuum.io/downloads)
2. Update select packages

    Everyone:

        conda install -c conda-forge ipyparallel ujson dask distributed
        pip install snakeviz

    Python 2 users:

        conda install futures

    Linux/Mac users:

        conda install -c quasiben spark

Test your installation:

    python -c 'import concurrent.futures, ipyparallel, dask, jupyter, pyspark'


## Dataset Preparation

We will generate a dataset for use locally.  This will take up about 1GB of
space in a new local directory, `data/`.

    pip install fakestockdata
    python prep.py


## Sponsored Cloud Provider

[Google Compute Engine](https://cloud.google.com/compute/)
