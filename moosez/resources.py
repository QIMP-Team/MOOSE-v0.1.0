#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import torch

# ----------------------------------------------------------------------------------------------------------------------
# Author: Lalith Kumar Shiyam Sundar
# Institution: Medical University of Vienna
# Research Group: Quantitative Imaging and Medical Physics (QIMP) Team
# Date: 13.02.2023
# Version: 2.0.0
#
# Description:
# This module contains the urls and filenames of the models and binaries that are required for the moosez.
#
# Usage:
# The variables in this module can be imported and used in other modules within the moosez to download the necessary
# binaries and models for the moosez.
#
# ----------------------------------------------------------------------------------------------------------------------

# This dictionary holds the pre-trained models available in MooseZ library.
# Each key is a unique model identifier following a specific syntax mentioned:
# 'clin' or 'preclin' (indicating Clinical or Preclinical),
# modality tag (like 'ct', 'pt', 'mr'), and then the tissue of interest.
# To make your model available, add its unique identifier to this list.
# Each value is a dictionary containing the following keys:
#    - url: The URL where the model files can be downloaded.
#    - filename: The filename of the model's zip file.
#    - directory: The directory where the model files will be extracted.
#    - trainer: The type of trainer used to train the model.
#    - voxel_spacing: The voxel spacing used in the model in the form [x, y, z], this is basically the median voxel
#    spacing generated by nnunetv2, and you can find this in the plans.json file of the model.
#    - multilabel_prefix: A prefix to distinguish between different types of labels in multi-label models.
#
# To include your own model, add a new entry to this dictionary following the above format.

MODELS = {
    "clin_ct_lungs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_lungs_24062023.zip",
        "filename": "Dataset333_HMS3dlungs.zip",
        "directory": "Dataset333_HMS3dlungs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Lungs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "lung_upper_lobe_left",
            2: "lung_lower_lobe_left",
            3: "lung_upper_lobe_right",
            4: "lung_middle_lobe_right",
            5: "lung_lower_lobe_right"
        },
        "limit_fov": None
    },
    "clin_ct_organs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_organs_05082024.zip",
        "filename": "Dataset123_Organs.zip",
        "directory": "Dataset123_Organs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Organs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "adrenal_gland_left",
            2: "adrenal_gland_right",
            3: "bladder",
            4: "brain",
            5: "gallbladder",
            6: "kidney_left",
            7: "kidney_right",
            8: "liver",
            9: "lung_lower_lobe_left",
            10: "lung_lower_lobe_right",
            11: "lung_middle_lobe_right",
            12: "lung_upper_lobe_left",
            13: "lung_upper_lobe_right",
            14: "pancreas",
            15: "spleen",
            16: "stomach",
            17: "thyroid_left",
            18: "thyroid_right",
            19: "trachea"
        },
        "limit_fov": None
    },
    "preclin_mr_all": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/preclin_mr_all_05122023.zip",
        "filename": "Dataset234_minimoose.zip",
        "directory": "Dataset234_minimoose",
        "trainer": "nnUNetTrainer",
        "voxel_spacing": [0.4000000059604645, 0.4000000059604645, 0.4000000059604645],
        "multilabel_prefix": "Preclin_MR_all_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "Brain",
            2: "Liver",
            3: "Intestines",
            4: "Pancreas",
            5: "Thyroid",
            6: "Spleen",
            7: "Bladder",
            8: "OuterKidney",
            9: "InnerKidney",
            10: "HeartInside",
            11: "HeartOutside",
            12: "WAT Subcutaneous",
            13: "WAT Visceral",
            14: "BAT",
            15: "Muscle TF",
            16: "Muscle TB",
            17: "Muscle BB",
            18: "Muscle BF",
            19: "Aorta",
            20: "Lung",
            21: "Stomach",
        },
        "limit_fov": None
    },
    "clin_ct_body": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_body_27112023.zip",
        "filename": "Dataset001_body.zip",
        "directory": "Dataset001_body",
        "trainer": "nnUNetTrainer",
        "voxel_spacing": [5, 5, 5],
        "multilabel_prefix": "CT_Body_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "Legs",
            2: "Body",
            3: "Head",
            4: "Arms"
        },
        "limit_fov": None
    },
    "clin_ct_ribs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_ribs_11082024.zip",
        "filename": "Dataset444_Ribs.zip",
        "directory": "Dataset444_Ribs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Ribs_",
        "configuration": "3d_fullres_big_patch",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "rib_left_1",
            2: "rib_left_2",
            3: "rib_left_3",
            4: "rib_left_4",
            5: "rib_left_5",
            6: "rib_left_6",
            7: "rib_left_7",
            8: "rib_left_8",
            9: "rib_left_9",
            10: "rib_left_10",
            11: "rib_left_11",
            12: "rib_left_12",
            13: "rib_left_13",
            14: "rib_right_1",
            15: "rib_right_2",
            16: "rib_right_3",
            17: "rib_right_4",
            18: "rib_right_5",
            19: "rib_right_6",
            20: "rib_right_7",
            21: "rib_right_8",
            22: "rib_right_9",
            23: "rib_right_10",
            24: "rib_right_11",
            25: "rib_right_12",
            26: "rib_right_13",
            27: "sternum"
        },
        "limit_fov": None
    },
    "clin_ct_muscles": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_muscles_09082024.zip",
        "filename": "Dataset555_Muscles.zip",
        "directory": "Dataset555_Muscles",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Muscles_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "autochthon_left",
            2: "autochthon_right",
            3: "gluteus_maximus_left",
            4: "gluteus_maximus_right",
            5: "gluteus_medius_left",
            6: "gluteus_medius_right",
            7: "gluteus_minimus_left",
            8: "gluteus_minimus_right",
            9: "iliopsoas_left",
            10: "iliopsoas_right"
        },
        "limit_fov": None
    },
    "clin_ct_peripheral_bones": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_peripheral_bones_05082024.zip",
        "filename": "Dataset666_Peripheral-Bones.zip",
        "directory": "Dataset666_Peripheral-Bones",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Peripheral-Bones_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "carpal_left",
            2: "carpal_right",
            3: "clavicle_left",
            4: "clavicle_right",
            5: "femur_left",
            6: "femur_right",
            7: "fibula_left",
            8: "fibula_right",
            9: "fingers_left",
            10: "fingers_right",
            11: "humerus_left",
            12: "humerus_right",
            13: "metacarpal_left",
            14: "metacarpal_right",
            15: "metatarsal_left",
            16: "metatarsal_right",
            17: "patella_left",
            18: "patella_right",
            19: "radius_left",
            20: "radius_right",
            21: "scapula_left",
            22: "scapula_right",
            23: "skull",
            24: "tarsal_left",
            25: "tarsal_right",
            26: "tibia_left",
            27: "tibia_right",
            28: "toes_left",
            29: "toes_right",
            30: "ulna_left",
            31: "ulna_right"
        },
        "limit_fov": None
    },
    "clin_ct_fat": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_fat_31082023.zip",
        "filename": "Dataset777_Fat.zip",
        "directory": "Dataset777_Fat",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Fat_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "spinal_chord",
            2: "skeletal_muscle",
            3: "subcutaneous_fat",
            4: "visceral_fat",
            5: "thoracic_fat",
            6: "eyes",
            7: "testicles",
            8: "prostate"
        },
        "limit_fov": None
    },
    "clin_ct_vertebrae": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_vertebrae_11082024.zip",
        "filename": "Dataset111_Vertebrae.zip",
        "directory": "Dataset111_Vertebrae",
        "trainer": "nnUNetTrainer_2000_epochs_DA5NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Vertebrae_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "vertebra_C1",
            2: "vertebra_C2",
            3: "vertebra_C3",
            4: "vertebra_C4",
            5: "vertebra_C5",
            6: "vertebra_C6",
            7: "vertebra_C7",
            8: "vertebra_T1",
            9: "vertebra_T2",
            10: "vertebra_T3",
            11: "vertebra_T4",
            12: "vertebra_T5",
            13: "vertebra_T6",
            14: "vertebra_T7",
            15: "vertebra_T8",
            16: "vertebra_T9",
            17: "vertebra_T10",
            18: "vertebra_T11",
            19: "vertebra_T12",
            20: "vertebra_L1",
            21: "vertebra_L2",
            22: "vertebra_L3",
            23: "vertebra_L4",
            24: "vertebra_L5",
            25: "vertebra_L6",
            26: "hip_left",
            27: "hip_right",
            28: "sacrum"
        },
        "limit_fov": None
    },
    "clin_ct_cardiac": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_cardiac_09082024.zip",
        "filename": "Dataset888_Cardiac.zip",
        "directory": "Dataset888_Cardiac",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Cardiac_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "heart_myocardium",
            2: "heart_atrium_left",
            3: "heart_atrium_right",
            4: "heart_ventricle_left",
            5: "heart_ventricle_right",
            6: "aorta",
            7: "iliac_artery_left",
            8: "iliac_artery_right",
            9: "iliac_vena_left",
            10: "iliac_vena_right",
            11: "inferior_vena_cava",
            12: "portal_splenic_vein",
            13: "pulmonary_artery"
        },
        "limit_fov": None
    },
    "clin_ct_digestive": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_digestive_10092023.zip",
        "filename": "Dataset999_Digestive.zip",
        "directory": "Dataset999_Digestive",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Digestive_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "esophagus",
            2: "trachea",
            3: "small_bowel",
            4: "duodenum",
            5: "colon",
            6: "urinary_bladder",
            7: "face"
        },
        "limit_fov": None
    },
    "preclin_ct_legs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/preclin_ct_legs_05122023.zip",
        "filename": "Dataset256_Preclin_leg_muscles.zip",
        "directory": "Dataset256_Preclin_leg_muscles",
        "trainer": "nnUNetTrainerNoMirroring",
        "voxel_spacing": [0.18000000715255737, 0.18000000715255737, 0.18000000715255737],
        "multilabel_prefix": "Preclin_CT_legs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "right_leg_muscle",
            2: "left_leg_muscle"
        },
        "limit_fov": None
    },
    "clin_ct_all_bones_v1": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_all_bones_25102023.zip",
        "filename": "Dataset600_Original_bones.zip",
        "directory": "Dataset600_Original_bones",
        "trainer": "nnUNetTrainer_2000epochs",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_all_bones_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "carpal",
            2: "clavicle",
            3: "femur",
            4: "fibula",
            5: "humerus",
            6: "metacarpal",
            7: "metatarsal",
            8: "patella",
            9: "pelvis",
            10: "fingers",
            11: "radius",
            12: "ribcage",
            13: "scapula",
            14: "skull",
            15: "spine",
            16: "sternum",
            17: "tarsal",
            18: "tibia",
            19: "toes",
            20: "ulna"
        },
        "limit_fov": None
    },
    "clin_ct_PUMA": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_PUMA_1k_23052024.zip",
        "filename": "Dataset002_PUMA.zip",
        "directory": "Dataset002_PUMA",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_PUMA_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            0: "background",
            1: "Spleen",
            2: "Kidneys",
            3: "Gallbladder",
            4: "Liver",
            5: "Stomach",
            6: "Pancreas",
            7: "Adrenal_glands",
            8: "Lungs",
            9: "Heart_myocardium",
            10: "Heart_atrium_left",
            11: "Heart_ventricle_left",
            12: "Heart_atrium_right",
            13: "Heart_ventricle_right",
            14: "Pulmonary_artery",
            15: "Aorta",
            16: "Inferior_vena_cava",
            17: "Esophagus",
            18: "Trachea",
            19: "Digestive",
            20: "Brain",
            21: "Skeleton",
            22: "Muscles",
            23: "Bladder"
        },
        "limit_fov": None
    },
    "clin_pt_fdg_brain_v1": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_fdg_pt_brain_v1_17112023.zip",
        "filename": "Dataset100_Brain_v1.zip",
        "directory": "Dataset100_Brain_v1",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [2.03125, 2.0862598419189453, 2.0862600803375244],
        "multilabel_prefix": "Clin_PT_FDG_brain_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            0: "background",
            1: "R-Hippocampus",
            2: "L-Hippocampus",
            3: "R-Amygdala",
            4: "L-Amygdala",
            5: "R-Anterior-temporal-lobe-medial-part",
            6: "L-Anterior-temporal-lobe-medial-part",
            7: "R-Anterior-temporal-lobe-lateral-part",
            8: "L-Anterior-temporal-lobe-lateral-part",
            9: "R-Parahippocampal-and-ambient-gyri",
            10: "L-Parahippocampal-and-ambient-gyri",
            11: "R-Superior-temporal-gyrus-posterior-part",
            12: "L-Superior-temporal-gyrus-posterior-part",
            13: "R-Middle and inferior temporal gyrus",
            14: "L-Middle and inferior temporal gyrus",
            15: "R-Fusiform gyrus",
            16: "L-Fusiform gyrus",
            17: "R-Cerebellum",
            18: "L-Cerebellum",
            19: "Brainstem",
            20: "L-Insula",
            21: "R-Insula",
            22: "L-Lateral remainder of occipital lobe",
            23: "R-Lateral remainder of occipital lobe",
            24: "L-Cingulate gyrus gyrus cinguli anterior part",
            25: "R-Cingulate gyrus gyrus cinguli anterior part",
            26: "L-Cingulate gyrus gyrus cinguli posterior part",
            27: "R-Cingulate gyrus gyrus cinguli posterior part",
            28: "L-Middle frontal gyrus",
            29: "R-Middle frontal gyrus",
            30: "L-Posterior temporal lobe",
            31: "R-Posterior temporal lobe",
            32: "L-Inferiolateral remainder of parietal lobe",
            33: "R-Inferiolateral remainder of parietal lobe",
            34: "L-Caudate nucleus",
            35: "R-Caudate nucleus",
            36: "L-Nucleus accumbens",
            37: "R-Nucleus accumbens",
            38: "L-Putamen",
            39: "R-Putamen",
            40: "L-Thalamus",
            41: "R-Thalamus",
            42: "L-Pallidum",
            43: "R-Pallidum",
            44: "Corpus callosum",
            45: "R-Lateral ventricle excluding temporal horn",
            46: "L-Lateral ventricle excluding temporal horn",
            47: "R-Lateral ventricle, temporal horn",
            48: "L-Lateral ventricle, temporal horn",
            49: "Third ventricle",
            50: "L-Precentral gyrus",
            51: "R-Precentral gyrus",
            52: "L-Straight gyrus",
            53: "R-Straight gyrus",
            54: "L-Anterior orbital gyrus",
            55: "R-Anterior orbital gyrus",
            56: "L-Inferior frontal gyrus",
            57: "R-Inferior frontal gyrus",
            58: "L-Superior frontal gyrus",
            59: "R-Superior frontal gyrus",
            60: "L-Postcentral gyrus",
            61: "R-Postcentral gyrus",
            62: "L-Superior parietal gyrus",
            63: "R-Superior parietal gyrus",
            64: "L-Lingual gyrus",
            65: "R-Lingual gyrus",
            66: "L-Cuneus",
            67: "R-Cuneus",
            68: "L-Medial orbital gyrus",
            69: "R-Medial orbital gyrus",
            70: "L-Lateral orbital gyrus",
            71: "R-Lateral orbital gyrus",
            72: "L-Posterior orbital gyrus",
            73: "R-Posterior orbital gyrus",
            74: "L-Substantia nigra",
            75: "R-Substantia nigra",
            76: "L-Subgenual frontal cortex",
            77: "R-Subgenual frontal cortex",
            78: "L-Subcallosal area",
            79: "R-Subcallosal area",
            80: "L-Pre-subgenual frontal cortex",
            81: "R-Pre-subgenual frontal cortex",
            82: "L-Superior temporal gyrus anterior part",
            83: "R-Superior temporal gyrus anterior part"
        },
        "limit_fov": None
    },
    "clin_ct_ALPACA": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_ALPACA.zip",
        "filename": "Dataset080_Alpaca.zip",
        "directory": "Dataset080_Alpaca",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_ALPACA_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "heart_ventricle_left",
            2: "heart_ventricle_right",
            3: "pulmonary_artery",
            4: "iliac_artery_left",
            5: "iliac_artery_right",
            6: "aorta"
        },
        "limit_fov": None
    },
    "clin_ct_PUMA4": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_PUMA4_06032024.zip",
        "filename": "Dataset003_PUMA4.zip",
        "directory": "Dataset003_PUMA4",
        "trainer": "nnUNetTrainer_2000epochs",
        "voxel_spacing": [4, 4, 4],
        "multilabel_prefix": "Clin_CT_PUMA4_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            0: "background",
            1: "Spleen",
            2: "Kidneys",
            3: "Gallbladder",
            4: "Liver",
            5: "Stomach",
            6: "Pancreas",
            7: "Adrenal Glands",
            8: "Lungs",
            9: "Heart",
            10: "Vessels",
            11: "Esophagus",
            12: "Trachea",
            13: "Digestive",
            14: "Brain",
            15: "Skeleton",
            16: "Muscles",
            17: "Bladder",
            18: "Filler"
        },
        "limit_fov": None
    },
    "clin_ct_liver_segments": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_liver_segments_10092024.zip",
        "filename": "Dataset134_Couinaud.zip",
        "directory": "Dataset134_Couinaud",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_liver_segments_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "segment_I",
            2: "segment_II",
            3: "segment_III",
            4: "segment_IV",
            5: "segment_V",
            6: "segment_VI",
            7: "segment_VII",
            8: "segment_VIII"
        },
        "limit_fov": {
            "model_to_crop_from": "clin_ct_fast_organs",
            "inference_fov_intensities": 8,
            "label_intensity_to_crop_from": 8,
            "largest_component_only": False
        }
    },
    "clin_ct_fast_organs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_organs_6_02092024.zip",
        "filename": "Dataset145_Fast_organs.zip",
        "directory": "Dataset145_Fast_organs",
        "trainer": "nnUNetTrainer_2000epochs",
        "voxel_spacing": [6, 6, 6],
        "multilabel_prefix": "Clin_CT_fast_organs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "adrenal_gland_left",
            2: "adrenal_gland_right",
            3: "bladder",
            4: "brain",
            5: "gallbladder",
            6: "kidney_left",
            7: "kidney_right",
            8: "liver",
            9: "lung_lower_lobe_left",
            10: "lung_lower_lobe_right",
            11: "lung_middle_lobe_right",
            12: "lung_upper_lobe_left",
            13: "lung_upper_lobe_right",
            14: "pancreas",
            15: "spleen",
            16: "stomach",
            17: "thyroid_left",
            18: "thyroid_right",
            19: "trachea"
        },
        "limit_fov": None
    },
    "clin_ct_aorta": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_aorta_02092024.zip",
        "filename": "Dataset321_Aorta.zip",
        "directory": "Dataset321_Aorta",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_aorta_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "zone_0",
            2: "innominate",
            3: "zone_1",
            4: "left_common_carotid",
            5: "zone_2",
            6: "left_subclavian_artery",
            7: "zone_3",
            8: "zone_4",
            9: "zone_5",
            10: "zone_6",
            11: "celiac_artery",
            12: "zone_7",
            13: "sma",
            14: "zone_8",
            15: "right_renal_artery",
            16: "left_renal_artery",
            17: "zone_9",
            18: "right_common_iliac_artery",
            19: "left_common_iliac_artery",
            20: "right_internal_iliac_artery",
            21: "left_internal_iliac_artery",
            22: "right_external_iliac_artery",
            23: "left_external_iliac_artery"
        },
        "limit_fov": {
            "model_to_crop_from": "clin_ct_fast_cardiac",
            "inference_fov_intensities": 6,
            "label_intensity_to_crop_from": 6,
            "largest_component_only": False
        }
    },
    "clin_pt_fdg_tumor": {
        "organ_indices": {
            1: "tumor"
        },
        "limit_fov": None
    },
    "clin_ct_body_composition": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_body_composition_05092024.zip",
        "filename": "Dataset778_Body_composition.zip",
        "directory": "Dataset778_Body_composition",
        "trainer": "nnUNetTrainer_2000epochs",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_body_composition_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
                1: "skeletal_muscle",
                2: "subcutaneous_fat",
                3: "visceral_fat"
        },
        "limit_fov": {
            "model_to_crop_from": "clin_ct_fast_vertebrae",
            "inference_fov_intensities": [20, 24],
            "label_intensity_to_crop_from": 22,
            "largest_component_only": True
        }
    },
    "clin_ct_fast_vertebrae": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_vertebrae3_10092024.zip",
        "filename": "Dataset112_FastVertebrae.zip",
        "directory": "Dataset112_FastVertebrae",
        "trainer": "nnUNetTrainer_2000_epochs_DA5NoMirroring",
        "voxel_spacing": [3, 3, 3],
        "multilabel_prefix": "Clin_CT_fast_vertebrae_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "vertebra_C1",
            2: "vertebra_C2",
            3: "vertebra_C3",
            4: "vertebra_C4",
            5: "vertebra_C5",
            6: "vertebra_C6",
            7: "vertebra_C7",
            8: "vertebra_T1",
            9: "vertebra_T2",
            10: "vertebra_T3",
            11: "vertebra_T4",
            12: "vertebra_T5",
            13: "vertebra_T6",
            14: "vertebra_T7",
            15: "vertebra_T8",
            16: "vertebra_T9",
            17: "vertebra_T10",
            18: "vertebra_T11",
            19: "vertebra_T12",
            20: "vertebra_L1",
            21: "vertebra_L2",
            22: "vertebra_L3",
            23: "vertebra_L4",
            24: "vertebra_L5",
            25: "vertebra_L6",
            26: "hip_left",
            27: "hip_right",
            28: "sacrum"
            },
        "limit_fov": None
        },
    "clin_ct_fast_cardiac": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_cardiac3_10092024.zip",
        "filename": "Dataset890_FastCardiac.zip",
        "directory": "Dataset890_FastCardiac",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [3, 3, 3],
        "multilabel_prefix": "CT_Fast_Cardiac_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans",
        "organ_indices": {
            1: "heart_myocardium",
            2: "heart_atrium_left",
            3: "heart_atrium_right",
            4: "heart_ventricle_left",
            5: "heart_ventricle_right",
            6: "aorta",
            7: "iliac_artery_left",
            8: "iliac_artery_right",
            9: "iliac_vena_left",
            10: "iliac_vena_right",
            11: "inferior_vena_cava",
            12: "portal_splenic_vein",
            13: "pulmonary_artery"
        },
        "limit_fov": None
    }


    # More dictionaries for other models...
}

AVAILABLE_MODELS = MODELS.keys()


# This function returns a dictionary indicating the expected modality for a given model_name, the imaging technique,
# the type of tissue to be segmented. The model_name should be the same as the unique identifier mentioned in the
# MODELS dictionary above and the AVAILABLE_MODELS list.
# If the model_name is not found, it logs an error message and returns an error message.
#
# If you add your own model, update this function to return the expected modality dictionary for your model.

def expected_modality(model_name: str) -> dict:
    """
    Display expected modality for the model.
    :param model_name: The name of the model.
    :return: The expected modality for the model.
    """
    models = {
        "clin_ct_lungs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Lungs"},
        "clin_ct_organs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Organs"},
        "clin_ct_body": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Body, Arms, legs, head"},
        "preclin_mr_all": {"Imaging": "Pre-clinical", "Modality": "MR", "Tissue of interest": "All regions"},
        "clin_ct_ribs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Ribs"},
        "clin_ct_muscles": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Muscles"},
        "clin_ct_peripheral_bones": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Peripheral Bones"},
        "clin_ct_fat": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Fat"},
        "clin_ct_vertebrae": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Vertebrae"},
        "clin_ct_cardiac": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Cardiac"},
        "clin_ct_digestive": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Digestive"},
        "preclin_ct_legs": {"Imaging": "Pre-clinical", "Modality": "CT", "Tissue of interest": "Legs"},
        "clin_ct_all_bones_v1": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "All bones"},
        "clin_ct_PUMA": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "PUMA tissues"},
        "clin_pt_fdg_brain_v1": {"Imaging": "Clinical", "Modality": "PT", "Tissue of interest": "Brain regions"},
        "clin_ct_ALPACA": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "ALPACA tissues"},
        "clin_ct_PUMA4": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "PUMA tissues"},
        "clin_ct_liver_segments": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Liver segments"},
        "clin_ct_fast_organs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Organs"},
        "clin_ct_aorta": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Aorta segments"},
        "clin_ct_body_composition": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Body composition on the L3 vertebra region"}
    }

    if model_name in models:
        model = models[model_name]
        model["Model name"] = model_name
        return model

    logging.error(" Requested model is not available. Please check the model name.")
    return {"Error": "Requested model is not available. Please check the model name."}


# This function maps the model name to the task number. This is the number that comes after Dataset in DatasetXXXX,
# after nnunetv2 training. If your model folder is Dataset123, then the task number is 123.
# It checks for known model names and returns the associated task number, this is ABSOLUTELY NEEDED for the moosez to
# work. If the provided model name doesn't match any known model, it raises an exception.


def check_device() -> str:
    """
    This function checks the available device for running predictions, considering CUDA and MPS (for Apple Silicon).

    Returns:
        str: The device to run predictions on, either "cpu", "cuda", or "mps".
    """
    # Check for CUDA
    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        print(f" CUDA is available with {device_count} GPU(s). Predictions will be run on GPU.")
        return "cuda"
    # Check for MPS (Apple Silicon) Here for the future but not compatible right now
    elif torch.backends.mps.is_available():
        print(" Apple MPS backend is available. Predictions will be run on Apple Silicon GPU.")
        return "mps"
    elif not torch.backends.mps.is_built():
        print(" MPS not available because the current PyTorch install was not built with MPS enabled.")
        return "cpu"
    else:
        print(" CUDA/MPS not available. Predictions will be run on CPU.")
        return "cpu"
