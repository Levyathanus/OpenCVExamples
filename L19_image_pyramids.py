import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/lena.jpg')

# (Gaussian) pyrDown(img): riduce la risoluzione dell'immagine
# (Gaussian) pyrUp(img): aumenta la risoluzione dell'immagine
#lower_resolution_1 = cv2.pyrDown(img)
#lower_resolution_2 = cv2.pyrDown(lower_resolution_1)
#higher_resolution_1 = cv2.pyrUp(lower_resolution_2)

layer = img.copy()
gaussian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    #cv2.imshow(str(i), layer)

layer = gaussian_pyramid[-1]
cv2.imshow('Upper level Gaussian pyramid', layer)
laplacian_pyramid = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid[i])
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original Image', img)
#cv2.imshow('pyrDown 1 Image', lower_resolution_1)
#cv2.imshow('pyrDown 2 Image', lower_resolution_2)
#cv2.imshow('pyrUp 1 Image', higher_resolution_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
