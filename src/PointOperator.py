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
    original_image = cv.imread("Lena.bmp", cv.IMREAD_GRAYSCALE)
    cv.imshow("original", original_image)
    cv.imshow("lighter", image_lighter(original_image, 100))
    cv.imshow("darker", image_darker(original_image, 150))
    cv.imshow("contrtass schlechter", image_kontrass(original_image, 0.5))
    cv.imshow("contrtass besser", image_kontrass(original_image, 2))

    cv.waitKey()
    

if __name__ == "__main__":
    main()