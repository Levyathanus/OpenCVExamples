import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 175, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0]) # lista dei punti (tuple (x,y)) dei punti che compongono il primo contorno

# -1 disegna tutti i contorni ->
cv2.drawContours(img, contours, -1, (129,129,129), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()