import cv2

#zakhire file ba format delkhah

pic = cv2.imread('image1.jpg')
pic1 = cv2.imread('image1.jpg', 1)
pic2 = cv2.imread('image1.jpg', 0)

cv2.imwrite('image.png', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()