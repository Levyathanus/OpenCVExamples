import cv2, numpy as np
from matplotlib import pyplot as plt

# Canny edge detection algorithm:
# 1) Noise reduction (Gaussian filter)
# 2) Gradient calculation
# 3) Non-maximum suppression
# 4) Double threshold
# 5) Edge tracking by histeresis

def nothing(x):
    pass

img = cv2.imread('./opencv/samples/data/messi5.jpg', 0)
cv2.namedWindow('Edges')


# Canny(img, threshold1, threshold2)
#canny = cv2.Canny(img, 100, 200)

# trackbar for threshold1 and threshold2
cv2.createTrackbar('TH1', 'Edges', 0, 255, nothing)
cv2.createTrackbar('TH2', 'Edges', 0, 255, nothing)

while(True):
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    th1 = cv2.getTrackbarPos('TH1', 'Edges')
    th2 = cv2.getTrackbarPos('TH2', 'Edges')
    canny = cv2.Canny(img, th1, th2)
    cv2.imshow('Canny', canny)

#titles = ['image', 'Canny']
#images = [img, canny]

#for i in range(len(images)):
#    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
#    plt.title(titles[i])
#    plt.xticks([]), plt.yticks([])

#plt.show()

cv2.destroyAllWindows()
