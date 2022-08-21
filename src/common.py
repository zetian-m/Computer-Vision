

from PIL import Image
import cv2
import os 
import numpy as np
import logging
import time
import matplotlib.pyplot as plt

#*
#?
#todo
#+
#//
#!!


def fun():
    """ Function documentation example
    """
    pass

def loadImage(imgFileName):

    currentPath = os.getcwd()

    #* Use \\ instead \
    imagePath = currentPath +  "\\pics\\original\\" + imgFileName 

    print(imagePath)

    #* Could also use the cv2 function instead
    original_image = plt.imread(imagePath, plt.gray)

    return original_image

def convolution(image, kernel):

    #* Get Size of image and kernel
    imgSizeX, imgSizeY = image.shape
    kernelSizeX, kernelSizeY = kernel.shape

    
    
    #* Check if both are square
    if imgSizeX == imgSizeY:
        imgSize = imgSizeX
    else:
        logging.warning("imgSizeX != imgSizeY")
    if kernelSizeX == kernelSizeY:
        kernelSize = kernelSizeX
    else:
        logging.warning("kernelSizeX != kernelSizeY")

    resultSizeX = imgSize - kernelSize + 1
    resultSizeY = imgSize - kernelSize + 1

    #* Notice that np.zeros() has different position of X and Y in input
    resultImage = np.zeros((resultSizeY,resultSizeX))

    for i in range(resultSizeX):
        for j in range(resultSizeY):
            resultImage[j][i] = np.sum(image[j:j+kernelSize, i:i+kernelSize] * kernel)
    
    return resultImage

def stopwatchStart():
    start = time.time()
    return start

def stopwatchStop(start):
    stop = time.time()

    return stop-start

if __name__ == "__main__":
    #* Write the module test function here
    pass