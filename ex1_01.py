
import os
import sys
import numpy
from snappy import Product
from snappy import ProductData
from snappy import ProductIO
from snappy import ProductUtils
from snappy import FlagCoding

from pathlib import Path  #test


if len(sys.argv) != 2:
    print("usage: %s <file>" % sys.argv[1])
    sys.exit(1)

file = sys.argv[1]

print(file)

#dirs = os.listdir( path )
# This would print all the files and directories
#for file in dirs:
#   print(file)
dirname,filename=os.path.split(file)
print(filename)

"""
output = "output.txt"
with open(output, "a") as outputfile:
    outputfile.write(file)
"""
print("Reading...")
product = ProductIO.readProduct(file)
#product = ProductIO.readProduct(filename)
width = product.getSceneRasterWidth()
height = product.getSceneRasterHeight()
name = product.getName()
description = product.getDescription()
band_names = product.getBandNames()

print("Product:     %s, %s" % (name, description))
print("Raster size: %d x %d pixels" % (width, height))
print("Start time:  " + str(product.getStartTime()))
print("End time:    " + str(product.getEndTime()))
print("Bands:       %s" % (list(band_names)))

output = "output.txt"
with open(output, "a") as outputfile:
    outputfile.write("Product:     %s, %s" % (name, description)+"\n")
    outputfile.write("Raster size: %d x %d pixels" % (width, height)+"\n")
    outputfile.write("Start time:  " + str(product.getStartTime())+"\n")
    outputfile.write("End time:    " + str(product.getEndTime())+"\n")
    outputfile.write("Bands:       %s" % (list(band_names))+"\n")
