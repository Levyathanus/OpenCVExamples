import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/smarties.png')
output = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.medianBlur(img_gray, 5)
circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=35)

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x,y), r, (255,0,255), 3)
    cv2.circle(output, (x,y), 2, (0,255,255), 3) # punto per il centro

cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
