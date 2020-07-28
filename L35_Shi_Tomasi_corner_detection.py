import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/pic1.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# goodFeaturesToTrack(img_gray, numOfCorners, minimum qualityLevel for the corner, minimum distance)
corners = cv2.goodFeaturesToTrack(img_gray, 50, 0.01, 10)
corners = np.int0(corners) # equivalente a corners = np.int64(corners)

for corner in corners:
    x, y = corner.ravel()  # https://numpy.org/doc/stable/reference/generated/numpy.ravel.html
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
