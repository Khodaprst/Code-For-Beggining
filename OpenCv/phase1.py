import cv2
import numpy as np

def read(path, mode=-1):
    return cv2.imread(path, mode)


img = read('image.jpg')


def show(img):

    cv2.imshow('image.jpg', img)
    while(True):
        key = cv2.waitKey(0)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


#show(img)
show(read('image.jpg', 1))