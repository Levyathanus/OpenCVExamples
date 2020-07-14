#!/usr/bin/env python3

import cv2

#cv2.VideoCapture('my_video_file.mp4')
cap = cv2.VideoCapture(0) # 0 -> default camera
fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc video code
# anche fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fps = 20.0
resolution = (640,480)
out = cv2.VideoWriter('output.avi', fourcc, fps, resolution)
# print(cap.isOpened()) True se tutto ok

while(cap.isOpened()):
    ret, frame = cap.read() # ret == True frame è disponibile
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # guarda cv2 documentation per
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # per tutte le proprietà

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'): # q per uscire
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
