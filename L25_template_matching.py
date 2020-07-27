import cv2, numpy as np

# search a template image inside a larger image
img = cv2.imread('./opencv/samples/data/messi5.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi_face.jpg', 0)

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# il valore più vicino a 1 indica il punto dell'immagine dove l'origine del template
# (angolo alto sinistra) va posizionata per la miglior corrispondenza 
print(res)
threshold = 0.95
loc = np.where(res >= threshold)
print(loc) # (65, 209)

w, h = template.shape[::-1]
for pt in zip(*loc[::-1]): # zip(*) unzip the iterable
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h), (0,0,255), 2)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()