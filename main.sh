source path.global.sh
source bool.global.sh
source flag.global.sh

echo '<<<<<<<<<<<<< begin <<<<<<<<<<<<<'

if [ '$TEMPO_BOOL' = true ]; then
    cd ./tempo
    python main.py \
        --show_warning=${SHOW_WARNING} \
        --scp_path=${ORIGINAL_FILE_LIST_PATH} \
        --tempo_path=${BASE_PATH}
    cd ..
fi

if [ '$FBK' = true ]; then
     cd ./feature_extraction
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --feat_scp_path=${FBK_SCP_PATH} \
        --feat_path=${FBK_PATH} \
        --file_list_path=${FILE_LIST_PATH} \
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type=fbk
     cd ..
fi

if [ '$PLP' = true ]; then
     cd ./feature_extraction
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --feat_scp_path=${PLP_SCP_PATH} \
        --feat_path=${PLP_PATH} \
        --file_list_path=${FILE_LIST_PATH} \
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type=plp
     cd ..
fi

if [ '$MFCC' = true ]; then
     cd ./feature_extraction
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --feat_scp_path=${MFCC_SCP_PATH} \
        --feat_path=${MFCC_PATH} \
        --file_list_path=${FILE_LIST_PATH} \
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type=mfcc
     cd ..
fi


echo script finished, for 
