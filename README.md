# workflow-alisoncleonard

## Purpose

This github repository contains code to plot the frequency of rna transcripts
'gene counts' for different genes in a given tissue, using data from the
Genotype-Tissue Expression (GTEx) Project. More information on the GTEx Project
can be found here <https://commonfund.nih.gov/gtex>.

## How to use

The repository contains 3 scripts necessary to extract and plot data:

get_tissue_samples.py takes a sample attributes file, a tissue group (SMTS),
and output file as parameters, and creates a file with all of the samples ids
(SAMPID) for that tissue group.

get_gene_counts.py takes a gene count file, a gene name, and an output file as
parameters, and creates a file with the sample ids and counts for that gene.

box.py plots the gene expression distribution across a set of genes for a set
of tissue groups. The set of tissue groups, the set of genes, and the output
file should be passed as command-line parameters. Data will be drawn from
txt files saved in the current directory.

These scripts are accompanied by a Snakefile to plot data from the genes SDHB,
MEN1, KCNH2, MSH2, MYL2, and "BRCA2 in the tissues blood, brain, heart, and
skin.

## How to install

language: python

before_install:
    - wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    - bash Miniconda3-latest-Linux-x86_64.sh -b
    - . /home/travis/miniconda3/etc/profile.d/conda.sh
    - conda update --yes conda
    - conda config --add channels r
    - conda create --yes -n test
    - conda activate test
    - conda install -y pycodestyle
    - conda install --yes python=3.6
    - conda install -y matplotlib
    - conda install -y -c bioconda -c conda-forge snakemake

script:
    - snakemake

Code is available at <https://github.com/cu-swe4s-fall-2019/workflow-alisoncleonard> 
