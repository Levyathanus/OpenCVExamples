import cv2, numpy as np

cap = cv2.VideoCapture('./opencv/samples/data/vtest.avi')
# 3 Background Subtractor
#fg_bg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fg_bg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fg_bg = cv2.createBackgroundSubtractorKNN(detectShadows=False)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break
    fg_mask = fg_bg.apply(frame) # applicare il subtractor per la foreground mask
   
    cv2.imshow('Video', frame)
    cv2.imshow('FG MASK Frame', fg_mask)
    key = cv2.waitKey(30)
    if key == 27 or key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
