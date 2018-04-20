# networkie [![License](https://img.shields.io/badge/license-GPL-green.svg?style=flat)](https://github.com/junipertcy/networkie/blob/master/LICENSE) [![Build Status](https://travis-ci.org/junipertcy/networkie.svg?branch=master)](https://travis-ci.org/junipertcy/networkie)

Introduction to the engineering workflow on network data for undergraduates.

The `networkie` libray is organized with the following modules:

*  **gen:**  Network object generation via various generative models, including loading from custom data.
   Current implementation includes `Custom`. There are virtual classes for `Erdős–Rényi model` and `Gaussian mixture model` (will be implemented in the future).
*  **partition:** Graph partitioning via various methods. Current implementation includes `Louvain`.
*  **transform:** Network data transformation between various formats. Current implementation includes the `Edgelist` class. It is designed to transform `*.edgelist` txt data to other formats.
   Current implementation includes transformation between the plain text `edgelist` file and the Numpy.ndarray `matrix` format.
*  **viz:** Network visualization module.
*  **dataset:** Network data sets for the project.

More broadly, the repository is organized as follows:

*  **build_tools** Continuous integration related scripts.
*  **dataset** Network data sets.
*  **homework** Homework designed for learning network analysis with the library.
*  **networkie** Main library of the `networkie`.
*  **scripts** Other scripts, including the script that parses Google Forms' raw csv file.
*  **tests** Scripts for unit tests via `pytest`.

The main function for the files in the root directory is as follows:

*  **.gitattributes** Attributes for the Git repo. Here, we ask Git to ignore counting `*.ipynb` files as part of the code contribution in the repo.
*  **.gitignore** Listing of the files (and file extensions) that you would like Git to ignore.
*  **.travis.yml** Configuration file for [travis-ci](http://travis-ci.org/).
*  **LICENSE** License for the project. Here, we use [GNU GPLv3](http://choosealicense.online/licenses/gpl-3.0/) because we cared about sharing improvements.
*  **pytest.ini** Configuration file for the `pytest` framework.
*  **README.md** The readme file for the project.
*  **requirements.txt** The libraries that you have to install before running the code of the project smoothly.
*  **requirements_test.txt** The libraries that you have to install before running the code of the project smoothly; when running in a test mode.
*  **\*.ipynb** Jupyter Notebooks that are useful for learning.


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
conda install numpy jupyter networkx pytest
```
Or, you may simply do:
```commandline
pip install -r requirements.txt
pip install -r requirements_test.txt
```
Oh, did I mention that Anaconda (which ships with `conda`) is an useful package management tool for Python?
To download Anaconda Distribution, visit [here](https://www.anaconda.com/download/).

If you have pulled the codes, it should now be ready to work!
To make sure the code works well, run the unit tests:
```commandline
pytest
```

If `pytest` shows a green pass sign, you should be ready!

## Outline

We use these `*.ipynb` files to illustrate the use of `networkx` in analyzing the in-class social network data.
For more info, please check out the references.

1. [Overview](tutorials/01_overview.ipynb) - introduction to basic tools, e.g. git, GitHub, Python.

2. [Foundations](tutorials/02_foundations.ipynb) - Reading files, importing data, creating the Graph, adding attributes to the graph.
 
3. [Analysis](tutorials/03_analysis.ipynb) - centrality measures, community detection with modularity (TODO).

4. [Visualization](tutorials/04_visualization.ipynb) - network visualization.


## Reference
1. [Network Analysis Made Simple](https://github.com/ericmjl/Network-Analysis-Made-Simple) by Eric Ma on GitHub. We will go through some parts of the repo in the lecture.
2. [Exploring and Analyzing Network Data with Python](https://programminghistorian.org/lessons/exploring-and-analyzing-network-data-with-python), yet another example for using `networkx`, with a focus on analyzing humanities data.
3. Ball, B., & Newman, M. (2013). Friendship networks and social status. Network Science, 1(1), 16-30. The [paper](https://doi.org/10.1017/nws.2012.4) illustrates an interesting research work on generic in-class social network data.
