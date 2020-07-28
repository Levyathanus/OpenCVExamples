import cv2

# classifiers già pronti in ./opencv/data/haarcascades

face_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('face_test.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)



cv2.imshow('Image', img)
cv2.waitKey(0)