"""
get_tissue_samples.py takes a sample attributes file, a tissue group (SMTS),
and output file as parameters, and creates a file with all of the samples ids
(SAMPID) for that tissue group.
"""

import argparse


def main():
    """Creates an output file with sample ids for each tissue

    Parameters
    -----------
    --sample_input_file : A txt file containing sample identification
    information, corresponding to data in the .gz file. Input as a string.
    ex. 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'

    --tissue_group : Data is displayed by tissue, and can be sorted by
    tissue groups (SMTS) or tissue types (SMTSD). Input either 'SMTS' or
    'SMTSD' as a string.

    --output_file_name: File name to save the output data fle.

    Returns
    --------

    Function returns an output file containing sample ids grouped by tissue

    """
    parser = argparse.ArgumentParser(description='extract sample id info',
                                     prog='get_tissue_samples.py')

    parser.add_argument('--sample_info_file', type=str, help='Name of sample'
                        'info input file', required=True)

    parser.add_argument('--tissue_group', type=str, help='Select either'
                        'tissue groups (SMTS) or tissue types (SMTSD)',
                        required=True)

    parser.add_argument('--output_file_name', type=str, help='Name for saved'
                        'output file', required=True)

    args = parser.parse_args()

    try:
        # file with informational headers for each sample
        sample_info_file_name = args.sample_info_file
    except FileNotFoundError:
        print('Could not find input data file')
        sys.exit(1)
    except PermissionError:
        print('Could not open input data file')
        sys.exit(1)

    # chose either tissue groups (SMTS) or tissue types (SMTSD)
    group_col_name = args.tissue_group

    output_file_name = args.output_file_name
    outfile = open(output_file_name, 'w')

    # SAMPID is from column 0, SMTS column 5, SMTSD column 6
    for l in open(sample_info_file_name):
        line_split = l.rstrip().split('\t')
        if group_col_name == 'SMTS':
            text = str(line_split[5]) + ',' + str(line_split[0]) + "\n"
            outfile.write(text)
        if group_col_name == 'SMTSD':
            text = str(line_split[6]) + ',' + str(line_split[0]) + "\n"
            outfile.write(text)
    outfile.close()


if __name__ == '__main__':
    main()
