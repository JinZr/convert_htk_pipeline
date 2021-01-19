spkr_ids=$(ls "${BASE_PATH}${WAV_PATH}")

for id in ${spkr_ids}; do
    if [ ! -d "${BASE_PATH}${PLP_PATH}${id}" ]; then
        mkdir "${BASE_PATH}${PLP_PATH}${id}"
    fi
    scp_file_path="${BASE_PATH}${PLP_SCP_PATH}${id}.scp"
    HCopy -T 7 -S ${scp_file_path} -A -D -V -C "./configs/plp.cfg"
done    
  
