# networkie (engineering workflows on network data)
[![License](https://img.shields.io/badge/license-GPL-green.svg?style=flat)](https://github.com/junipertcy/networkie/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/junipertcy/networkie.svg?branch=master)](https://travis-ci.org/junipertcy/networkie)

Introduction to engineering workflows on network data for undergraduates.

The modules are organized as follows

*  **gen:**  Synthetic network data generation via various models.
   Current implementation includes `Erdős–Rényi model` and `Gaussian mixture model` (to be implemented).
*  **partition:** Graph partitioning via various methods.
*  **transform:** Network data transformation between various formats.
   Current implementation includes transformation between the plain text `edgelist` file and the Numpy.ndarray `matrix` format.
*  **viz:** Network visualization module.
*  **dataset:** Network dataset for the project.


## Getting started
First things first, please [fork this repository](https://help.github.com/articles/fork-a-repo/) on your GitHub.
And then, clone this repository locally on your computer.
```commandline
git clone https://github.com/YOUR-USERNAME/data-engineering-tutorial.git
``` 

Now, let's install the libraries needed by the project.
We will do so by installing the libraries into existing environment.
However, a better practice is to [create a new environment for the project](http://docs.python-guide.org/en/latest/dev/virtualenvs/). 
```commandline
conda install ******
```
Oh, did I mention that Anaconda (which ships with `conda`) is an useful package management tool for Python?
To download Anaconda Distribution, visit [here](https://www.anaconda.com/download/).

If you have pulled the codes, it should now be ready to work!
To test its functionalities, let's first prepare some synthetic data.
From the repo directory, run:
```commandline
python scripts/prep.py
```

And then, run:
```commandline
python scripts/test.py
```

Note that building unit test pipelines (_citation needed_) along with main analytic codes is an important part of software developement.
However, due to time constraint, we will not focus on this topic. 


## Outline

1. [Overview](tutorials/01_overview.ipynb) - introduction to basic tools, e.g. git, GitHub, Python.

2. [Foundations](tutorials/02_foundations.ipynb) - Using `networkx` to represent network data;
 
3. [Visualization](tutorials/03_visualization.ipynb) - TBD.

4. [Analysis](tutorials/04_analysis.ipynb) - TBD.

## Reference
1. The GitHub repository [Network Analysis Made Simple](https://github.com/ericmjl/Network-Analysis-Made-Simple) by Eric Ma.
2. Ball, B., & Newman, M. (2013). Friendship networks and social status. Network Science, 1(1), 16-30. [paper](https://doi.org/10.1017/nws.2012.4)
