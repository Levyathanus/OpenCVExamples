# Hough Transform:
# detect a shape if it is representable in a
# mathematical form: es. y = mx + c o x*cos(theta) + y*sin(theta) = r
# nello spazio mc al posto che xy (https://en.wikipedia.org/wiki/Hough_transform)
# Algorithm:
# 1) Edge detection (e.g. Canny edge detection)
# 2) Mapping of edge points to the Hough space and 
#    storage in an accumulator
# 3) Interpretation of the accumulator to yield lines
#    of infinite length. The interpretation is done by
#    thresholding and possibly other constraints
# 4) Conversion of infinite lines to finite lines

import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/sudoku.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) # rho = 1, theta = pi/180, threshold = 200

for line in lines:
    rho, theta = line[0]
    print(str(rho) + " " + str(theta))
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x0 * cos(theta) + y0 * sin(theta) = r
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow("Edges", edges)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()