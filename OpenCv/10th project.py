import cv2
import numpy as np
#tashkhis labeh - laplacian
#tamarkoz namayesh mehvar - sobel

cap = cv2.VideoCapture(0)

while(True):
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_8U)
    sobely = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize= 5)
    sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize= 5)
    sobel1 = cv2.Sobel(frame, cv2.CV_8U, 1, 1, ksize= 5)
    canny = cv2.Canny(frame, 100, 200)

    cv2.imshow('windows', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('canny', canny)
    cv2.imshow('sobl1', sobel1)

    k = cv2.waitKey(5) & 0xFF
    if (k==27):
        break

cv2.destroyAllWindows()
cap.release()