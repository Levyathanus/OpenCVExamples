import cv2, numpy as np

# vedi introduzione su HSV colorspace

def nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('L_HUE', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('L_SAT', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('L_VAL', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('U_HUE', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('U_SAT', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('U_VAL', 'Tracking', 255, 255, nothing)


while(True):
    frame = cv2.imread('./opencv/samples/data/smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_hue = cv2.getTrackbarPos('L_HUE', 'Tracking')
    l_sat = cv2.getTrackbarPos('L_SAT', 'Tracking')
    l_val = cv2.getTrackbarPos('L_VAL', 'Tracking')
    u_hue = cv2.getTrackbarPos('U_HUE', 'Tracking')
    u_sat = cv2.getTrackbarPos('U_SAT', 'Tracking')
    u_val = cv2.getTrackbarPos('U_VAL', 'Tracking')

    # trovare gli smarties del colore nel range selezionato
    l_b = np.array([l_hue,l_sat,l_val]) # lower_bound: color range
    u_b = np.array([u_hue,u_sat,u_val]) # upper_bound: color range
    mask = cv2.inRange(hsv, l_b, u_b) # maschera
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('hsv', hsv)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()
