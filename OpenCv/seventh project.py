import cv2
import numpy as np

img = cv2.imread('imag.jpg')
img2 = cv2.imread('imag1.jpg')

rows, cols, channels = img2.shape
roi = img[0:rows, 0:cols]

#sefid, siah va baghi rang ha, sefid
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask= cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)

#gheir az sefid, baghi rang ha siah.
mask_inv = cv2.bitwise_not(mask)

#ba backgound kari nadarad va jelo siah ast
background = cv2.bitwise_and(roi, roi, mask = mask)

#logo ro kari nadare va background ro taghir mide
foreground = cv2.bitwise_and(img2, img2, mask = mask_inv)

#tarkibi
dst = cv2.add(background, foreground)
img[0:rows, 0:cols] = dst

#cv2.imshow('imag', img1)
#cv2.imshow('imag1', img2)
#cv2.imshow('image', add)
#cv2.imshow('img1bg', background)
#cv2.imshow('img2bg', foreground)

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()