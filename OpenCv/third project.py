import cv2
import numpy as np
#return gray video
cap = cv2.VideoCapture(0)
#forever:
while(True):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #khat
    cv2.line(frame, (100, 100), (200, 400), (0, 255, 0), 1)
    #mostatil
    cv2.rectangle(frame, (100, 200), (200, 300), (0, 0, 255), 5)
    #name of camera
    cv2.imshow('webcam', frame)
    #closing camera
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
#showing camera
cap.release()
cv2.destroyAllWindows()