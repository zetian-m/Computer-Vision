import cv2 as cv
import numpy as np
def imageLighter(image, add_light):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            pixel_hell_temp = image[y,x]
            pixel_hell_temp += add_light
            if pixel_hell_temp > 255:
                pixel_hell_temp = 255
            image[y,x] = pixel_hell_temp

    return image

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