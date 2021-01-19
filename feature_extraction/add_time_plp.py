import os
import sys


def add_time_stamp_plp(fin: str, fout: str):
    result = []

    mapping_dct = {}
    mapping_dct['1'] = '0'
    mapping_dct['2'] = '00'
    mapping_dct['3'] = '000'
    mapping_dct['4'] = '0000'
    mapping_dct['5'] = '00000'
    mapping_dct['6'] = '000000'
    mapping_dct['7'] = '000000'
    with open(fout, 'w') as out_f:
        with open(fin, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                cmd = 'HList -h -e 0 ' + line
                output = os.popen(cmd)
                output = output.read().split(' ')
                index = output.index('Samples:')
                end = str(int(output[index+3])-1)
                first_name = line.split('/')[-1].split('.')[0]+'_0000000'+ '_' + mapping_dct[str(7-len(end))] + end + '.plp'
                second_name = line + '[0,' + end + ']'
                result.append(first_name + '=' + second_name + '\n')
            out_f.writelines(result)
