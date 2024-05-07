# joanapy

Joint continuous multi-Omics enrichment ANAlysis (JOANA) from MLO Lab.

## Install joanapy
We recommend utilizing conda for environment management, and pip for installing joanapy as a Python package. Follow these instructions to set up and activate joanapy

```
conda create -n joana python=3.11
conda activate joana
```
Make sure that your working directory is JOANA. 
Use pip to install joanapy on your conda environment.

```
pip install .
```

after installing joanapy on joana environment run JOANA through run-joana function.

```
run-joana [-o omics1.txt] [-o2 omics2.txt] [-p pathwayfile.gmt] [-d input-output-directory-path] [-m min-num-genes]
-o gene names with signifficant scores (e.g. q-values) a two-column tab delimited file (input file name).
-o2 gene names and correspond significant scores of the second modality (optional when you want to run joana with multi-omics data) (input file name)
-p the name of 'gmt' file which contains biological pathways
-d specify the path that all your input files are there and also your result directory would be on that path
-m its a number [0,1) which specified by client (default value is 0). '-m 0.5' means JOANA consider pathways which atleast 50% of its genes have measurments.   

```

The input files -o and -o2 should be a two-column tab-delimited file the first column geneNames and the second column significant scores(e.g. p-values, or adj-pvalues, ...) with the following format:

```
TMEM171  0.212951673007631
AGR3  0.212951673007631
KIR2DL3  0.212951673007631
CROCC2  0.212951673007631
PRSS3  0.212951673007631
TGM2 0.212951673007631   
```

The 'gmt' file could be provided by downloading from msigDB or any other desired file with gmt format.

To execute JAOAN on single-omics data if you are already in the directory of input data, the command line would be:

```
run-joana -o omics1.txt -p pathway.gmt -d ./ -m 0.7

```
And to execute JAOAN on multi-omics data if you are already in the directory of input data, the command line would be:

```
run-joana -o omics1.txt -o2 omics2.txt -p pathway.gmt -d ./ -m 0.7

```

## Example
An example for how to run JOANA with joanapy can be found in the joanapy/tests folder.

## Uninstall joanapy
The package can be uninstalled with the following command:

```
pip uninstall joanapy
```


## Fitting a mixture of Beta distributions
Code was adapted from Schröder C, Rahmann S. A hybrid parameter estimation algorithm for beta mixtures and applications to methylation state classification. Algorithms Mol Biol. 2017 Aug 18;12:21. doi: 10.1186/s13015-017-0112-1. PMID: 28828033; PMCID: PMC5563068 (https://bitbucket.org/genomeinformatics/betamix/src/master/).
