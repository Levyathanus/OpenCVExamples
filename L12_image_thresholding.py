import cv2, numpy as np

# Thresholding: tecnica di segmentazione che confronta
# pixel per pixel l'immagine con una soglia per staccare
# il soggetto dallo sfondo

img = cv2.imread('./opencv/samples/data/gradient.png', 0)
# threshold(img, soglia, max_val, tipo)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # se valore del pixel < soglia -> 0, altrimenti -> max_val
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # se valore del pixel < soglia -> max_val, altrimenti -> 0
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # se valore del pixel > soglia -> soglia, altrimenti invariato
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # se valore del pixel < soglia -> 0, altrimenti invariato
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # se valore del pixel > soglia -> 0, altrimenti invariato

cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()