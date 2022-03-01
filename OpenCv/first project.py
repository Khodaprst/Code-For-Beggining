import cv2
import numpy as np
from matplotlib import pyplot as pt

img = cv2.imread('image.jpg', 0)
cv2.imshow('image', img)

pt.imshow(img, cmap='gray', interpolation='bicubic')
pt.plot([100, 200], [370, 200], 'blue', linewidth = 5 )
pt.show()

cv2.imwrite('imgout.jpg', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()