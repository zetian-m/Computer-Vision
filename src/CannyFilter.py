import common as CO
import GaussFilter as GAUSF
import SobelFilter as SOBF
import matplotlib.pyplot as plt
import numpy as np
import cv2

#* This canny filter was implemented with this website as tutorial: 
#* https://pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/
#* https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123

def nearestQuarter(ang):
    # round the angle to a quarter
    return (0.5*np.pi) * (np.round(ang / (0.5*np.pi)))

def roundAngle(sobelPixelAngle):

    angleMatrixRows, angleMatrixCols = sobelPixelAngle.shape
    pixelAngleRounded = np.zeros(sobelPixelAngle.shape)
    #* Go through each pixel and round the angle value
    for r in range (angleMatrixRows):
        for c in range (angleMatrixCols):
            pixelAngleRounded[r, c] = nearestQuarter(sobelPixelAngle[r, c])

    return pixelAngleRounded

def nonMaximaSuppression(edgeGradient, pixelAngleRounded):
    #* Set the direction Value
    TOP = 0.5*np.pi
    RIGHT1 = np.pi
    RIGHT2 = -np.pi
    BOTTOM = -0.5*np.pi
    LEFT = 0

    numRows, numCols = edgeGradient.shape

    newEdgeGradient = np.zeros(edgeGradient.shape)

    #* Because of NMS, the value in a 3x3 matrix will be searched. 
    #* Beginns with 1 and ends with numCols-1

    for r in range(1, numRows-1):
        for c in range(1, numCols-1):

            #* get the central pixel Angle
            centralPixelAngle = pixelAngleRounded[r,c]

            #* check the angle direction of central pixel

            if  centralPixelAngle in (TOP, BOTTOM):
                #* compare the central gradient value with TOP and BOTTOM
                neighborPixelA = edgeGradient[r+1, c]
                neighborPixelB = edgeGradient[r-1, c]

            elif centralPixelAngle in (LEFT, RIGHT1, RIGHT2):
                #* compare the cantral gradient value with LEFT and RIGHT
                neighborPixelA = edgeGradient[r,c+1]
                neighborPixelB = edgeGradient[r,c-1]

            else:
                return -1

            #* If the central gradient larger than others in the direction, then consider this. Else equals 0
            if edgeGradient[r,c] > neighborPixelA and edgeGradient[r,c] > neighborPixelB:
                newEdgeGradient[r,c] = edgeGradient[r,c]
        
    return newEdgeGradient    

def cannyThreshold(edgeGradient, thUpper, thLower):



    numRows, numCols = edgeGradient.shape
    newEdgeGradient = np.zeros(edgeGradient.shape)
    #* go throught every pixel in the edgeGardient
    for r in range (0, numRows):
        for c in range (0, numCols):

            #* Get the central pixel value
            centralPixelValue = edgeGradient[r, c]
            if centralPixelValue >= thUpper:
                #* Value above threshold upper -> take it as a edge
                centralPixelValue = 255
            elif centralPixelValue <= thLower:
                #* Value under threshold lower -> discard it
                centralPixelValue = 0
            else:
                centralPixelValue = 0
                #* Value between threshold upper and lower -> take it and check connectivity
                pass

            #* Set the pixel value
            newEdgeGradient[r,c] = centralPixelValue
    
    #* Check if this pixel connects to a edge
    for r in range(numRows-2):
        for c in range(numCols-2):
            #* Get the 3x3 submatrix surrounding
            subEdgeGradient = newEdgeGradient[r:r+3, c:c+3]
            #* Get the central pixel value
            centralPixelValue = subEdgeGradient[1,1]

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
                newEdgeGradient[r:r+3, c:c+3] = subEdgeGradient
            else:
                continue
    #* Uncomment this to see the result of hysteresis Thresholding
    """plt.subplot(131),plt.imshow(edgeGradient, cmap = 'gray')
    plt.title('oldEdgeGradient'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(133),plt.imshow(newEdgeGradient, cmap = 'gray')
    plt.title('EndEdgeGradient'), plt.xticks([]), plt.yticks([])
    plt.show()"""      


    return newEdgeGradient

def cannyFilter(inputImg, sigma, upperThreshold, lowerThreshold, sobelKernelSize = 3, convMethod = 1 ):
    GAUSKERNELSIZE = 3

    #* Step 1: Noise Reduction with gauss filter by 5x5 Kernel
    gaussKernel, imgGaussFiltered = GAUSF.gaussFilter(inputImg, GAUSKERNELSIZE, sigma, convMethod)

    #* Step 2.1: Finding Intensity Gradient of the image by using sobel filer
    #* Sobel-Kernel size is by default: 3
    sobelKernelX, sobelKernelY = SOBF.creatSobelKernel(sobelKernelSize)
    Gx = CO.convolution2D(imgGaussFiltered, sobelKernelX, convMethod)
    Gy = CO.convolution2D(imgGaussFiltered, sobelKernelY, convMethod)
    EdgeGradient = (Gx ** 2 + Gy ** 2) ** 0.5

    #* Uncomment to see the result of sobel filter
    """plt.subplot(221),plt.imshow(imgGaussFiltered,cmap = 'gray')
    plt.title('imgGaussFiltered'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(Gx,cmap = 'gray')
    plt.title('Gx'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(Gy,cmap = 'gray')
    plt.title('Gy'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(EdgeGradient,cmap = 'gray')
    plt.title('EdgeGradient'), plt.xticks([]), plt.yticks([])
    plt.show()"""

    #* Step 2.2: Calculate Angle of each pixel 
    pixelAngle = np.arctan2(Gy, Gx)
    
    
    #* Step 2.3: Round all angles to a quater of a circle
    #* LEFT     -> rad:0, degree:0
    #* TOP      -> rad:1.57, degree:90
    #* BOTTOM   -> rad:-1.57, degree:-90
    #* RIGHT    -> rad:3.14 or -3.14, degree:180 or -180
    pixelAngleRounded = roundAngle(pixelAngle)

    #* Step 3: Application of Non-maxima suppression
    newEdgeGradient = nonMaximaSuppression(EdgeGradient, pixelAngleRounded)

    #* Uncomment these to see the result of non Maxima Suppression
    """plt.subplot(221),plt.imshow(pixelAngle, cmap = 'gray')
    plt.title('pixelAngle'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(pixelAngleRounded, cmap = 'gray')
    plt.title('pixelAngleRounded'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(EdgeGradient, cmap = 'gray')
    plt.title('EdgeGradient'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(newEdgeGradient, cmap = 'gray')
    plt.title('newEdgeGradient'), plt.xticks([]), plt.yticks([])
    plt.show()"""
    
    #* Step 4: hysteresis Thresholding
    EdgeGradient = cannyThreshold(newEdgeGradient, upperThreshold, lowerThreshold)

    return EdgeGradient


if __name__ == "__main__":
    pass

    


