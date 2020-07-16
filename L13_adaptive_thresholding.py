import cv2, numpy as np

# threshold value calcolato per ogni piccola regione (block)
# dell'immagine (thresholding adattivo)

img = cv2.imread('./opencv/samples/data/sudoku.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# adaptiveThreshold(img, max_value, adaptive_method, type, block_size, subtractive_constant_C)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
