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

## Chat Room

Stuck? Ask for help here: https://gitter.im/dask/pydata-dc-2016 

## Installation

1. Install [Anaconda](https://www.continuum.io/downloads)
2. Update select packages

    Everyone:

        conda install -c conda-forge ipyparallel ujson dask distributed bokeh scikit-learn pytables jupyter
        pip install snakeviz dask distributed --upgrade

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


## Part 1: Local Notebooks

Part one of this tutorial takes place on your laptop, using multiple cores.
Run Jupyter Notebook locally and navigate to the `notebooks/` directory.

    jupyter notebook

The notebooks are ordered 1, 2, 3, so you can start with `01-map.ipynb`


## Part 2: Remote Clusters

Part two of this tutorial takes place on a remote cluster.

Visit the following page to start an eight-node cluster:
[http://bigfatintegral.net/](http://bigfatintegral.net/)

If at any point your cluster fails you can always start a new one by
re-visiting this page.

*Warning: your cluster will be deleted when you close
out.  If you want to save your work you will need to *Download* your notebooks
explicitly.*


## Slides

Brief, high level slides exist at
[http://mrocklin.github.com/scipy-2016-parallel/](http://mrocklin.github.com/scipy-2016-parallel/).


## Sponsored Cloud Provider

We thank Google for generously providing compute credits on
[Google Compute Engine](https://cloud.google.com/compute/).
