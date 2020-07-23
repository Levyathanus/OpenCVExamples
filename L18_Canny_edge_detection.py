import cv2, numpy as np
from matplotlib import pyplot as plt

# Canny edge detection algorithm:
# 1) Noise reduction (Gaussian filter)
# 2) Gradient calculation
# 3) Non-maximum suppression
# 4) Double threshold
# 5) Edge tracking by histeresis

img = cv2.imread('./opencv/samples/data/messi5.jpg', 0)



titles = ['image']
images = [img]

for i in range(len(images)):
    plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
