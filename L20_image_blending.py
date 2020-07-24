import cv2, numpy as np

apple = cv2.imread('./opencv/samples/data/apple.jpg')
orange = cv2.imread('./opencv/samples/data/orange.jpg')

print(apple.shape)
print(orange.shape)


cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.waitKey(0)
cv2.destroyAllWindows()