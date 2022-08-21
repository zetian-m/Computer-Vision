
#!
#todo
#//
#*
#
#?
from PIL import Image
import cv2
import os 

def fun():
    """ Function documentation example
    """
    pass

def loadImage(imgFileName):
    
    currentPath = os.getcwd()

    #* Use \\ instead \
    imagePath = currentPath +  "\\pics\\original\\" + imgFileName 

    print(imagePath)

    original_image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

    return original_image

def convolution():
    pass

if __name__ == "__main__":
    pass