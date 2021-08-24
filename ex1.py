
import sys
import numpy
from snappy import Product
from snappy import ProductData
from snappy import ProductIO
from snappy import ProductUtils
from snappy import FlagCoding

if len(sys.argv) != 2:
    print("usage: %s <file>" % sys.argv[0])
    sys.exit(1)

file = sys.argv[1]

print("Reading...")
product = ProductIO.readProduct(file)
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
