import cv2
import numpy as np

#img = cv2.imread('./opencv/samples/data/sudoku.png')
img = cv2.imread('road.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)
# rho = 1, theta = pi/180, threshold = 100
# linee < 100 di lunghezza sono scartate
# un gap <= 10 tra segmenti li fa unire come singola linea
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Edges", edges)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
