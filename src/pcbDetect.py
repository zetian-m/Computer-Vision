import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOF
import CannyFilter as CANF
import matplotlib.pyplot as plt
import sys
import logging
import cv2
import PointOperator as POP
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

    gaKernel, gaImg = GAUSF.gaussFilter(originalImg, GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)
    #* SOBEL filtering
    timeStart = CO.stopwatchStart()
    sobelGx, sobelGy, sobelImg = SOF.sobelFilter(gaImg, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Sobel Filter needed:", timeSobelFilter)

    timeStart = CO.stopwatchStart()
    cannyImg = CANF.cannyFilter(sobelImg, 130, 120, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Canny Filter needed:", timeSobelFilter)

    imgThreshold = TH.threshold(sobelImg, 50, 15, 4)
    #imgThreshold = TH.threshold(sobelImg, 150, 15, 2)

    plt.subplot(151),plt.imshow(originalImg, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(152),plt.imshow(gaImg, cmap = 'gray')
    plt.title('Gauss Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(153),plt.imshow(sobelImg, cmap = 'gray')
    plt.title('Sobel Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(154),plt.imshow(cannyImg, cmap = 'gray')
    plt.title('Canny Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(155),plt.imshow(imgThreshold, cmap = 'gray')
    plt.title('Threshold'), plt.xticks([]), plt.yticks([])
    plt.show()


    gaKernel, gaImg = GAUSF.gaussFilter(originalImg, GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)

    plt.subplot(131),plt.imshow(originalImg, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(gaKernel, cmap = 'gray')
    plt.title('Gauss Kernel'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(gaImg, cmap = 'gray')
    plt.title('Image after Gaussfiltering'), plt.xticks([]), plt.yticks([])
    plt.show()


    kontrassImg = POP.imageKontrass(originalImg, 1.5)

    imgThreshold = TH.threshold(kontrassImg, 110, 90, 2)

    plt.subplot(131),plt.imshow(originalImg,cmap = 'gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(kontrassImg,cmap = 'gray')
    plt.title('kontrass'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(imgThreshold,cmap = 'gray')
    plt.title('Threshold'), plt.xticks([]), plt.yticks([])
    plt.show()

    #thresholdImg = TH.threshold(kontrassImg, 150, 140, 3)

    timeStart = CO.stopwatchStart()
    gausskernel, gaussImg = GAUSF.gaussFilter(originalImg, GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Gauss Filter needed:", timeSobelFilter)


    

    plt.subplot(131),plt.imshow(originalImg,cmap = 'gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(kontrassImg,cmap = 'gray')
    plt.title('kontrass'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(gaussImg,cmap = 'gray')
    plt.title('Gauss'), plt.xticks([]), plt.yticks([])
    plt.show()

    #* SOBEL filtering
    timeStart = CO.stopwatchStart()
    sobelGx, sobelGy, sobelImg = SOF.sobelFilter(originalImg, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Sobel Filter needed:", timeSobelFilter)

    timeStart = CO.stopwatchStart()
    cannyImg = CANF.cannyFilter(originalImg, 70, 50, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Canny Filter needed:", timeSobelFilter)

    #* Plotting
    plt.subplot(221),plt.imshow(originalImg,cmap = 'gray')
    plt.title('imgOriginal'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(originalImg,cmap = 'gray')
    plt.title('img kontrass higher'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(sobelImg,cmap = 'gray')
    plt.title('imgSobel'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(cannyImg,cmap = 'gray')
    plt.title('imgCanny'), plt.xticks([]), plt.yticks([])
    plt.show()
    
    cv2.imwrite("CannyFiltered2.bmp", cannyImg)
    plt.imshow(cannyImg,cmap = 'gray')
    plt.show()
    #plt.imshow(resultImg, interpolation='none', cmap='gray')
    #plt.show()
    



