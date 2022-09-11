import math
import matplotlib.pyplot as plt
import numpy as np
import common as CO
import logging
import cv2

def creatGaussKernel(kernelSize, sigma):

    gaussKernel = np.zeros((kernelSize, kernelSize))

    kernelHalfSize = int(kernelSize/2)

    xArray = np.linspace(-kernelHalfSize, kernelHalfSize, kernelSize)
    yArray = np.linspace(-kernelHalfSize, kernelHalfSize, kernelSize)
    XX,YY = np.meshgrid(xArray, yArray)

    #creat kernel with the coordinats from kernelSize
    gaussKernel = (1/(2*math.pi*sigma**2)) * np.exp( (-1) * ((XX**2 + YY**2) / (2 * sigma**2)) )

    #* plot the kernel
    """plt.imshow(gaussKernel, interpolation='none', cmap='gray')
    plt.show()"""
    

    #todo: Normalisation
    #todo: is this the right way?
    #kernel = kernel/np.linalg.norm(kernel)
    gaussKernel /= np.sum(gaussKernel)
    

    #* Uncomment this for proving gauss kernel with opencv
    # plt.imshow(gaussKernel, interpolation='none', cmap='gray')
    # plt.show()
    # gaussKernel = cv2.getGaussianKernel(kernelSize, 1)
    # gaussKernel = gaussKernel * gaussKernel.transpose(1,0)
    # plt.imshow(gaussKernel, interpolation='none', cmap='gray')
    # plt.show()
    

    return gaussKernel

def gaussFilter(originalImg, kernelSize, sigma, convMethod=0):

    gaussKernel = creatGaussKernel(kernelSize, sigma)

    resultImg = CO.convolution2D(originalImg, gaussKernel, convMethod)

    gaussKernel = gaussKernel
    resultImg = resultImg.astype(np.uint8)

    return gaussKernel, resultImg

if __name__ == '__main__':
    #* Write the module test function here
    pass