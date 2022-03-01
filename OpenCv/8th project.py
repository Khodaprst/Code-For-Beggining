from cv2 import CV_32F

import cv2
import numpy as np
#roshan kardan sfhe taarik

img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold= cv2.threshold(gray, 200, 15, cv2.THRESH_BINARY)
#th = cv2.adaptiveThreshold(manba'e, had aksar meghdar, method, no'e threshold, block size, destination)
th = cv2.adaptiveThreshold(gray, 355, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

cv2.imshow('orginal_img', img)
cv2.imshow('dark_img', threshold)
cv2.imshow('page', th)

cv2.waitKey(0)
cv2.destroyAllWindows()