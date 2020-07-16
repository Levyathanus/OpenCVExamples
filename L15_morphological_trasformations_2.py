import cv2
import numpy as np
from matplotlib import pyplot as plt

# morphological trasformations: simple operation based on the image shape
# they are normally performed in binary images
# the kernel tells u how to change the value of a pixel
# combining it with different amounts of the nearby pixels

img = cv2.imread('./opencv/samples/data/LinuxLogo.jpg', cv2.IMREAD_GRAYSCALE)  # 0

# 2x2 square shape
kernel = np.ones((2, 2), np.uint8)

# dilatazione(mask, kernel, iterations)
dilation = cv2.dilate(img, kernel, iterations=2)
# erosione(mask, kernel, iterations)
erosion = cv2.erode(img, kernel, iterations=1)
# funzione per una trasformazione generale
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# morphologyEx(mask, trasformazione, kernel), opening = erosion -> dilation
# closing = dilation -> erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# vedi altre morphological trasformations

titles = ['image', 'mask', 'dilation', 'erosion',
          'opening', 'closing', 'gradient', 'tophat']
images = [img, img, dilation, erosion, opening, closing, gradient, tophat]

for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
