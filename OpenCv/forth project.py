import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #cv2.line(frame, (100, 100), (200, 400), (0, 255, 0), 1)
    #cv2.rectangle(frame, (100, 200), (200, 300), (0, 0, 255), 5)
    #cv2.circle(frame, (300, 200), 70, (120, 0, 50),3)
    
    #pts = np.array([[50, 120], [120, 200], [220, 100], [400, 20]])
    #cv2.polylines(frame, [pts], True, (60, 40, 20), 6, )

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, 'Hello World!', (100, 100), font, 1, (100, 0, 0), 1)


    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
