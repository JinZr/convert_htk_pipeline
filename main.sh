source path.global.sh
source bool.global.sh

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
     cd ./fbank_or_plp
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --plp_scp_path=${PLP_SCP_PATH} \
        --fbk_scp_path=${FBK_SCP_PATH} \
        --fbk_path=${FBK_PATH} \ 
        --plp_path=${PLP_PATH} \
        --file_list_path=${FILE_LIST_PATH} \ 
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type='fbk'
     ./main.fbk.sh
     cd ..
fi

if [ '$PLP' = true ]; then
     cd ./fbank_or_plp
     python main.py \
        --base_path=${BASE_PATH} \
        --wav_path=${WAV_PATH} \
        --plp_scp_path=${PLP_SCP_PATH} \
        --fbk_scp_path=${FBK_SCP_PATH} \
        --fbk_path=${FBK_PATH} \ 
        --plp_path=${PLP_PATH} \
        --file_list_path=${FILE_LIST_PATH} \ 
        --file_list_time_stamp_path=${FILE_LIST_TIME_STAMP_PATH} \
        --feature_type='plp'
     ./main.plp.sh
     cd ..
fi
