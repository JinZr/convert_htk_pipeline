import os 
import threading
import argparse

# import f_conf
from funcs import *
from double_check import *
from add_time_fbk import *
from add_time_plp import *

import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--base_path', type=str, required=True)
parser.add_argument('--wav_path', type=str, required=True)
parser.add_argument('--feat_scp_path', type=str, required=True)
parser.add_argument('--feat_path', type=str, required=True)
parser.add_argument('--file_list_path', type=str, required=True)
parser.add_argument('--file_list_time_stamp_path', type=str, required=True)

parser.add_argument('--feature_type', type=str, required=True)

args = parser.parse_args()

if __name__ == "__main__":
    BASE_PATH = args.base_path
    WAV_PATH = args.wav_path
    FEAT_SCP_PATH = args.feat_scp_path
    FEAT_PATH = args.feat_path
    FILE_LIST_PATH = args.file_list_path
    FILE_LIST_TIME_STAMP_PATH = args.file_list_time_stamp_path

    FEATURE_TYPE = args.feature_type

    wav_path = os.path.join(BASE_PATH, WAV_PATH)
    feat_scp_path = os.path.join(BASE_PATH, FEAT_SCP_PATH)
    feat_path = os.path.join(BASE_PATH, FEAT_PATH)

    temp_file_list_path = os.path.join(BASE_PATH, FILE_LIST_PATH)
    file_list_with_time_stamp_path = os.path.join(BASE_PATH, FILE_LIST_TIME_STAMP_PATH)

    id_filelist_dict = file_list_for_all(wav_path=wav_path)
  
    for dir_name in id_filelist_dict.keys():
        print('<<<<<<<<<<<<<<<< {}.scp file <<<<<<<<<<<<<<<<'.format({dir_name}))
        generate_scp_file(
            wav_path=wav_path,
            feat_path=feat_path,
            spkr_id=dir_name,
            scp_path=feat_scp_path,
            scp_name='{}.scp'.format(dir_name),
            feature_type=FEATURE_TYPE,
            file_names=id_filelist_dict[dir_name],
            )

    feat_sub_dirs = os.listdir(feat_path)
    p = subprocess.Popen("./main.{}.sh".format(FEATURE_TYPE), shell=True, stdout=subprocess.PIPE)
    p.wait()
    print('<<<<<<<<<<<<<<<< main.{}.sh finished <<<<<<<<<<<<<<<<'.format(FEATURE_TYPE))
    
    if not os.path.exists(temp_file_list_path): os.makedirs(temp_file_list_path)
    if not os.path.exists(file_list_with_time_stamp_path): os.makedirs(file_list_with_time_stamp_path)
    for fbk_sub_dir in feat_sub_dirs:
        print('<<<<<<<<<<<<<<<< {} <<<<<<<<<<<<<<<<'.format({fbk_sub_dir}))
        fbk_file_path = os.path.join(fbk_path, fbk_sub_dir)
        fbk_file_list = os.listdir(fbk_file_path)
        fbk_file_list = list(map(lambda x: os.path.join(fbk_file_path, x + '\n'), fbk_file_list))

        file_list_path = os.path.join(temp_file_list_path, '{}.scp'.format(fbk_sub_dir))
        with open(file_list_path, 'w+') as fout:
            fout.writelines(fbk_file_list)
        
        add_time_stamp = add_time_stamp_fbk
        if FEATURE_TYPE == 'plp':  add_time_stamp = add_time_stamp_plp
        # elif FEATURE_TYPE == 'mfcc': add_time_stamp = add_time_stamp_mfcc

        thread = threading.Thread(
            target=add_time_stamp,
            args=(file_list_path, os.path.join(file_list_with_time_stamp_path, '{}.scp'.format(fbk_sub_dir)))
        )
        thread.start()


    # plp_scp_2_fbk_scp(
    #     plp_scp_path=plp_scp_path,
    #     fbk_scp_path=fbk_scp_path,
    #     fbk_path=fbk_path,
    # )

    # double_check(
    #     wav_path=wav_path,
    #     plp_scp_path=plp_scp_path,
    #     fbk_scp_path=fbk_scp_path,
    #     plp_path=plp_path,
    #     fbk_path=fbk_path,
    # )

        
    
    
