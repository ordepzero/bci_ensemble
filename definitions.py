# -*- coding: utf-8 -*-

import os

SIGNAL_FILE_A = "../../bases/data_set_2/subject_A/Subject_A_Train_Signal.txt"
SIGNAL_FILE_B = "../../bases/data_set_2/subject_B/Subject_B_Train_Signal.txt"
STIMULUS_FILE_A = "../../bases/data_set_2/subject_A/Subject_A_Train_StimulusType.txt"
STIMULUS_FILE_B = "../../bases/data_set_2/subject_B/Subject_B_Train_StimulusType.txt"
STIMULUS_CODE_A = "../../bases/data_set_2/subject_A/Subject_A_Train_StimulusCode.txt"
STIMULUS_CODE_B = "../../bases/data_set_2/subject_B/Subject_B_Train_StimulusCode.txt"


SIGNAL_TESTFILE_A = "../../bases/data_set_2/subject_A/Subject_A_Test_Signal.txt"
SIGNAL_TESTFILE_B = "../../bases/data_set_2/subject_B/Subject_B_Test_Signal.txt"
STIMULUS_TESTCODE_A = "../../bases/data_set_2/subject_A/Subject_A_Test_StimulusCode.txt"
STIMULUS_TESTCODE_B = "../../bases/data_set_2/subject_B/Subject_B_Test_StimulusCode.txt"


DIRECTORY_BASE = "../../enhanced_bases"
DIRECTORY_SIGNALS_CHANNELS = DIRECTORY_BASE+"/signals_channels"
DIRECTORY_SIGNALS_CHANNELS_A = DIRECTORY_SIGNALS_CHANNELS+"/signals_channels_A"
DIRECTORY_SIGNALS_CHANNELS_B = DIRECTORY_SIGNALS_CHANNELS+"/signals_channels_B"
DIRECTORY_IMAGES = DIRECTORY_BASE+"/images"


def create_directories():
    
    if not os.path.exists(DIRECTORY_BASE):
        os.makedirs(DIRECTORY_BASE)
    
    if not os.path.exists(DIRECTORY_SIGNALS_CHANNELS):
        os.makedirs(DIRECTORY_SIGNALS_CHANNELS)
    
    if not os.path.exists(DIRECTORY_SIGNALS_CHANNELS_A):
        os.makedirs(DIRECTORY_SIGNALS_CHANNELS_A)
    
    if not os.path.exists(DIRECTORY_SIGNALS_CHANNELS_B):
        os.makedirs(DIRECTORY_SIGNALS_CHANNELS_B)