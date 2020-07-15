import cv2, numpy as np

img = cv2.imread('./opencv/samples/data/messi5.jpg')
img2 = cv2.imread('./opencv/samples/data/opencv-logo.png')

print(img.shape) # returns a tuple of number of rows, columns and channels
print(img.size) # returns the total number of pixels accessed
print(img.dtype) # returns the image datatype

b, g, r = cv2.split(img) # metodo veloce per dividere i canali BGR
img = cv2.merge((b,g,r)) # unisco i canali BGR per formare un'immagine
# ogni canale è di tipo uint8 (unsigned int a 8 bit (0 - 255))

# ROI: Region Of Interest dell'immagine
# coordinate della palla nell'immagine
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img2 = cv2.resize(img2, (img.shape[0],img.shape[1]))

dst = cv2.add(img, img2) # somma due vettori (matrici/immagini) o un vettore e uno scalare

#cv2.imshow('image', img)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
