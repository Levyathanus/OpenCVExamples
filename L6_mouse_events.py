import cv2, numpy as np

# [i for i in dir(cv2)]: tutte le classi e le funzioni del pacchetto cv2
# events = [i for i in dir(cv2) if 'EVENT' in i] 
# print(events)
def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + ', ' + str(y)
        print(strXY)
        cv2.putText(img, strXY, (x,y), font, .5, (255,100,0), 2)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # stampo i canali BGR del punto cliccato
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (255, 100, 125), 2)
        cv2.imshow('image', img)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('./opencv/samples/data/lena.jpg')
cv2.imshow('image', img)

# nomi delle immagini uguali dappertutto
# settare la funzione che gestisce il mouse
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0) # aspetta tasto esc
cv2.destroyAllWindows()
