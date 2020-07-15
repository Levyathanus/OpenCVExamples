import cv2
import numpy as np

# connetto i punti segnati con il mouse con una linea
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # disegno un punto pieno (thickness = -1)
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            # collego gli ultimi due punti
            cv2.line(img, points[-1], points[-2], (255,200,100), 5)
        cv2.imshow('image', img)
    
img = np.zeros((512,512,3), np.uint8)
#img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

# vettore delle tuple (coordinate dei punti)
points = []

# nomi delle immagini uguali dappertutto
# settare la funzione che gestisce il mouse
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)  # aspetta tasto esc
cv2.destroyAllWindows()
