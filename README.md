# Reproducible Project Management

Reproducible project management is the cornerstone of efficient and transparent workflows in the development and collaboration world. It involves implementing practices and utilizing tools that ensure the consistent and reliable reproduction of project results. To ensure reproducibility, creating and publishing packages, and open-source documentation play a key role. In this hands-on session, I will walk you through open-sourcing Python projects with GitHub, publishing packages online through PyPI (Python Package Index), dockerization, and creating detailed documentation with Read the Docs.


## Getting started

The following frameworks are needed to work with this project.
 ### Softwares Installations
```
$ git clone https://github.com/brainhack-vandy/NeuroPreprocessing.git
$ Visual Studio Code installation
$ Docker Desktop installation
$ Python or Anaconda environment
$ pip install numpy nilearn setuptools wheel and twine sphinx sphinx_rtd_theme 
```

#### Accounts needed

```
$ GitHub (https://github.com)
$ Python Package Index (PyPI) (https://pypi.org). Make sure that you genearte API token and save it on your machine
$ Read the Docs (https://readthedocs.org)

```

## Developing an fMRI preprocessing pipeline

We will be using part of our fMRI preprocessing tool, NeuroGraph (https://neurograph.readthedocs.io/en/latest/) that provides a set of tools for downloading, preprocessing and creating graph-based representations and benchmarks. We will use Python programming language. Our project structure is as follows. 

<p align="center">
<img src="structure.png" alt="Alt text" width="50%" height="50%">
</p>

The utils.py file has the implementation for the fMRI preprocessing. main.py file consider a single example and use the pipeline to preprocess the data. 

## Packaging and publishing Python projects

Publishing packages online offers widespread accessibility, allowing developers and researchers across the globe to easily discover, install, and integrate your software into their projects. To publish our package online, we will use the Python Package Index (PyPI). We will use the setup.py file to configure the package, and then we will use the following terminal commands to create the package. 


```
$ python setup.py sdist bdist_wheel (this command should create the distribution folder (dist))
$ twine check dist/*   (this check the package and return errors if any) 
```

Now, to upload the package to PyPI, we create an account on PyPI and obtain the API key. Using the API key, we create a ".pypirc" file and save it in the home folder (~/.pypirc). We can then upload the package to PyPI as follows.

```
$ twine upload dist/*
```
Out Python package is online and is ready to install with

```
$ pip install NeuroPrep
```
## Containerize the Package






