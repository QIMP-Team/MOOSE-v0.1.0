#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------------------------------
# Author: Lalith Kumar Shiyam Sundar
# Institution: Medical University of Vienna
# Research Group: Quantitative Imaging and Medical Physics (QIMP) Team
# Date: 09.02.2023
# Version: 2.0.0
#
# Description:
# The main module of the mooseZ. It contains the main function that is executed when the mooseZ is run.
#
# Usage:
# The main function in this module is executed when the mooseZ is run.
#
# ----------------------------------------------------------------------------------------------------------------------

import argparse
import logging
import os
from datetime import datetime
from halo import Halo
from moosez import display
from moosez import download
from moosez import file_utilities
from moosez import input_validation

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO,
                    filename=datetime.now().strftime('moosez-v.2.0.0.%H-%M-%d-%m-%Y.log'),
                    filemode='w')


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--main_directory", type=str, help="Main directory containing subject folders",
                        required=True)

    parser.add_argument("-m", "--model_name", type=str, help="Name of the model to use for segmentation",
                        choices=["clin_ct_bones",
                                 "clin_ct_ribs",
                                 "clin_ct_vertebrae",
                                 "clin_ct_muscles",
                                 "clin_ct_lungs",
                                 "clin_ct_fat",
                                 "clin_ct_vessels",
                                 "clin_ct_organs",
                                 "clin_pt_fdg_tumor",
                                 "clin_ct_all",
                                 "clin_fdg_pt_ct_all",
                                 "preclin_mr_all"], required=True)
    args = parser.parse_args()

    parent_folder = os.path.abspath(args.main_directory)
    model_name = args.model_name

    display.logo()
    display.citation()

    logging.info('****************************************************************************************************')
    logging.info('                                     STARTING MOOSE-Z V.2.0.0                                       ')
    logging.info('****************************************************************************************************')

    # INPUT VALIDATION AND PREPARATION

    logging.info(' ')
    logging.info('- Main directory: ' + parent_folder)
    logging.info('- Model name: ' + model_name)
    logging.info(' ')
    print(' ')
    print(' NOTE:')
    print(' ')
    display.expectations(model_name)

    # DOWNLOADING THE MODEL
    print('')
    print(' MODEL DOWNLOAD:')
    print('')
    model_path = file_utilities.nnunet_folder_structure()
    download.model(model_name, model_path)

    # CHECKING FOR EXPECTED MODALITIES

    with open(os.devnull, "w") as devnull:
        old_stdout = os.dup(1)
        os.dup2(devnull.fileno(), 1)

        # Call the function with suppressed output
        modalities = display.expected_modality(model_name)

        # Restore stdout
        os.dup2(old_stdout, 1)

    # SETTING UP DIRECTORY STRUCTURE

    print('')
    print(' SETTING UP MOOSE-Z DIRECTORY FOR BATCH PROCESSING:')
    print('')
    logging.info(' ')
    logging.info(' SETTING UP MOOSE-Z DIRECTORY FOR BATCH PROCESSING:')
    logging.info(' ')
    moose_dir, input_dirs, output_dirs = file_utilities.moose_folder_structure(parent_folder, model_name, modalities)
    print(f" MOOSE directory for the current run set at: {moose_dir}")
    logging.info(f" MOOSE directory for the current run set at: {moose_dir}")

    # INPUT STANDARDIZATION

    print('')
    print(' STANDARDIZING INPUT DATA:')
    print('')
    logging.info(' ')
    logging.info(' STANDARDIZING INPUT DATA:')
    logging.info(' ')

    # PREPARE THE DATA FOR PREDICTION

    # get the subdirectories inside the parent folder
    subjects = [os.path.join(parent_folder, d) for d in os.listdir(parent_folder) if
                os.path.isdir(os.path.join(parent_folder, d))]
    # Remove the moose_dir path from the subjects list
    if moose_dir in subjects:
        subjects.remove(moose_dir)
    moose_compliant_subjects = input_validation.select_moose_compliant_subjects(subjects, modalities)
    file_utilities.organise_files_by_modality(moose_compliant_subjects, modalities, moose_dir)
    # Make the data nnUNet compatible
    spinner = Halo(text='Preparing data for prediction', spinner='dots')
    spinner.start()
    for input_dir in input_dirs:
        input_validation.make_nnunet_compatible(input_dir)
    spinner.succeed('Data ready for prediction')


    # RUN PREDICTION

    print('')
    print(' RUNNING PREDICTION:')
    print('')
    logging.info(' ')
    logging.info(' RUNNING PREDICTION:')
    logging.info(' ')
    # Run the segmentation on the standardized data and save the results in the output directory
    # Push back the results to their original locations


if __name__ == '__main__':
    main()
