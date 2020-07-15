import cv2
import numpy as np

# visualizzo colore di un punto su un'altra finestra
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        mycolor_image = np.zeros((512,512,3), np.uint8)
        # riempio l'immagine nera con i canali BGR
        mycolor_image[:] = [blue, green, red]
        cv2.imshow('color', mycolor_image)
        #cv2.imshow('image', img)


#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('./opencv/samples/data/lena.jpg')
cv2.imshow('image', img)

# nomi della stessa immagine uguale dappertutto
# settare la funzione che gestisce il mouse
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)  # aspetta tasto esc
cv2.destroyAllWindows()
