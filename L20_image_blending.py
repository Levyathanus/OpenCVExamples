import cv2, numpy as np

# Goal: blend (merge), half of the apple with half of the orange

apple = cv2.imread('./opencv/samples/data/apple.jpg')
orange = cv2.imread('./opencv/samples/data/orange.jpg')

print(apple.shape)
print(orange.shape)

# Metodo base (no blending): unisce le immagini come matrici (tupla)
apple_orange = np.hstack((apple[:,:256], orange[:,256:]))

# 1) Generate Gaussian pyramids
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# 2) Generate Laplacian pyramids
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)

# 3) Join the halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)], orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# 4) Reconstruction of the image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow('Apple_Orange', apple_orange)
cv2.imshow('Apple_Orange_Reconstruct', apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
