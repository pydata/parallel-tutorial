# Parallel Python: Analyzing Large Datasets

[![Join the chat at https://gitter.im/pydata/parallel-tutorial](https://badges.gitter.im/pydata/parallel-tutorial.svg)](https://gitter.im/pydata/parallel-tutorial?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


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
    -  Scaling cross validation parameter search
    -  Tabular data with map/submit
    -  Tabular data with dataframes


## Installation

1.  Download this repository:

        git clone https://github.com/pydata/parallel-tutorial

    or download as a [zip file](https://github.com/pydata/parallel-tutorial/archive/master.zip).

2. Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)
3. Create a new conda environment:

        conda env create -f environment.yml
        source activate parallel  # Linux OS/X
        activate parallel         # Windows

4. If you want to use Spark (this is a large download):

        conda install -c conda-forge pyspark

Test your installation:

    python -c "import concurrent.futures, dask, jupyter"


## Dataset Preparation

We will generate a dataset for use locally.  This will take up about 1GB of
space in a new local directory, `data/`.

    python prep.py


## Part 1: Local Notebooks

Part one of this tutorial takes place on your laptop, using multiple cores.
Run Jupyter Notebook locally and navigate to the `notebooks/` directory.

    jupyter notebook

The notebooks are ordered 1, 2, 3, so you can start with `01-map.ipynb`


## Part 2: Remote Clusters

Part two of this tutorial takes place on a remote cluster.

Visit the following page to start an eight-node cluster:
[https://pydata-parallel.jovyan.org/](https://pydata-parallel.jovyan.org/)

If at any point your cluster fails you can always start a new one by
re-visiting this page.

*Warning: your cluster will be deleted when you close out.  If you want to save
your work you will need to *Download* your notebooks explicitly.*


## Slides

Brief, high level slides exist at
[http://pydata.github.io/parallel-tutorial/](http://pydata.github.io/parallel-tutorial/).


## Sponsored Cloud Provider

We thank Google for generously providing compute credits on
[Google Compute Engine](https://cloud.google.com/compute/).
