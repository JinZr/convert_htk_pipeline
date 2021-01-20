# BASE_PATH=/project_bdda3/bdda/zrjin/Tempo_Generated/
# CMVN_PATH=CMVN/
# FILE_LIST_TIME_STAMP_PATH=STMP/
# KALDI_PATH=KALDI/

# PREPROCESS_PATH=/project_bdda3/bdda/zrjin/DA-AL/preprocess/
# CONFIG_PATH=/project_bdda3/bdda/zrjin/DA-AL/preprocess/cfgs/

# readonly BASE_PATH CMVN_PATH FILE_LIST_TIME_STAMP_PATH KALDI_PATH CONFIG_PATH PREPROCESS_PATH

# echo ${BASE_PATH}

# SPKR_IDs=(XXF02 XXF03 XXF04 XXF05 XXM01 XXM04 XXM05 XXM06 XXM07 XXM08 XXM09 XXM10 XXM11 XXM12 XXM14 XXM16)
# readonly SPKR_IDs

# echo ${#SPKR_IDs[@]}

cd ${BASE_PATH}${KALDI_PATH}

# source ${PREPROCESS_PATH}path.sh

# link the tasks
for spkr_id in ${SPKR_IDs}; do
	echo $spkr_id
    ln -s  ${BASE_PATH}${CMVN_PATH}${spkr_id}/tasks ${spkr_id}.tasks
done


# create and change the cfgs
cd ${CONFIG_PATH}

for spkr_id in ${SPKR_IDs}; do
	echo create and change the cfgs ${spkr_id}
    touch local.${spkr_id}.cfg
    sed "s/tasks/${spkr_id}.tasks/g" local.original.cfg > local.${spkr_id}.cfg
done

# link the scp files
cd ${BASE_PATH}${KALDI_PATH}
mkdir -p ${BASE_PATH}${KALDI_PATH}scp/

for spkr_id in ${SPKR_IDs}; do
	echo link scp files ${spkr_id}
    mkdir -p ${BASE_PATH}${KALDI_PATH}scp/${spkr_id}
    ln -s  ${BASE_PATH}${FILE_LIST_TIME_STAMP_PATH}${spkr_id}.scp ${BASE_PATH}${KALDI_PATH}scp/${spkr_id}/${spkr_id}.scp
done


# make data directory
mkdir -p ${BASE_PATH}${KALDI_PATH}data/
cd ${BASE_PATH}${KALDI_PATH}data/

for spkr_id in ${SPKR_IDs}; do
	echo mkdir for ${spkr_id}
    mkdir -p ${spkr_id}
done


# run the generate_kaldi_script
cd ${BASE_PATH}${KALDI_PATH}
mkdir -p feats
mkdir -p exp


for spkr_id in ${SPKR_IDs}; do
	echo convert feature for ${spkr_id}
    mkdir -p feats/${spkr_id}
    bash ${PREPROCESS_PATH}get_kaldi_fbk_data_from_htk.sh\
        ${BASE_PATH}${KALDI_PATH}data/${spkr_id}\
        ${BASE_PATH}${KALDI_PATH}exp/${spkr_id}\
        ${BASE_PATH}${KALDI_PATH}feats/${spkr_id}\
        out/${spkr_id}\
        ${BASE_PATH}${KALDI_PATH}scp/${spkr_id}/${spkr_id}.scp\
        40\
        ${spkr_id}\
    	${CONFIG_PATH}\
        ${PREPROCESS_PATH}
done


