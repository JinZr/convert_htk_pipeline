SPKR_IDs=$(ls "${BASE_PATH}${WAV_PATH}")

BASE_PATH='/project_bdda4/bdda/zrjin/Tempo_Generated/'
ORIGINAL_FILE_LIST_PATH='/project/bdda/mengzhe/DataAugmentation/Data/UASpeech/UASpeech_trim/scp/train.orig.wav.scp' 
    # path to scp files
PROJECT_PATH=/project_bdda4/bdda/zrjin/convert_htk_pipeline/

# feature_extraction
WAV_PATH='WAVE/'
PLP_SCP_PATH='PLP_SCP/'
PLP_PATH='PLP/'
FBK_SCP_PATH='FBK_SCP/'
FBK_PATH='FBK/'
MFCC_SCP_PATH='MFCC_SCP/'
MFCC_PATH='MFCC/'

FILE_LIST_PATH='TEMP/'
FILE_LIST_TIME_STAMP_PATH='STMP/'

# single_pass_retraining
PAIRED_SCP_FILE=''
MLF_FILE=''
ORIGINAL_HMM_FILE=''
RETRAINED_HMM_PATH=''
HMM_LIST_FILE=''

# CMVN
CMVN_PATH=CMVN/
CMVN_CONFIG_PATH=${PROJECT_PATH}cmvn/cmvn.configs

# htk2kaldi
KALDI_PATH=KALDI/
PREPROCESS_PATH=${PROJECT_PATH}htk2kaldi/
CONFIG_PATH=${PREPROCESS_PATH}cfgs/
