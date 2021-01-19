#!/bin/bash 

inark=$1
outdir=$2

source /opt/share/etc/gcc-5.4.0.sh

copy-feats-to-htk --output-dir=$2 --output-ext=fbk --sample-period=100000 ark:$1

