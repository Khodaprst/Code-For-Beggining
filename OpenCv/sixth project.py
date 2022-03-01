import cv2
import numpy as np

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

#add = img1 + img2
#add = cv2.add(img1, img2)
add = cv2.addWeighted(img1, 0.7, img2, 0.5, 0)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('add', add)

cv2.waitKey(0)
cv2.destroyAllWindows()