import cv2
import numpy as np
#filter kardan rang dar doorbin

cam = cv2.VideoCapture(0)

while(True):
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_color = np.array([50, 100, 50])
    upper_color = np.array([255, 255, 230])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('camera', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('khoruji', res)

    if (cv2.waitKey(5) & 0xFF) == 27:
        break

cv2.destroyAllWindows()()
cam.release()