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
        return 5
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

    originalImg = CO.loadImage(PATHCONST.IMGINPUT)
    #originalImg = POP.imageLighter(originalImg, 1)
    os.chdir(r"C:\Users\75639\OneDrive\BHT\2. Se\Bildverarbeitung\Computer-Vision\pics\python")

    #kontrassImg = POP.imageKontrass(originalImg, 2)

    #kontrassImg = IL.Illuminate(originalImg, 5, 0.8)

    gaKernel, gaImg = GAUSF.gaussFilter(originalImg , GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)
    imgThreshold = TH.threshold(gaImg, 210, 50, 2)
    imgThreshold = TH.threshold(imgThreshold, 190, 200, 3)


    
    
    sobelGx, sobelGy, sobelImg = SOF.sobelFilter(imgThreshold, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)

    cannyImg = CANF.cannyFilter(imgThreshold, 10, 5, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)

    plt.subplot(221),plt.imshow(originalImg, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(imgThreshold, cmap = 'gray')
    plt.title('Thresholded Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(sobelImg, cmap = 'gray')
    plt.title('Sobel Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(cannyImg, cmap = 'gray')
    plt.title('Canny Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()
