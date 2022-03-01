import cv2
import numpy as np

read = cv2.imread('image.jpg')
cnv = cv2.cvtColor(read, cv2.COLOR_BGR2HSV)

stack = np.hstack((read, cnv))
cv2.imshow('stack', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow('crysis2', cv2.window_)