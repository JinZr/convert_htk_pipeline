import os
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

mapping_dct = {}
mapping_dct['1'] = '0'
mapping_dct['2'] = '00'
mapping_dct['3'] = '000'
mapping_dct['4'] = '0000'
mapping_dct['5'] = '00000'
mapping_dct['6'] = '000000'
mapping_dct['7'] = '000000'
with open(outFile, 'w') as out_f:
    with open(inFile, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cmd = 'HList -h -e 0 ' + line
            output = os.popen(cmd)
            output = output.read().split(' ')
            index = output.index('Samples:')
            end = str(int(output[index+3])-1)
            first_name = line.split('/')[-1].split('.')[0]+'_0000000'+ '_' + mapping_dct[str(7-len(end))] + end + '.plp'
            second_name = line + '[0,' + end + ']'
            out_f.write(first_name + '=' +second_name + '\n')
