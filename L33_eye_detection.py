import cv2

# classifiers già pronti in ./opencv/data/haarcascades

face_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)  # da webcam
while cap.isOpened():
    _, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        ROI_gray = img_gray[y:y+h, x:x+w]
        ROI_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(ROI_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(ROI_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
