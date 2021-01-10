import os

import sox
from tqdm import tqdm
from scipy.io import wavfile
import threading

def parse_scp_and_tempo(scp_path: str, tempo_path: str):
    """
    parse scp file
    """
    with open(scp_path, 'r') as scp_file:
        file_lines = scp_file.readlines()
        wav_folder = '/'.join(file_lines[0].split('/')[:-1]) + '/'
        file_names = list(map(lambda x: x.split('/')[-1].strip(), file_lines))
        dys_file_names = __get_dysarthric_spkr__(file_names)
        ctrl_file_names = __get_control_spkr__(file_names)

        grouped_dys_file_names = __group_by_spkr__(dys_file_names)

        # if t_conf.DEBUG:
        #     print(wav_folder)
        #     print(file_names[0])
        #     print(dys_file_names[1])
        #     print(ctrl_file_names[1])
        #     print(grouped_dys_file_names.keys())
        #     quit()

        print(
            '''
            file name count: {}
            dysarthric file count: {}
            control file count: {}
            dysarthric speaker count: {}
            '''.format(len(file_names), len(dys_file_names), len(ctrl_file_names), len(grouped_dys_file_names.keys()))
        )

        # checkpoint
        # checkpoint_spkr = ''
        # with open(t_conf.CHECKPOINT, 'w+') as checkpoint:
        #     checkpoint_spkr = checkpoint.readline().strip()
        #     print('<<<<<<<<<<<<<< checkpoint spkr: {} <<<<<<<<<<<<<<'.format(checkpoint_spkr))

        for dys_spkr in grouped_dys_file_names.keys():

            # if checkpoint_spkr != "" and checkpoint_spkr != dys_spkr: continue

            thread = threading.Thread(target=tempo_selected_spkr, args=(dys_spkr, tempo_path, grouped_dys_file_names, ctrl_file_names, wav_folder))
            thread.start()
            # tempo_selected_spkr(dys_spkr, tempo_path, grouped_dys_file_names, ctrl_file_names, wav_folder)

            # checkpoint_spkr = dys_spkr
            # with open(t_conf.CHECKPOINT, 'w+') as checkpoint:
            #     checkpoint.write(checkpoint_spkr)

def tempo_selected_spkr(dys_spkr, tempo_path, grouped_dys_file_names, ctrl_file_names, wav_folder):
    print('<<<<<<<<<<<<<< {} <<<<<<<<<<<<<<'.format(dys_spkr))
    if not os.path.exists(os.path.join(tempo_path, dys_spkr)): 
        os.makedirs(os.path.join(tempo_path, dys_spkr))
    dys_spkr_file_names = grouped_dys_file_names[dys_spkr]
    for f_name in tqdm(dys_spkr_file_names):
        word_and_microphone_index = f_name.split('-')[4].split('_')[1]
        matched_ctrl_file_names = list(filter(
            lambda x: x.split('-')[4].split('_')[1] == word_and_microphone_index, 
            ctrl_file_names))
        dys_file_path = os.path.join(wav_folder, f_name)
        _, dys_waveform = wavfile.read(dys_file_path)
        dys_length = len(dys_waveform)
        for matched_file_name in matched_ctrl_file_names:
            ctrl_file_path = os.path.join(wav_folder, matched_file_name)
            _, ctrl_waveform = wavfile.read(ctrl_file_path)
            __tempo_wav__(
                src_file_path=ctrl_file_path,
                tgt_file_path=os.path.join(tempo_path, dys_spkr, matched_file_name),
                ratio=len(ctrl_waveform) / dys_length
                )


def __tempo_wav__(src_file_path: str, tgt_file_path: str, ratio: float):
    """
    src_file_path: str source wav file path
    tgt_file_path: str path to store the tempo stretched wav file
    ratio: float parameter for tempo 
    """
    transformer = sox.transform.Transformer()
    transformer.tempo(factor=ratio, audio_type='s')
    transformer.build(
        input_filepath=src_file_path, 
        output_filepath=tgt_file_path, 
        sample_rate_in=16000)


def __get_dysarthric_spkr__(file_names: [str]) -> [str]:
    """
    file_names: [str] All file names

    return: 
        file names of all dysarthric spkrs
    """
    return list(filter(
        lambda x: x.split('-')[1][0:2] == 'XX',
        file_names
    ))

def __get_control_spkr__(file_names: [str]) -> [str]:
    """
    file_names: [str] All file names

    return: 
        file names of all dysarthric spkrs
    """
    return list(filter(
        lambda x: x.split('-')[1][0:2] == 'XC',
        file_names
    ))

def __group_by_spkr__(file_names: [str]) -> dict:
    """
    file_names: [str] file names of dys spkrs

    return:
        dict [str: [str]], key is SPKR_ID, value is corresponding file_names
    """
    result = dict()
    for name in file_names:
        spkr_id = name.split('-')[1]
        if spkr_id in result.keys(): result[spkr_id].append(name)
        else: result[spkr_id] = []; result[spkr_id].append(name)
    return result        
            
