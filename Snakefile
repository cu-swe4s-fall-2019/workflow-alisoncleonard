"""
Snakefile to run SWE4S homework 10
"""

TISSUE_GROUP = 'SMTS'
GENES = ["SDHB", "MEN1", "KCNH2", "MSH2", "MYL2", "BRCA2"]
TISSUES = ['Brain', 'Heart', 'Blood', 'Skin']


rule all:
    input: expand('{tissue}_plot.png', tissue=TISSUES)

rule get_tissue_samples:
    input: 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output: 'SMTS_sampids.txt'
    shell: 'python get_tissue_samples.py ' \
     + "{input} 'SMTS' '_sampids.txt'"

rule get_gene_counts:
    input: "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
    output: expand('{gene}_counts.txt', gene=GENES)
    shell: 'for gene in {GENES}; do python get_gene_counts.py {input} $gene ' \
    + '_counts.txt; done'

rule boxplot:
    input:
        expand("{group}_sampids.txt", group=TISSUE_GROUP),
        expand('{gene}_counts.txt', gene=GENES)
    output: expand('{tissue}_plot.png', tissue=TISSUES)
    shell: 'python box.py --tissues Brain Heart Blood Skin --genes SDHB MEN1 ' \
    + 'KCNH2 MSH2 MYL2 BRCA2 --out_file_name _plot.png'
