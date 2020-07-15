#!/usr/bin/env python3

import numpy as np
import cv2

#img = cv2.imread('./opencv/samples/data/lena.jpg', 1)
img = np.zeros([512,512,3],np.uint8) # immagine nera con numpy

# disegnare una linea cv2.line(image,xy_start,xy_end,BGR_color,thickness)
img = cv2.line(img, (0,0), (255,255), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (0,0), (0,255), (255, 0, 0), 5)
# disegnare un rettangolo: top-left, bottom-right
# se thickness = -1 riempi la forma con il colore
img = cv2.rectangle(img, (384,0),(510,128),(0,0,255),5)
# disegnare un cerchio: centro, raggio
img = cv2.circle(img,(447,63),63,(0,255,0),-1)
# scrivere testo sull'immagine
font = cv2.FONT_HERSHEY_SIMPLEX # vedi altri font
img = cv2.putText(img,'OpenCV',(10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
