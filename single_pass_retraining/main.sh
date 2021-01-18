# DOCs: Single-pass retraining is enabled in HERest by setting
# the -r switch. This causes the input training files to be 
# read in pairs. The first of each pair is used to compute the
# forward/backward probabilities and the second is used to 
# estimate the parameters for the new models. Very often, of
# course, data input to HTK is modified by the HParm module 
# in accordance with parameters set in a configuration file. 
# In single-pass retraining mode, configuration parameters can
# be prefixed by the pseudo-module names HPARM1 and HPARM2. 
# Then when reading in the first file of each pair, only 
# the HPARM1 parameters are used and when reading the second 
# file of each pair, only the HPARM2 parameters are used.

HERest -r -C retrain.cfg\
    -S ${PAIRED_SCP_FILE}\ # "some scp files"
    -I ${MLF_FILE}\ # "master label file mlf"
    -H ${ORIGINAL_HMM_FILE}\ # "original HMM model"
    -M ${RETRAINED_HMM_PATH}\ # "dir to save retrained HMM Model"
    ${HMM_LIST_FILE} # "HMM structure"