import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./opencv/samples/data/lena.jpg', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# matplotlib usa immagini in formato RGB (non BGR)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

# titles = ['title1', 'title2', ...]
# images = [img1, img2, ...]
########### subplot ############
# for i in range(0, len(images)):
#   plt.subplot(rows, columns, i), plt.imshow(images[i], 'gray')
#   plt.title(titles[i])
#   plt.xticks([]), plt.yticks([])
#  plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()