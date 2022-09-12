import GaussFilter as GASF
import numpy as np

def Illuminate(image, kernelSize, factor):
    

    gaussKernel, bluredImg = GASF.gaussFilter(image, kernelSize, 1, convMethod=1)

    newImg = np.ones(bluredImg.shape)
    val = 127*newImg

    newImg = np.rint((val - bluredImg) * factor + image)

    return newImg

if __name__ == "__main__":
    pass
    

    

    