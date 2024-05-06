# joanapy
Joint continuous multi-Omics enrichment ANAlysis (JOANA).

## Build and install joanapy

Make sure that your working directory is JOANA. 

We recommend utilizing conda for environment management, and pip for installing joanapy as a Python package. Follow these instructions to set up and activate joanapy
```
conda create -n joana python=3.11
conda activate joana

```
use pip to install joanapy on your conda environment

```
pip install .
```
The package can be uninstalled with the following command:

```
pip uninstall joanapy
```

## Example
An example for how to run JOANA with joanapy can be found in the joanapy/tests folder.

## Fitting a mixture of Beta distributions
Code was adapted from Schröder C, Rahmann S. A hybrid parameter estimation algorithm for beta mixtures and applications to methylation state classification. Algorithms Mol Biol. 2017 Aug 18;12:21. doi: 10.1186/s13015-017-0112-1. PMID: 28828033; PMCID: PMC5563068 (https://bitbucket.org/genomeinformatics/betamix/src/master/).
