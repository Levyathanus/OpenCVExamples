import cv2, numpy as np

# Meanshift object tracking algorithm:
# 1) Take the first frame of the video
# 2) Setup initial window location
# 3) Setup the ROI for tracking
# 4) Setup the termination criteria, either 10 iterations or move by at least 1 point
cap = cv2.VideoCapture('slow_traffic.mp4')

# 1)
ret, frame = cap.read()
# 2)
x, y, width, height = 300, 200, 100, 50 # calcolato "a mano"
track_window = (x, y, width, height)
# 3) (histogram back-projected image)
ROI = frame[y:y+height, x:x+width]
hsv_ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_ROI, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
ROI_hist = cv2.calcHist([hsv_ROI], [0], mask, [180], [0, 180])
cv2.normalize(ROI_hist, ROI_hist, 0, 255, cv2.NORM_MINMAX) # normalizzare tra 0 e 255
# 4)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], ROI_hist, [0, 180], 1)
        # apply the meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
        x, y, w, h = track_window
        final_img = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
        cv2.imshow('Final Image', final_img)
        cv2.imshow('Dst', dst)
        
        #cv2.imshow('Video', frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
