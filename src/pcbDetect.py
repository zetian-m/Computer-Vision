import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOF
import CannyFilter as CANF
import matplotlib.pyplot as plt
import sys
import logging
import cv2
import PointOperator as POP

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
        return 3

class _PATHCONST(object):
    @constant
    def IMGINPUT():
        return '\\PCB\\LADEIC_MICRO_TOP1.bmp'
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

    kontrassImg = POP.imageKontrass(originalImg, 1.5)
    plt.imshow(kontrassImg, interpolation='none', cmap='gray')
    plt.show()

    #* GAUSS filtering
    timeStart = CO.stopwatchStart()
    gaussKernel, resultImg = GAUSF.gaussFilter(kontrassImg, GAUSSFCONST.KERNELSIZE, GAUSSFCONST.SIGMA, CONVCONST.CONVMETHOD)
    timeGaussFilter = CO.stopwatchStop(timeStart)
    print("Gauss Filter needed:", timeGaussFilter)
    plt.imshow(resultImg, interpolation='none', cmap='gray')
    plt.show()

    #* SOBEL filtering
    timeStart = CO.stopwatchStart()
    sobelGx, sobelGy, resultImg = SOF.sobelFilter(resultImg, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    timeSobelFilter = CO.stopwatchStop(timeStart)
    print("Sobel Filter needed:", timeSobelFilter)
    plt.imshow(resultImg, interpolation='none', cmap='gray')
    plt.show()
   
    timeStart = CO.stopwatchStart()
    resultImg = CANF.cannyFilter(originalImg, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    plt.imshow(resultImg, interpolation='none', cmap='gray')
    plt.show()
    resultImg = cv2.Canny(originalImg, 170,120)
    #resultImg = CANF.cannyFilter(originalImg, GAUSSFCONST.SIGMA, SOFCONST.KERNELSIZE, CONVCONST.CONVMETHOD)
    

    #plt.imshow(resultImg, interpolation='none', cmap='gray')
    plt.show()
    cv2.waitKey()

    #* Plotting
    #plt.imshow(resultImg, interpolation='none', cmap='gray')
    #plt.show()
    



