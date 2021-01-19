# Credit: Mengzhe GENG

import os
import sys

from tqdm import tqdm

# inFile = sys.argv[1]
# outFile = sys.argv[2]




def add_time_stamp_fbk(fin: str, fout: str):
    result = []

    mapping_dct = {}
    mapping_dct['1'] = '0'
    mapping_dct['2'] = '00'
    mapping_dct['3'] = '000'
    mapping_dct['4'] = '0000'
    mapping_dct['5'] = '00000'
    mapping_dct['6'] = '000000'
    mapping_dct['7'] = '000000'
    with open(fout, 'w+') as out_f:
        with open(fin, 'r') as f:
            for line in tqdm(f.readlines()):
                line = line.strip()
                cmd = '/project/bdda/mengzhe/HTK/HTK-3.5.beta-2/htk/bin.cpu/HList -h -e 0 ' + line
                output = os.popen(cmd)
                output = output.read().split(' ')
                index = output.index('Samples:')
                end = str(int(output[index+3])-1)
                first_name = line.split('/')[-1].split('.')[0]+'_0000000' \
                    + '_' + mapping_dct[str(7-len(end))] + end + '.fbk'
                second_name = line + '[0,' + end + ']'
                result.append(first_name + '=' + second_name + '\n')
            out_f.writelines(result)









