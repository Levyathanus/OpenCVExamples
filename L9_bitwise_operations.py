import cv2, numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread('image_1.png') 
img2 = cv2.resize(img2, (img1.shape[1],img1.shape[0]))

bit_and = cv2.bitwise_and(img2, img1) # and logico tra immagini (nero: 0, bianco: 1)
bit_or = cv2.bitwise_or(img2, img1) # or logico tra immagini (nero: 0, bianco: 1)
bit_xor = cv2.bitwise_xor(img2, img1) # xor logico tra immagini (nero: 0, bianco: 1) (1 quando sono diversi)
bit_not1 = cv2.bitwise_not(img1) # not logico per img1 (nero: 0, bianco: 1)
bit_not2 = cv2.bitwise_not(img2) # not logico per img2 (nero: 0, bianco: 1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bit_and', bit_and)
cv2.imshow('bit_or', bit_or)
cv2.imshow('bit_xor', bit_xor)
cv2.imshow('bit_not1', bit_not1)
cv2.imshow('bit_not2', bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()
