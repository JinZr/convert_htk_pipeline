import os
from tqdm import tqdm
import f_conf

def generate_scp_file(
    wav_path: str, feat_path: str, spkr_id: str, scp_path: str, scp_name: str, feature_type: str, file_names: [str]
    ):
    if not os.path.exists(scp_path): os.makedirs(scp_path)
    with open(os.path.join(scp_path, scp_name), 'w+') as fout:
        file_names_with_return = map(
            lambda x: __generate_paired_wav_path__(os.path.join(wav_path, spkr_id), x)\
                + ' '\
                + __generate_paired_fbank_path__(os.path.join(feat_path, spkr_id), x, feature_type) + '\n', 
            file_names
        )
        fout.writelines(file_names_with_return)

def plp_scp_2_fbk_scp(plp_scp_path: str, fbk_scp_path: str, fbk_path: str):
    if not os.path.exists(fbk_scp_path): os.makedirs(fbk_scp_path)
    plp_scp_file_list = os.listdir(plp_scp_path)
    for plp_scp_file in plp_scp_file_list:
        with open(os.path.join(plp_scp_path, plp_scp_file), 'r') as fin:
            plp_path_list = list(map(lambda x: x.strip().split(' ')[1], fin.readlines()))
            plp_file_list = list(map(lambda x: '/'.join(x.split('/')[-2:]), plp_path_list))
            plp_file_name_list = list(map(lambda x: x.split('.')[0], plp_file_list))
            fbk_path_list = list(map(lambda x: os.path.join(fbk_path, x + '.fbk'), plp_file_name_list))

            spkr_id = plp_scp_file.split('.')[0]

            print('<<<<<<<<<<<<<<<< {} <<<<<<<<<<<<<<<<<'.format(spkr_id))

            with open(os.path.join(fbk_scp_path, '{}.scp'.format(spkr_id)), 'w+') as fout:
                for plp, fbk in tqdm(zip(plp_path_list, fbk_path_list)):
                    fout.writelines(['{} {}\n'.format(plp, fbk)])


def __generate_paired_wav_path__(spkr_wav_path: str, wav_file_name: str) -> str:
    return os.path.join(spkr_wav_path, wav_file_name)

def __generate_paired_fbank_path__(spkr_fbank_path: str, wav_file_name: str, feature_type: str) -> str:
    fbank_name = '_'.join(wav_file_name.split('_')[0:2])
    scp_name = '{}.{}'.format(fbank_name, feature_type)
    return os.path.join(spkr_fbank_path, scp_name)


def file_list_for_all(wav_path: str) -> dict:
    dirs = os.listdir(wav_path)
    result = dict()
    for d in dirs:
        result[d] = __file_list_for_spkr__(
            wav_path=wav_path, 
            spkr_id=d
        )
    return result
    

def __file_list_for_spkr__(wav_path: str, spkr_id: str) -> [str]:
    return os.listdir(
        os.path.join(wav_path, spkr_id)
    )

