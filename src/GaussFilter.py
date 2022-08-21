import math
import matplotlib.pyplot as plt
import numpy as np
import common as CO
import logging

def creatGaussKernel(kernelSize, sigma):

    gaussKsernel = np.zeros((kernelSize, kernelSize))

    kernelHalfSize = int(kernelSize/2)

    xArray = np.linspace(-kernelHalfSize, kernelHalfSize, kernelSize)
    yArray = np.linspace(-kernelHalfSize, kernelHalfSize, kernelSize)
    XX,YY = np.meshgrid(xArray, yArray)

    #creat kernel with the coordinats from kernelSize
    gaussKsernel = (1/(2*math.pi*sigma**2)) * np.exp( (-1) * ((XX**2 + YY**2) / (2 * sigma**2)) )

    #* plot the kernel
    """plt.imshow(gaussKsernel, interpolation='none', cmap='gray')
    plt.show()"""
    

    #todo: Normalisation
    #todo: is this the right way?
    #kernel = kernel/np.linalg.norm(kernel)
    gaussKsernel /= np.sum(gaussKsernel)

    return gaussKsernel

def gaussFilter(originalImg, kernelSize, sigma):

    gaussKernel = creatGaussKernel(kernelSize, sigma)
    resultImg = CO.convolution(originalImg, gaussKernel)

    return gaussKernel, resultImg

if __name__ == '__main__':
    #* Write the module test function here
    pass