import math
import matplotlib.pyplot as plt
import numpy as np
import common as CO
import logging

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

    return gaussKernel

def gaussFilter(originalImg, kernelSize, sigma, convMethod=0):

    gaussKernel = creatGaussKernel(kernelSize, sigma)
    
    resultImg = CO.convolution2D(originalImg, gaussKernel, convMethod)

    return gaussKernel, resultImg

if __name__ == '__main__':
    #* Write the module test function here
    pass