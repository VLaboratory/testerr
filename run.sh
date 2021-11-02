#unzip data/s2.zip -d /tmp/unzipped
unzip data/s2.zip
python ex1.py *.SAFE
#python ex1.py /tmp/unzipped/*.SAFE
#$(ls -d /tmp/unzipped/*.SAFE)
