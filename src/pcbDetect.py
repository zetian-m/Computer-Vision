import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOF
import CannyFilter as CANF
import matplotlib.pyplot as plt
import sys
import logging
import cv2
import PointOperator as POP
import Illuminate as IL
import Threshold as TH
import MedianFilter as MF
import os

#############################################
#                                           #
#                 Constants                 #
#                                           #
#############################################
def constant(f):
    """ Definetion of constants in this Python-Script.
        If you try to change the constants, it will show error.
    Args:
        f (_type_): _description_
    """
    def fset(self, value):
            raise TypeError
    def fget(self):
            return f()
    return property(fget, fset)

class _CONVCONST(object):
    @constant
    def CONVMETHOD():
        return 1

class _GAUSSFILCONST(object):
    """ Constants for using gauss filter
    Returns:
        _int_: kernelsize, sigma
    """
    @constant
    def SIGMA():
        #9.3
        #0.93
        #1
        return 1
    @constant
    def KERNELSIZE():
        return 5

class _SOBELFILCONST(object):
    """ Constants for using sobel filter
    Returns:
        _int_: kernelsize
    """
    @constant
    def KERNELSIZE():
        return 3

class _PATHCONST(object):
    @constant
    def IMGINPUT():
        return '\\PCB\\BMS_TOP3.bmp'
#############################################
#                                           #
#              End of Constants             #
#                                           #
#############################################    


    
if __name__ == "__main__":
    GAUSSFCONST = _GAUSSFILCONST()
    SOFCONST = _SOBELFILCONST()
    CONVCONST = _CONVCONST()
    PATHCONST = _PATHCONST() 
    #

    originalImg = CO.loadImage(PATHCONST.IMGINPUT)
    #originalImg = POP.imageLighter(originalImg, 1)
    os.chdir(r"C:\Users\75639\OneDrive\BHT\2. Se\Bildverarbeitung\Computer-Vision\pics\python")

    #kontrassImg = POP.imageKontrass(originalImg, 2)

    #kontrassImg = IL.Illuminate(originalImg, 5, 0.8)

    #!! LowPass Median-Filter
    medianImg = MF.medianFilter(originalImg, 7, CONVCONST.CONVMETHOD)
    plt.subplot(121),plt.imshow(originalImg, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(medianImg, cmap = 'gray')
    plt.title('Median Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    

    #!! High Pass - Threshold->Sobel und Canny
    gaKernel, gaImg = GAUSF.gaussFilter(originalImg , GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)
    plt.imshow(gaImg , cmap = 'gray')
    plt.show()
    imgThreshold = TH.threshold(gaImg, 200, 50, 2)
    plt.imshow(imgThreshold, cmap = 'gray')
    plt.show()

    sobelGx, sobelGy, sobelImg = SOF.sobelFilter(imgThreshold, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)

    cannyImg = CANF.cannyFilter(imgThreshold, 5, 3, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    """cv2.imwrite("Original.png", originalImg)
    cv2.imwrite("ThresholdImg.png", imgThreshold)
    cv2.imwrite("Sobel_PCB.png", sobelImg)
    cv2.imwrite("Canny_PCB.png", cannyImg)
"""
    plt.subplot(221),plt.imshow(originalImg, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(imgThreshold, cmap = 'gray')
    plt.title('Thresholded Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(sobelImg, cmap = 'gray')
    plt.title('Sobel Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(cannyImg, cmap = 'gray')
    plt.title('Canny Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()


    


