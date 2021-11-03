#!/bin/bash
#unzip data/s2.zip -d /tmp/unzipped
unzip data/sat_product.zip -d /tmp/data
#python ex1.py /tmp/sat_product/*.SAFE
#python ex1.py $(ls -d /tmp/sat_product/*.SAFE)

python ex1_01.py $(ls -d /tmp/data/*.SAFE)

#python ex1.py /tmp/unzipped/*.SAFE
#$(ls -d /tmp/unzipped/*.SAFE)
