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

