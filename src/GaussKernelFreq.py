import cv2                          # open cv library 
import numpy as np                  # array, matrices  
import math                         # mathematical function
import matplotlib.pyplot as plt     # plot
import GaussFilter as GF
import common as com    
import PointOperator as po




if __name__ == "__main__":

    # load kernel
    f = GF.creatGaussKernel(41, 1)
    
    # image size
    M, N = f.shape

    # new image size with zero padding
    P = 2 * M
    Q = 2 * N

    # perform fft (was ist mit 2^n für FFT?)
    F = np.fft.fft2(f, s=[P, Q])

    # shift dc value to the middle, i.e. [P/2, Q/2]
    F_shift = np.fft.fftshift(F)

    # calc magnitude of frequency, log transformation log(1+r)
    Fshiftmag = np.log1p(np.abs(F_shift))

    # create ideal low pass filter
    H = np.zeros((P, Q), dtype=np.float32)

    D0 = 80
    for u in range(P):
        for v in range(Q):
            D = np.sqrt((u-P/2)**2 + (v-Q/2)**2)
            H[u, v] = math.exp(-(D**2)/(2*D0**2))


    # apply low pass filter
    G_shift = F_shift * H

    # calc magnitude of frequency, log transformation log(1+r)
    G_shiftmag = np.log1p(np.abs(G_shift))

    # shift dc value back to index 0
    G = np.fft.ifftshift(G_shift)

    # iDFT
    g_p = np.real(np.fft.ifft2(G))

    # remove padding
    g = g_p[0:M, 0:N]

    plt.figure(1)
    plt.subplot(121),plt.imshow(f, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(Fshiftmag, cmap = 'gray')
    plt.title('Amplituden des Frequenzspektrums'), plt.xticks([]), plt.yticks([])
    plt.show(),

    plt.figure(2)
    plt.subplot(121),plt.imshow(H, cmap = 'gray')
    plt.title('H[u, v]'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(G_shiftmag, cmap = 'gray')
    plt.title('G[u, v]'), plt.xticks([]), plt.yticks([])

    plt.figure(3)
    plt.subplot(111),plt.imshow(g, cmap = 'gray')
    plt.title('Gefiltertes Bild'), plt.xticks([]), plt.yticks([])
    plt.show()

    plt.figure(4)
    ax = plt.subplot(projection='3d')
    u = np.linspace(0, M, N)
    v = np.linspace(0, N, N)
    U, V = np.meshgrid(u, v)
    ax.plot_surface(U, V, f)
    ax.set_xlabel("u")
    ax.set_ylabel("v")
    ax.set_zlabel("H[u,v]")
    plt.show()


    pass