import cv2, numpy as np
from matplotlib import pyplot as plt

#img = np.zeros((200,200), np.uint8)
#cv2.rectangle(img, (0,100), (200,200), (255,255,255), -1)
#cv2.rectangle(img, (0,50), (100,100), (127), -1)
img = cv2.imread('./opencv/samples/data/lena.jpg', 0)

#b, g, r = cv2.split(img)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
cv2.imshow("Image", img)
#cv2.imshow("B", b)
#cv2.imshow("G", g)
#cv2.imshow("R", r)

# hist(img.ravel(), maxval, range)
plt.hist(img.ravel(), 256, [0, 256]) # usando matplotlib
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()