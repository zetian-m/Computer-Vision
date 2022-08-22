import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOF
import CannyFilter as CANF
import matplotlib.pyplot as plt
import sys
import logging

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
        return 5
    @constant
    def KERNELSIZE():
        return 33

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
        return 'Picture_Crossing_noise_0_pixelCnt_128_featureCnt_5.bmp'
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

    
    #* GAUSS filtering
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

    #* Plotting
    #plt.imshow(resultImg, interpolation='none', cmap='gray')
    #plt.show()
    



