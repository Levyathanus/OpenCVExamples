import cv2
import numpy as np
from matplotlib import pyplot as plt


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  # matrice di 0 con dimensioni come img
    #channel_count = img.shape[2]
    match_mask_color = 255  # maschero con il nero
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img


def draw_lines(img, lines):
    new_img = np.copy(img)
    blank_img = np.zeros(
        (new_img.shape[0], new_img.shape[1], new_img.shape[2]), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_img, (x1, y1), (x2, y2), (0, 0, 255), thickness=3)
    img = cv2.addWeighted(new_img, 0.8, blank_img, 1, 0.0)
    return img

def process(img):
    height = img.shape[0]
    width = img.shape[1]

    # define a ROI (Region Of Interest)
    ROI_vertices = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]

    # Canny edge detection before masking
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_img = cv2.Canny(gray_img, 100, 200)

    # masking the ROI
    masked_img = region_of_interest(canny_img, np.array([ROI_vertices], np.int32))

    # probabilistic Hough line transform
    lines = cv2.HoughLinesP(masked_img, rho=6, theta=np.pi/60, threshold=160,
                            lines=np.array([]), minLineLength=40, maxLineGap=25)
    line_img = draw_lines(img, lines)
    return line_img

cap = cv2.VideoCapture('test.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = process(frame)
        cv2.imshow(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()