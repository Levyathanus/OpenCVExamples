import cv2, numpy as np

def nothing(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image') # creazione di una finestra con nome

# creazione trackbar (nome, nome_finestra, valore_iniziale, valore_finale, callback_function)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

# trackbar "interruttore"
switch = '0: OFF\n 1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(True):
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    # getTrackbarPosition: (nome_trackbar, nome_window)
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        # riempimento dell'immagine con i 3 canali (monocromatica)
        img[:] = [b, g, r]
cv2.destroyAllWindows()
