#!/bin/bash
#unzip data/sat_product.zip -d tmp

#python ex1.py tmp/*.SAFE


unzip data/sat_product.zip -d /tmp/unzipped
#debug lines
ls -l /tmp/unzipped/
ls -l /tmp/unzipped/*/
ls -d /tmp/unzipped/*.SAFE

python ex1.py $(ls -d /tmp/unzipped/*.SAFE)
