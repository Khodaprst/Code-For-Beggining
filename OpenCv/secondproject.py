import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 24.0, (640, 480))

while(True):
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, 1)
    out.write(frame)


    cv2.imshow('webcam', color)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows() 