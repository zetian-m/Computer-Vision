import cv2 as cv
import numpy as np



def imageLighter(image, add_light):
    newImg = np.zeros(image.shape)
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            pixelValue = image[r,c]
            pixelValue += add_light
            if pixelValue > 255:
                pixelValue = 255
            newImg[r,c] = pixelValue

    return newImg

def imageDarker(image, darker):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            pixel_hell_temp = image[y,x]
            pixel_hell_temp -= darker
            if pixel_hell_temp < 0:
                pixel_hell_temp = 0
            image[y,x] = pixel_hell_temp

    return image

def imageKontrass(image, kontrassFactor):
    for x in range(0, image.shape[0]):
        for y in range(0, image.shape[1]):
            pixelValue = image.item((x,y))
            pixelValue *= kontrassFactor
            if pixelValue < 0:
                pixelValue = 0
            if pixelValue > 255:
                pixelValue = 255
            image[x,y] = pixelValue

    return image

def main():
    pass
    

if __name__ == "__main__":
    main()