import math
import matplotlib.pyplot as plt
import numpy as np
import common as CO

def creatSobelKernel(kernelSize):

    kernelY = []
    kernelX = []

    if kernelSize == 3:
        kernelX = np.array([[1, 0, -1], 
                                [2, 0, -2], 
                                [1, 0, -1]])
        kernelY = np.array([[1, 2, 1],
                                [0, 0, 0],
                                [-1, -2, -1]])
    if kernelSize == 5 :
        kernelX = np.array([[-1, -2, 0, 2, 1],
                                [-4, -8, 0, 8, 4],
                                [-6, -12, 0, 12, 6],
                                [-4, -8, 0, 8, 4],
                                [-1, -2, 0, 2, 1]])

        kernelY = np.array([[-1, -4, -6, -4, -1],
                                [-2, -8, -12, -8, -2],
                                [0, 0, 0, 0, 0],
                                [2, 8, 12, 8, 2],
                                [1, 4, 6, 4, 1]])


    kernel_dict = {"SOBEL_X": kernelX, "SOBEL_Y": kernelY}

    return kernelX, kernelY

def sobelFilter(originalImg, kernelSize):

    sobelKernelX, sobelKernelY = creatSobelKernel(kernelSize)
    
    Gx = CO.convolution(originalImg, sobelKernelX)
    Gy = CO.convolution(originalImg, sobelKernelY)

    resultImg = np.sqrt(Gx**2 + Gy**2)

    return resultImg

if __name__ == "__main__":
    #* Write the module test function here
    pass