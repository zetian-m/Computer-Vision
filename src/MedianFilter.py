import common as CO
import numpy as np




def medianFilter(image, kernelSize, convMethod=1):
    imgRows, imgCols = image.shape

    extentionRows = int((kernelSize-1)/2)
    extentionCols = extentionRows
    newImg = np.zeros(image.shape)
    image = np.pad(image, [(extentionRows, ),(extentionCols, )], mode='constant', constant_values=0)

    
    for r in range(0, imgRows):
        for c in range(0, imgCols):
            medianValue = np.median(image[r:r+kernelSize, c:c+kernelSize])
            newImg[r,c] = medianValue

    return newImg


if __name__ == "__main__":
    pass