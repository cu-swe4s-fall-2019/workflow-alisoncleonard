"""
get_gene_counts.py takes a gene count file, a gene name, and an output file as
parameters, and creates a file with the sample ids and counts for that gene.
"""

import argparse
import gzip


def main():
    """Creates an output file with sample ids and counts for an input gene,
    reading data from a gene count file.

    Parameters
    -----------
    gene_count_file : A GTEx_Analysis file ending in '.gct.gz'. Contains
    measured gene expression level by tissue type. Input as a string.
    ex. 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'

    gene_name : The gene of interest. Input as a string. A full
    list of available genes can be found here: https://github.com/swe4s/
    lectures/blob/master/data_integration/gtex/acmg_genes.txt

    output_file_name_base: File name to save the output data file.

    Returns
    --------

    Function returns an output file containing sample ids and counts for the
    gene of interest.

    """

    parser = argparse.ArgumentParser(description='extract gene count data from'
                                     'gtex files', prog='get_gene_counts.py')

    parser.add_argument('gene_count_file', type=str, help='Name of gene'
                        'count input file')

    parser.add_argument('gene_name', type=str, help='Gene of interest')

    parser.add_argument('output_file_name_base', type=str, help='Name for '
                        'saved output file')

    args = parser.parse_args()

    gene_name = args.gene_name

    try:
        # file with gene read counts for each sample
        data_file_name = args.gene_count_file
    except FileNotFoundError:
        print('Could not find input data file')
        sys.exit(1)
    except PermissionError:
        print('Could not open input data file')
        sys.exit(1)

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    output_file_name = str(gene_name) + str(args.output_file_name_base)
    outfile = open(output_file_name, 'w')

    gzip_file = gzip.open(data_file_name, 'rt')

    for l in gzip.open(data_file_name, 'rt'):

        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = l.rstrip().split('\t')
            continue

        # remove first and second items from list (not sample ids)
        data_header.pop(0)
        data_header.pop(0)
        sample_ids = data_header

        A = l.rstrip().split('\t')

        for i in range(len(sample_ids)):
            if A[gene_name_col] == gene_name:
                SAMPID = sample_ids[i]
                count = A[i + 2]
                outfile.write(SAMPID + ',' + count + "\n")

    outfile.close()


if __name__ == '__main__':
    main()
