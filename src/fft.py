import cv2                          # open cv library 
import numpy as np                  # array, matrices  
import math                         # mathematical function
import matplotlib.pyplot as plt     # plot
import common as com    
import PointOperator as po




if __name__ == "__main__":

    img = com.loadImage('Picture_Crossing_noise_0_pixelCnt_128_featureCnt_5.bmp')
    po.imageLighter(img, 1)

    dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    #magnitude_spectrum = cv2.magnitude(dft[:,:,0],dft[:,:,1])
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    pass