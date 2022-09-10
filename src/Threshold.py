import numpy as np

def threshold(img, upperThreshold, lowerThreshold, thMethod=1):
    numRows, numCols = img.shape
    imgThreshold = img.copy()

    #* Pixelvalue >= Threshold -> 255
    #* Pixelvalue = Pixelvalue
    if thMethod == 1:
        for r in range(0, numRows):
            for c in range(0, numCols):
                if img[r,c] > upperThreshold:
                    imgThreshold[r, c] = 255
                else:
                    continue

    #* Binary Threshold
    elif thMethod == 2:
        for r in range(0, numRows):
            for c in range(0, numCols):
                if img[r,c] > upperThreshold:
                    imgThreshold[r,c] = 255
                else:
                    imgThreshold[r,c] = 0

    elif thMethod == 3:
        for r in range(0, numRows):
            for c in range(0, numCols):
                if img[r,c] < lowerThreshold:
                    imgThreshold[r,c] = 0
                else:
                    continue
    
    return imgThreshold
