import cv2, numpy as np
from matplotlib import pyplot as plt

# morphological trasformations: simple operation based on the image shape
# they are normally performed in binary images
# the kernel tells u how to change the value of a pixel
# combining it with different amounts of the nearby pixels

img = cv2.imread('./opencv/samples/data/smarties.png', cv2.IMREAD_GRAYSCALE) # 0
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# 2x2 square shape
kernel = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kernel, iterations = 2) # dilatazione(mask, kernel, iterations)
erosion = cv2.erode(mask, kernel, iterations = 1) # erosione(mask, kernel, iterations)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # funzione per una trasformazione generale
# morphologyEx(mask, trasformazione, kernel), opening = erosion -> dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # closing = dilation -> erosion
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
# vedi altre morphological trasformations

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, gradient, tophat]

for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
