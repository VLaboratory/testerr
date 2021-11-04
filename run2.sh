#!/bin/bash
unzip data/sat_product.zip -d tmp

python ex1.py $(ls -d tmp/*.SAFE)
