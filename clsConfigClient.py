################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 31-Mar-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal AI-driven voice assistant.    ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'MODEL_PATH': Curr_Path + sep + 'model' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'MODEL_DIR': 'model',
        'APP_DESC_1': 'PyCaret Training!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'Titanic.csv',
        'MODEL_NAME': 'PyCaret-ft-personal-2023-03-31-04-29-53',
        'TITLE': "PyCaret Training!",
        'PATH' : Curr_Path,
        'OUT_DIR': 'data'
    }
