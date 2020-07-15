import cv2
import numpy as np


def nothing(x):
    print(x)


cv2.namedWindow('image')  # creazione di una finestra con nome

# creazione trackbar (nome, nome_finestra, valore_iniziale, valore_finale, callback_function)
cv2.createTrackbar('CP', 'image', 10, 400, nothing)

# trackbar "interruttore"
switch = 'colored/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(True):
    img = cv2.imread('./opencv/samples/data/lena.jpg')
    pos = cv2.getTrackbarPos('CP', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50,150), font, 4, (0,0,255))
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.imshow('image', img)

cv2.destroyAllWindows()
