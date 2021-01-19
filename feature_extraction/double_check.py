import os

from tqdm import tqdm

import f_conf


def double_check(wav_path: str, plp_scp_path: str, fbk_scp_path: str, plp_path: str, fbk_path: str):
    spkr_id_list = os.listdir(wav_path)
    for spkr_id in spkr_id_list:
        print('<<<<<<<<<<<<<<<<<< {} <<<<<<<<<<<<<<<<<<'.format(spkr_id))
        scp_file_name = '{}.scp'.format(spkr_id)
        plp_scp_file_path = os.path.join(plp_scp_path, scp_file_name)
        fbk_scp_file_path = os.path.join(fbk_scp_path, scp_file_name)

        plp_contents = []
        fbk_contents = []

        with open(plp_scp_file_path, 'r') as fin:
            plp_contents = fin.readlines()
        with open(fbk_scp_file_path, 'r') as fin:
            fbk_contents = fin.readlines()

        plp_paths_from_plp_scp = list(map(lambda x: x.split(' ')[1].strip(), plp_contents))
        plp_paths_from_fbk_scp = list(map(lambda x: x.split(' ')[0].strip(), fbk_contents))

        for plp, fbk in tqdm(zip(plp_paths_from_plp_scp, plp_paths_from_fbk_scp)):
            assert(plp == fbk)


if __name__ == "__main__":
    wav_path = os.path.join(f_conf.BASE_PATH, f_conf.WAV_PATH)
    plp_scp_path = os.path.join(f_conf.BASE_PATH, f_conf.PLP_SCP_PATH)
    fbk_scp_path = os.path.join(f_conf.BASE_PATH, f_conf.FBK_SCP_PATH)
    plp_path = os.path.join(f_conf.BASE_PATH, f_conf.PLP_PATH)
    fbk_path = os.path.join(f_conf.BASE_PATH, f_conf.FBK_PATH)

    double_check(
        wav_path=wav_path,
        plp_scp_path=plp_scp_path,
        fbk_scp_path=fbk_scp_path,
        plp_path=plp_path,
        fbk_path=fbk_path,
    )
