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

                #* search for max and discard other value
                pixelGradientList = setPixelGradientValue(pixelGradientList)

                subEdgeGradient[1:2, 0:3] = pixelGradientList

            elif centralPixelAngle == LEFT or centralPixelAngle == RIGHT:
                #* compare the cantral gradient value with LEFT and RIGHT
                pixelGradientList = subEdgeGradient[0:3, 1:2]
                #* search for max and discard other value
                pixelGradientList = setPixelGradientValue(pixelGradientList)

                subEdgeGradient[0:3, 1:2] = pixelGradientList

            else:
                return -1
            newEdgeGradient[y:y+3, x:x+3] = subEdgeGradient
            x += 3
        y += 3    
            #print(subEdgeGradient.item(1,1))
        
    return newEdgeGradient        

def cannyThreshold(edgeGradient, thUpper, thLower):

    gradientSizeX, gradientSizeY = edgeGradient.shape

    #* go throught every pixel in the edgeGardient
    for x in range (gradientSizeX):
        for y in range (gradientSizeY):

            #* Get the central pixel value
            pixelValue = edgeGradient.item((x,y))

            
            if pixelValue >= thUpper:
                #* Value above threshold upper -> take it as a edge
                pixelValue = 255
            elif pixelValue <= thLower:
                #* Value under threshold lower -> discard it
                pixelValue = 0
            else:
                #* Value between threshold upper and lower -> take it and check connectivity
                pass


            #* Set the pixel value
            edgeGradient[x,y] = pixelValue

    #* Check if this pixel connects to a edge
    plt.imshow(edgeGradient, interpolation='none', cmap='gray')
    plt.show()
    
    for y in range(gradientSizeY-2):
        for x in range(gradientSizeX-2):
            #* Get the 3x3 submatrix surrounding
            subEdgeGradient = edgeGradient[y:y+3, x:x+3]
            #* Get the central pixel value
            centralPixelValue = subEdgeGradient.item((1,1))
            
            if  centralPixelValue < thUpper and centralPixelValue > thLower:
                #* only consider the value that between threshold
                connectedToEdge = False
                
                for index, pixelValue in np.ndenumerate(subEdgeGradient) :
                    
                    if pixelValue >= thUpper:
                        #* Check if there is any pixel value larger than threshold upper
                        #* but this pixel is not the central pixel
                        connectedToEdge = True
                        break
                    else:
                        continue
                
                if not connectedToEdge:
                    subEdgeGradient[1, 1] = 0
                    
                else:
                    subEdgeGradient[1, 1] = 255
                    
                #* Change value of edgeGradient
                edgeGradient[y:y+3, x:x+3] = subEdgeGradient
                

                

              
            else:
                continue
                
    return edgeGradient



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
    plt.imshow(EdgeGradient, interpolation='none', cmap='gray')
    plt.show()
    #* Step 4: Thresholding
    EdgeGradient = cannyThreshold(EdgeGradient, 220, 190)



    #sobelPixelAngleRounded = sobelPixelAngleRounded.astype(np.uint8)
    plt.imshow(EdgeGradient, interpolation='none', cmap='gray')
    plt.show()

    return EdgeGradient


if __name__ == "__main__":
    pass

    


