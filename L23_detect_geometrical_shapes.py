import cv2, numpy as np

img = cv2.imread('shapes.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx_polygon = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx_polygon], 0, (0,255,0), 3)
    x = approx_polygon.ravel()[0] # coordinate del poligono
    y = approx_polygon.ravel()[1]
    if len(approx_polygon) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx_polygon) == 4:
        x, y, w, h = cv2.boundingRect(approx_polygon)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
        else: 
            cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx_polygon) == 5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx_polygon) == 6:
        cv2.putText(img, "Hexagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx_polygon) == 7:
        cv2.putText(img, "Heptagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx_polygon) == 8:
        cv2.putText(img, "Octagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))

# TODO: controllare errore esagono

cv2.imshow('Thresh', thresh)
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()