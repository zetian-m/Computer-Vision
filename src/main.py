import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOF
import CannyFilter as CANF
import matplotlib.pyplot as plt
import Threshold as TH
import sys
import logging
import cv2

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
        return 3

class _SOBELFILCONST(object):
    """ Constants for using sobel filter
    Returns:
        _int_: kernelsize
    """
    @constant
    def KERNELSIZE():
        return 5

class _PATHCONST(object):
    @constant
    def IMGINPUT():
        return '\\lena.bmp'
        #Picture_Crossing_noise_10_pixelCnt_128_featureCnt_5
        #Picture_Crossing_noise_10_pixelCnt_65_featureCnt_9
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

    CO.imgPadding(originalImg, GAUSF.creatGaussKernel(50, 1), paddingMethod=0)

    originalImgTh = TH.threshold(originalImg, 150, 50, 1)

    plt.subplot(121),plt.imshow(originalImg,cmap = 'gray')
    plt.title('origi'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(originalImgTh,cmap = 'gray')
    plt.title('Threshold'), plt.xticks([]), plt.yticks([])
    plt.show()



    
    """#* GAUSS filtering
    timeStart = CO.stopwatchStart()
    gaussKernel, resultImg = GAUSF.gaussFilter(originalImg, GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)
    timeGaussFilter = CO.stopwatchStop(timeStart)
    print("Gauss Filter needed:", timeGaussFilter)

    #* SOBEL filtering
    timeStart = CO.stopwatchStart()
    sobelGx, sobelGy, resultImg = SOF.sobelFilter(originalImg, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Sobel Filter needed:", timeSobelFilter)

    timeStart = CO.stopwatchStart()
    resultImg = CANF.cannyFilter(originalImg, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    print(resultImg)

    cv2.imshow("YYY", resultImg)"""
    resultImg = CANF.cannyFilter(originalImg, 190, 180, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)

    opencvImg = cv2.Canny(originalImg, 50, 29)

    plt.subplot(131),plt.imshow(originalImg,cmap = 'gray')
    plt.title('imgOriginal'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(resultImg,cmap = 'gray')
    plt.title('imgCanny'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(opencvImg,cmap = 'gray')
    plt.title('imgCanny-opencv'), plt.xticks([]), plt.yticks([])
    plt.show()

    #* Plotting
    #plt.imshow(resultImg, interpolation='none', cmap='gray')
    #plt.show()
    



