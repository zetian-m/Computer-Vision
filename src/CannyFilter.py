import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOBF
import matplotlib.pyplot as plt
import numpy as np

def nearest_quarter(ang):
    return (((round(((ang)/np.pi)/0.5))/4)*(2*np.pi)) % (2*np.pi)

def roundAngle(sobelPixelAngle):

    pixelMatrixSize = sobelPixelAngle.shape
    pixelAngleRounded = np.zeros(pixelMatrixSize)
    for x in range (pixelMatrixSize[0]):
        for y in range (pixelMatrixSize[1]):
            print(sobelPixelAngle[x:y])
            pixelAngleRounded[x:y] = nearest_quarter(nearest_quarter(sobelPixelAngle[x:y]))
    #for pixelArray, pixelRoundedArray in sobelPixelAngle, pixelAngleRounded:
    #    for pixel, pixelRounded in pixelArray, pixelRoundedArray:
            

    return pixelAngleRounded


def cannyFilter(inputImg, sigma, sobelKernelSize = 3, convMethod = 0):
    GAUSKERNELSIZE = 5

    #* Step 1: Noise Reduction with gauss filter by 5x5 Kernel
    gaussKernel, imgGaussFiltered = GAUSF.gaussFilter(inputImg, GAUSKERNELSIZE, sigma, convMethod)

    #* Step 2.1: Finding Intensity Gradient of the image by using sobel filer
    #* Sobel-Kernel size is by default: 3
    Gx, Gy, EdgeGradient = SOBF.sobelFilter(imgGaussFiltered, sobelKernelSize, convMethod)

    #* Step 2.2: Calculate Angle of each pixel 
    #* (rounded to one of four angles representing vertical, horizontal and two diagonal directions)

    sobelPixelAngle = np.arctan2(Gy, Gx)
    print(sobelPixelAngle)
    #sobelPixelAngle = sobelPixelAngle.astype(np.uint8)

    sobelPixelAngleRounded = roundAngle(sobelPixelAngle)
    sobelPixelAngleRounded = sobelPixelAngleRounded.astype(np.uint8)
    plt.imshow(sobelPixelAngleRounded, interpolation='none', cmap='gray')
    plt.show()


if __name__ == "__main__":
    pass

    


