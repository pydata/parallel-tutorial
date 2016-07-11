# Parallel Python: Analyzing Large Datasets

## Student Goals

Students will walk away with a high-level understanding of both parallel
problems and how to reason about parallel computing frameworks.  They will also
walk away with hands-on experience using a variety of frameworks easily
accessible from Python.

## Student Level

Knowledge of Python and general familiarity with the Jupyter notebook are
assumed.  This is generally aimed at a beginning to intermediate audience.


## Outline

For the first half we cover basic ideas and common patterns in parallel
computing, including embarrassingly parallel map, unstructured asynchronous
submit, and large collections.

For the second half we cover complications arising from distributed memory
computing and exercise the lessons learned in the first section by running
informative examples on provided clusters.

- Part one
    - Parallel Map
    - Asynchronous Futures
    - High Level Datasets
- Part two
    - Processes and Threads.  The GIL, inter-worker communication, and contention.
    - Distributed deployment
    - Cluster computing exercises

## Installation

1. Install [Anaconda](https://www.continuum.io/downloads)
2. Update select packages

    Everyone:

        conda install -c conda-forge ipyparallel ujson dask distributed bokeh
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
