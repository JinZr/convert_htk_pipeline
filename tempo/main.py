import sox

import os
import logging
import argparse
import threading

# import t_conf
from tempo import parse_scp_and_tempo


parser = argparse.ArgumentParser(description='Arguments for running tempo stretch using sox')

parser.add_argument('--show_warning', type=bool, default=False)
parser.add_argument('--scp_path', type=str, required=True)
parser.add_argument('--tempo_path', type=str, required=True)

args = parser.parse_args()

if __name__ == "__main__":
    if not args.show_warning: logging.getLogger('sox').setLevel(logging.ERROR)
 
    print('<<<<<<<<<<<<<<<<<<<< {} <<<<<<<<<<<<<<<<<<<<'.format('Parse SCP'))
    parse_scp_and_tempo(scp_path=args.scp_path, tempo_path=args.tempo_path)
    
