#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
source ssshtest

pycodestyle get_tissue_samples.py
pycodestyle get_gene_counts.py
pycodestyle box.py

run test_get_tissue_samples python get_tissue_samples.py \ 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt' 'SMTS' '_sampids.txt'
assert_no_stdout

run test_get_gene_counts python get_gene_counts.py \ "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz" "SDHB" '_counts.txt'
assert_no_stdout

run test_boxplot python box.py --tissues Brain --genes SDHB --out_file_name _plot.png
assert_exit_code 0
