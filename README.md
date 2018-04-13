# networkie [![License](https://img.shields.io/badge/license-GPL-green.svg?style=flat)](https://github.com/junipertcy/networkie/blob/master/LICENSE) [![Build Status](https://travis-ci.org/junipertcy/networkie.svg?branch=master)](https://travis-ci.org/junipertcy/networkie)

Introduction to the engineering workflow on network data for undergraduates.

The `networkie` modules are organized as follows:

*  **gen:**  Synthetic network data generation via various models.
   Current implementation includes `Erdős–Rényi model` and `Gaussian mixture model` (to be implemented).
*  **partition:** Graph partitioning via various methods.
*  **transform:** Network data transformation between various formats.
   Current implementation includes transformation between the plain text `edgelist` file and the Numpy.ndarray `matrix` format.
*  **viz:** Network visualization module.
*  **dataset:** Network dataset for the project.

More broadly, the repository is organized as follows:

*  **build_tools** Continuous integration related scripts.
*  **dataset** Network dataset.
*  **homework** Homework designed for learning network analysis with the library.
*  **networkie** Main library of the `networkie`.
*  **scripts** Other scripts.
*  **tests** Scripts for unit tests via `pytest`.
*  **tutorials** Jupyter Notebooks that are useful for learning the library (and network analysis).

The main function for the files in the root directory is as follows:

*  **.gitattributes** Attributes for the Git repo. Here, we ask Git to ignore counting `*.ipynb` files as part of the code contribution in the repo.
*  **.gitignore** Listing of the files (and file extensions) that you would like Git to ignore.
*  **.travis.yml** Configuration files for [travis-ci](http://travis-ci.org/).
*  **LICENSE** License for the project. Here, we use [GNU GPLv3](http://choosealicense.online/licenses/gpl-3.0/) because we cared about sharing improvements.
*  **pytest.ini** Configuration file for the `pytest` framework.
*  **README.md** The readme file for the project.
*  **requirements.txt** The libraries that you have to install before running the code of the project smoothly.
*  **requirements_test.txt** The libraries that you have to install before running the code of the project smoothly; when running in a test mode.

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
conda install numpy jupyter python-igraph
```
Oh, did I mention that Anaconda (which ships with `conda`) is an useful package management tool for Python?
To download Anaconda Distribution, visit [here](https://www.anaconda.com/download/).

If you have pulled the codes, it should now be ready to work!
To test whether the code runs well, let's first install the library for unit testing:

```commandline
conda install pytest
```

Then, run:
```commandline
pytest
```

If `pytest` shows a green pass sign, you should be ready!

## Outline

1. [Overview](tutorials/01_overview.ipynb) - introduction to basic tools, e.g. git, GitHub, Python.

2. [Foundations](tutorials/02_foundations.ipynb) - Using `networkx` to represent network data;
 
3. [Visualization](tutorials/03_visualization.ipynb) - TBD.

4. [Analysis](tutorials/04_analysis.ipynb) - TBD.

## Reference
1. The GitHub repository [Network Analysis Made Simple](https://github.com/ericmjl/Network-Analysis-Made-Simple) by Eric Ma.
2. Ball, B., & Newman, M. (2013). Friendship networks and social status. Network Science, 1(1), 16-30. [paper](https://doi.org/10.1017/nws.2012.4)
