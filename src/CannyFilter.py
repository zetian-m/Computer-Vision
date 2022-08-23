import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOBF
import matplotlib.pyplot as plt
import numpy as np

def nearestQuarter(ang):
    # round the angle to a quarter
    return (((round(((ang)/np.pi)/0.5))/4)*(2*np.pi)) % (2*np.pi)

def roundAngle(sobelPixelAngle):

    pixelMatrixSize = sobelPixelAngle.shape
    pixelAngleRounded = np.zeros(pixelMatrixSize)
    for x in range (pixelMatrixSize[0]):
        for y in range (pixelMatrixSize[1]):
            pixelAngleRounded[x][y] = nearestQuarter(sobelPixelAngle[x][y])

    return pixelAngleRounded

def setPixelGradientValue(pixelGradientList):

    maxPixelGradient = np.amax(pixelGradientList)

    for index, pixelGradient in np.ndenumerate(pixelGradientList):
        if pixelGradient != maxPixelGradient:
            pixelGradient = 0
        else:
            continue
    return pixelGradientList

def nonMaximaSuppression(edgeGradient, pixelAngleRounded):
    TOP = 0
    RIGHT = 0.5*np.pi
    BOTTOM = np.pi
    LEFT = 1.5*np.pi

    if edgeGradient.shape != pixelAngleRounded.shape:
        return -1

    gradientSizeX, gradientSizeY = edgeGradient.shape

    newEdgeGradient = np.zeros((gradientSizeX, gradientSizeY))

    #* Because of 3x3 submatrix, the iteration goes only for (size-2)
    for y in range(gradientSizeY-2):
        for x in range(gradientSizeX-2):
            #* get 3x3 submatrix for nonMaximaSuppression
            subEdgeGradient = edgeGradient[y:y+3, x:x+3]
            subPixelAngleRounded = pixelAngleRounded[y:y+3, x:x+3]

            #* get the central point value -> angle and gradient
            centralPixelAngle = subPixelAngleRounded.item((1,1))
            #centralPixelGradient = subEdgeGradient.item((1,1))

            #* check the angle direction
            if  centralPixelAngle == TOP or centralPixelAngle == BOTTOM:
                #* compare the central gradient value with TOP and BOTTOM
                pixelGradientList = subEdgeGradient[1:2, 0:3]

                pixelGradientList = setPixelGradientValue(pixelGradientList)

                subEdgeGradient[1:2, 0:3] = pixelGradientList

            elif centralPixelAngle == LEFT or centralPixelAngle == RIGHT:

                pixelGradientList = subEdgeGradient[0:3, 1:2]

                pixelGradientList = setPixelGradientValue(pixelGradientList)

                subEdgeGradient[0:3, 1:2] = pixelGradientList

            else:
                return -1
            newEdgeGradient[y:y+3, x:x+3] = subEdgeGradient
            x += 3
        y += 3    
            #print(subEdgeGradient.item(1,1))
        
    return newEdgeGradient        

    #todo: Take a 3x3 Matrix
    #todo: check direction TOP, RIGHT, BOTTOM, LEFT
    #todo: set 0 or keep value
    pass




def cannyFilter(inputImg, sigma, sobelKernelSize = 3, convMethod = 0):
    GAUSKERNELSIZE = 5

    #* Step 1: Noise Reduction with gauss filter by 5x5 Kernel
    gaussKernel, imgGaussFiltered = GAUSF.gaussFilter(inputImg, GAUSKERNELSIZE, sigma, convMethod)

    #* Step 2.1: Finding Intensity Gradient of the image by using sobel filer
    #* Sobel-Kernel size is by default: 3
    Gx, Gy, EdgeGradient = SOBF.sobelFilter(imgGaussFiltered, sobelKernelSize, convMethod)

    #* Step 2.2: Calculate Angle of each pixel 
    pixelAngle = np.arctan2(Gy, Gx)
    print(pixelAngle)
    
    #* Step 2.3: Round all angles to a quater of a circle (0, 0.5*pi, pi, 1,5*pi)
    pixelAngleRounded = roundAngle(pixelAngle)

    #* Step 3: Application of Non-maxima suppression
    EdgeGradient = nonMaximaSuppression(EdgeGradient, pixelAngleRounded)

    #sobelPixelAngleRounded = sobelPixelAngleRounded.astype(np.uint8)
    plt.imshow(EdgeGradient, interpolation='none', cmap='gray')
    plt.show()


if __name__ == "__main__":
    pass

    


