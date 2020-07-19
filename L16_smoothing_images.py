import cv2, numpy as np
from matplotlib import pyplot as plt

# smoothing or bluring for denoising
# various types of filters: homogeneous, gaussian, median...

#img = cv2.imread('./opencv/samples/data/opencv-logo.png')
img = cv2.imread('eye.jpg')
#img = cv2.imread('water.png')
#img = cv2.imread('./opencv/samples/data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25 # vedi formula del kernel per il filtro omogeneo
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5)) # averaging algorithm
gaussian_blur = cv2.GaussianBlur(img, (5,5), 0) # for high frequency noise
median_blur = cv2.medianBlur(img, 5) # for salt-and-pepper noise
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75) # denoising preserving the edges

titles = ['image', '2D convolution', 'blur', 'gaussian blur', 'median blur', 'bilateral filter']
images = [img, dst, blur, gaussian_blur, median_blur, bilateral_filter]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
