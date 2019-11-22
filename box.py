"""
box.py plots the gene expression distribution across a set of genes for a set
of tissue groups. The set of tissue groups, the set of genes, and the output
file should be passed as command-line parameters. Data will be drawn from
txt files saved in the current directory.
"""

import argparse
import matplotlib
import matplotlib.pyplot as plt
import sys
import os.path
from os import path
matplotlib.use('Agg')


def main():
    """Create a boxplot across a set of genes for a set of tissue groups and
    save the graph to an output file.

    Parameters
    ----------
    --tissues: list of tissues to plot

    --genes: list of genes to plot

    --out_file_name: The file name the graph will be saved under. Must use a
    supported file extension, such as .png. Input as a string.

    Returns
    _________

    Box plot of the input gene counts for the input tissues, saved as
    out_file_name in the current directory.

    """

    parser = argparse.ArgumentParser(description='boxplot gene count data '
                                     'by tissue', prog='box.py')

    parser.add_argument('--tissues', nargs='*', type=str,
                        help='tissues to plot', required=True)

    parser.add_argument('--genes', nargs='*', type=str, help='Genes to plot',
                        required=True)

    parser.add_argument('--out_file_name', type=str, help='Name for '
                        'saved output file', required=True)

    args = parser.parse_args()

    tissues = args.tissues  # tissues is a list of strings

    genes = args.genes  # genes is a list of strings

    outfile = args.out_file_name

    for tissue in tissues:
        counts_by_gene_list = []
        sampleid_list = []
        try:
            tissue_file = open('SMTS_sampids.txt', 'r')
            for line in tissue_file:
                line_split = line.rstrip().split(',')
                if line_split[0] == str(tissue):
                    sampleid_list.append(line_split[1])
        except FileNotFoundError:
            print('Could not find input data file')
            sys.exit(1)

        for gene in genes:
            counts_list = []
            try:
                gene_file = open(str(gene) + '_counts.txt', 'r')
                for line in gene_file:
                    line_split = line.rstrip().split(',')
                    if line_split[0] in sampleid_list:
                        counts_list.append(int(line_split[1]))
            except FileNotFoundError:
                print('Could not find input data file')
                sys.exit(1)

            counts_by_gene_list.append(counts_list)

        width = 10
        height = 3

        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1, 1, 1)

        ax.boxplot(counts_by_gene_list)
        ax.set_title(str(tissue))
        # set custom labels with the names of each list
        ax.set_xticklabels(genes)
        plt.xticks(rotation=90)
        ax.set_xlabel('genes')
        ax.set_ylabel('counts')
        plt.yscale('log')

        plt.savefig(str(tissue) + outfile, bbox_inches='tight')


if __name__ == '__main__':
    main()
