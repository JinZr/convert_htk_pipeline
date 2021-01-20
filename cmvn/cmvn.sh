#!/bin/bash

# credit: Mengzhe GENG

for spk in ${SPKR_IDs}; do
    echo "<<<<<<<<<<<<<<<<<< processing: ${spk} <<<<<<<<<<<<<<<<<<"

    mkdir -p ${BASE_PATH}${CMVN_PATH}${spk}
    cp -r ${CMVN_CONFIG_PATH}/{base,CMDs,htefiles,lib,local-dnn,xwrd.clustered.mlist} ${BASE_PATH}${CMVN_PATH}${spk}/
    cd ${BASE_PATH}${CMVN_PATH}${spk}/lib

    rm -rf flists
    mkdir flists

    ln -s ${BASE_PATH}${FILE_LIST_TIME_STAMP_PATH}${spk}.scp flists/train.scp
    cp flists/train.scp flists/train.sort.scp

    cd ${BASE_PATH}${CMVN_PATH}${spk}
    mkdir -p tasks/cmn
    mkdir -p tasks/cvn
    local-dnn/nbin/HCompV  -p '%%%%%%*' -k '%%%%%%-?????%%%%%%%%%%%%%%%%???_*'  -A -D -V -T 1 -C lib/cfgs/cmn.cfg  -c tasks/cmn -S lib/flists/train.scp
    local-dnn/nbin/HCompV  -p '%%%%%%*' -k '%%%%%%-?????%%%%%%%%%%%%%%%%???_*' -A -D -V -T 1 -C lib/cfgs/cvn.cfg -q v -c tasks/cvn  -S lib/flists/train.scp
done
