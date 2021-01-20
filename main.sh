source path.global.sh
source bool.global.sh
source flag.global.sh

echo '<<<<<<<<<<<<< begin <<<<<<<<<<<<<'

if [ $TEMPO_BOOL = true ]; then
   echo Implementing tempo stretch under folder ${PROJECT_PATH}tempo/
   cd ${PROJECT_PATH}tempo/
   python main.py \
      --show_warning=${SHOW_WARNING} \
      --scp_path=${ORIGINAL_FILE_LIST_PATH} \
      --tempo_path=${BASE_PATH}${WAV_PATH}
   cd ${PROJECT_PATH}
fi

if [ $FBK = true ]; then
     cd ${PROJECT_PATH}feature_extraction
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --feat_scp_path=${FBK_SCP_PATH} \
        --feat_path=${FBK_PATH} \
        --file_list_path=${FILE_LIST_PATH} \
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type=fbk
     cd ${PROJECT_PATH}
fi

if [ $PLP = true ]; then
     cd ${PROJECT_PATH}feature_extraction
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --feat_scp_path=${PLP_SCP_PATH} \
        --feat_path=${PLP_PATH} \
        --file_list_path=${FILE_LIST_PATH} \
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type=plp
     cd ${PROJECT_PATH}
fi

if [ $MFCC = true ]; then
     cd ${PROJECT_PATH}feature_extraction
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --feat_scp_path=${MFCC_SCP_PATH} \
        --feat_path=${MFCC_PATH} \
        --file_list_path=${FILE_LIST_PATH} \
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type=mfcc
     cd ${PROJECT_PATH}
fi


echo script finished, for cmvn and htk2kaldi, please use script under ./cmvn and ./htk2kaldi, resp.
