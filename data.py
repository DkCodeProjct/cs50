from PIL import Image
import sys
import csv

with open(sys.argv[1],'a') as file:
    cs50ShirtImage = Image.open(sys.argv[1] )
    pupetImage = Image.open(sys.argv[2])
    resizwImage = pupetImage.resize(cs50ShirtImage.size)

    outPutImage = resizwImage.copy()
    outPutImage.paste(cs50ShirtImage,(0,0),cs50ShirtImage)
    outPutImage.save(sys.argv[3])