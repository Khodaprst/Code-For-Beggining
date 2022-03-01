import cv2
import numpy as np

img = cv2.imread('image2.jpg', cv2.IMREAD_COLOR)

prt1 = img[100:200, 100:200]

img[300:400, 300:400] = prt1 


cv2.imshow('image2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()