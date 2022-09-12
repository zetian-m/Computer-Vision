import cv2                          # open cv library 
import numpy as np                  # array, matrices  
import math                         # mathematical function
import matplotlib.pyplot as plt     # plot
import common as com    
import PointOperator as po




if __name__ == "__main__":

    # load image
    f = com.loadImage("Flower_interference.jpg")
    
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

    D0 = 100
    for u in range(P):
        for v in range(Q):
            D = np.sqrt((u-P/2)**2 + (v-Q/2)**2)
            if D <= D0:
                H[u, v] = 1
            else:
                H[u, v] = 0

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

    # filter in spatial domain
    H_unshifted = np.fft.ifftshift(H)
    h = np.real(np.fft.ifft2(H_unshifted))
    h = np.fft.fftshift(h)

    # intensity profile of center line 
    intstyProfile = h[int(P/2), :]

    plt.figure(1)
    plt.subplot(121),plt.imshow(f, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(Fshiftmag, cmap = 'gray')
    plt.title('Amplituden des Frequenzspektrums'), plt.xticks([]), plt.yticks([])


    plt.figure(2)
    ax = plt.subplot(121)
    plt.imshow(H, cmap = 'gray')
    plt.title('H[u, v]'), plt.xticks([]), plt.yticks([])
    ax.set_xlabel("u", fontsize=20, labelpad=1)
    ax.set_ylabel("v", fontsize=20, labelpad=1)
    plt.subplot(122),plt.imshow(G_shiftmag, cmap = 'gray')
    plt.title('G[u, v]'), plt.xticks([]), plt.yticks([])

    plt.figure(3)
    plt.subplot(121),plt.imshow(g, cmap = 'gray')
    plt.title('Gefiltertes Bild'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(h, cmap = 'gray')
    plt.title('Filter im Originalbereich'), plt.xticks([]), plt.yticks([])

    plt.figure(4)
    plt.subplot(111),plt.plot(np.linspace(0,Q,Q), intstyProfile)
    plt.title('Intensitätsprofil'), plt.xticks([]), plt.yticks([])
    plt.show()
    pass
"""    plt.figure(5)
    #plt.rcParams['font.size'] = '16'
    ax = plt.subplot(projection='3d')
    u = np.linspace(0, P, P)
    v = np.linspace(0, Q, Q)
    U, V = np.meshgrid(u, v)
    ax.plot_surface(U, V, H)
    ax.set_xlabel("u", fontsize=20, labelpad=1)
    ax.set_ylabel("v", fontsize=20, labelpad=1)
    ax.tick_params(axis='x', colors='white', labelsize=2)
    ax.tick_params(axis='y', colors='white', labelsize=2)
    ax.tick_params(axis='z', colors='white', labelsize=2)
    #ax.axes.xaxis.set_ticks([])
    #ax.axes.yaxis.set_ticks([])
    #ax.axes.zaxis.set_ticks([])
    ax.grid(True)
    ax.set_zlabel("H[u,v]", fontsize=20, labelpad=1)"""