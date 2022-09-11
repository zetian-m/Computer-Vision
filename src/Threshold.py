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
        imgThreshold = np.zeros(img.shape)
        row_max, col_max = np.where(img > upperThreshold)
        imgThreshold[row_max, col_max] = 255
        
                
    #* Pixelvalue < lowerThreshold -> 0
    #* Pixelvalue = Pixelvalue
    elif thMethod == 3:

        row_max, col_max = np.where(img < lowerThreshold)
        imgThreshold[row_max, col_max] = 0

    elif thMethod == 4:
        row_max, col_max = np.where(img < lowerThreshold)
        imgThreshold[row_max, col_max] = 0
        row_max, col_max = np.where(img > upperThreshold)
        imgThreshold[row_max, col_max] = 0
    
    return imgThreshold
