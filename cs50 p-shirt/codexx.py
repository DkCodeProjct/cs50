from PIL import Image
from PIL import ImageOps
import os
import sys

def main():
    checkSys()
    try:
        imageFile = Image.open(sys.argv[1])  # 'before.png'
    except FileNotFoundError:
        sys.exit('Invalid input')


    shirtFile = Image.open('shirt.png')
    sizeImage = shirtFile.size
    muppet = ImageOps.fit(imageFile, shirtFile.size)
    
    muppet.paste(shirtFile, (0, 0), shirtFile)
    muppet.save(sys.argv[2])  # 'output.png'


def fileExtension(file):
    # Check if the file extension is in the list ['.jpg', '.png']
    if file[1].lower() in ['.jpg', '.png']:
        return True
    return False

def checkSys():
    if len(sys.argv) != 3:
        sys.exit('too many comand-line argument')
    if len(sys.argv) > 3:
        sys.exit('too many comand-line argument')

    if len(sys.argv) < 3:
        sys.exit('too few command-line argument')
    
    imageFile, outuptFile = os.path.splitext(sys.argv[1]), os.path.splitext(sys.argv[2])

    # Check if the file extensions are valid
    if not fileExtension(imageFile):
        sys.exit('Invalid input')

    if not fileExtension(outuptFile):
        sys.exit('Invalid input')

    
    # Compare the file extensions correctly
    if imageFile[1].lower() != outuptFile[1].lower():
        sys.exit("input and output file extensions do not match")

main()
