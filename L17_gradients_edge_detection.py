import cv2, numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('./opencv/samples/data/messi5.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('./opencv/samples/data/sudoku.png', cv2.IMREAD_GRAYSCALE)

# Laplacian(img, dataType(64 bit float), kernel_size(ksize))
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3) # trova i contorni
lap = np.uint8(np.absolute(lap)) # conversione a uint8

# Sobel(img, dataType, bool(dx), bool(dy), kernel_size)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel_combined = cv2.bitwise_or(sobelX, sobelY)


titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined']
images = [img, lap, sobelX, sobelY, sobel_combined]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()