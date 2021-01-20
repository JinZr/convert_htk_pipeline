#!/bin/bash

# credit: Mengzhe GENG

data_dir=$1
exp_dir=$2
out_feats_dir=$3
htk_feats=$4
scp=$5
job=$6
spkr_id=$7
cfgs_dir=$8
script_dir=$9


mkdir -p $htk_feats
mkdir -p $exp_dir $out_feats_dir
mkdir -p $data_dir/utt2spk
#out_feats_abs_dir=`perl -e '($data_dir,$pwd)= @ARGV; if($data_dir!~m:^/:) { $data_dir = "$pwd/$data_dir"; } print $data_dir; ' $out_feats_dir $PWD` # the absolute path of output HTK format plp dir
name=`basename $data_dir`

cat $scp | awk -v pwd=$PWD -v htkfeats=$htk_feats -F '=' '{print $0" "pwd"/"htkfeats"/"$1}' > $exp_dir/${name}_hcopy.scp
bash ${script_dir}helper_scripts/splitFile.sh $exp_dir/${name}_hcopy.scp $job
for i in `seq $job`; do
    HCopy -C ${cfgs_dir}/local.${spkr_id}.cfg -S $exp_dir/${name}_hcopy_sub$i.scp &
done
wait

cat $exp_dir/${name}_hcopy.scp | sed "s/.* \(.*\/\([^\/]*\).fbk\)/\2 \1/g" > $exp_dir/${name}_htk2kaldi.scp
bash ${script_dir}helper_scripts/splitFile.sh $exp_dir/${name}_htk2kaldi.scp $job
for i in `seq $job`; do
   copy-feats --compress=false --htk-in scp:$exp_dir/${name}_htk2kaldi_sub$i.scp ark,scp:$out_feats_dir/raw_fbk_${name}.$i.ark,$out_feats_dir/raw_fbk_${name}.$i.scp &
   #copy-feats --htk-in scp:$exp_dir/${name}_htk2kaldi_sub$i.scp ark,scp:$out_feats_dir/raw_fbk_${name}.$i.ark,$out_feats_dir/raw_fbk_${name}.$i.scp &
done
wait

for i in `seq $job`; do
    cat $out_feats_dir/raw_fbk_${name}.$i.scp
done | sort -u > $data_dir/feats.scp



