# Corners: large variations in intensity
# in both X and Y directions
# Harris Corner Detector:
# 1) Determine which windows produce very large
#    variations in intensity when moved in both
#    X and Y directions
# 2) With each window found, a score R is computed
#    R = det(M) - k*(trace(M))^2, det(M) = lambda1 * lambda2
#    trace(M) = lambda1 + lambda2
# 3) After applying a threshold to R, important corners
#    are selected and marked:
#    If |R| is small (lambda1, lambda2 small), the region is flat
#    If R < 0 (lambda1/2 >> lambda2/1), the region is an edge
#    If R is large (lamda1, lambda2 large and similar), the region is a corner

import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/chessboard.png')
img = cv2.resize(img, (3723//8, 3595//8))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = np.float32(img_gray)
# cornerHarris(img_gray_float32, blockSize: neighbourhood for corner detection, ksize: aperture parameter Sobel
# derivative, k: free parameter)
dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255] # mark the corners with red color

cv2.imshow('Image', img)
cv2.imshow('Dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()