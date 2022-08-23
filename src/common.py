from email.errors import BoundaryError
from PIL import Image
import cv2
import os 
import numpy as np
import logging
import time
import matplotlib.pyplot as plt
from scipy import signal

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
    try:
        original_image = plt.imread(imagePath, plt.gray)
    except:
        original_image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

    return original_image

def convolution2D(image, kernel, convMethod):
    """ This is the common function for doing convolution 2D.

    Args:
        image (_intMatrix_):        Image Matrix
        kernel (_floatMatrix_):     Filter kernel
        convMethod (_int_):         0 for doing conv with own func
                                    1 for doing conv with python built in lib

    Returns:
        resultImg (_intMatrix_):    The new image after convolution
    """
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

    if convMethod == 0:
        for i in range(resultSizeX):
            for j in range(resultSizeY):
                resultImage[j][i] = np.sum(image[j:j+kernelSize, i:i+kernelSize] * kernel)
    
    elif convMethod == 1:
        resultImage = signal.convolve2d(image, kernel, boundary='symm', mode='same')

    else:
        print("Convolution Method not valid")

    #* change data format
    #resultImage = resultImage.astype(np.uint8)

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