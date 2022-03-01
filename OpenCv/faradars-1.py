import cv2
pic = cv2.imread('image1.jpg')
pic1 = cv2.imread('image1.jpg', 1)
pic2 = cv2.imread('image1.jpg', 0)

#cv2.WINDOW_AUTOSIZE
cv2.namedWindow('image_autosize', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image_autosize', pic)

#cv2.WINDOW_NORMAL
cv2.namedWindow('image_window_normal', cv2.WINDOW_NORMAL)
cv2.imshow('image_window_normal', pic)

#cv2.imshow('pic1', pic)
#cv2.imshow('pic2', pic1)
#cv2.imshow('pic3', pic2)


cv2.waitKey(0)
cv2.destroyAllWindows()