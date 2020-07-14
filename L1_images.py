#!/usr/bin/env python3

import cv2

# 0: grayscale
# 1: color
# -1: color with alpha
img = cv2.imread('lena.jpg', -1)
print(img) # if None: error!

cv2.imshow('image', img)

key = cv2.waitKey(0) # if 0: wait for the closing button

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena_copy.png', img) # write a new image
    cv2.destroyAllWindows()



