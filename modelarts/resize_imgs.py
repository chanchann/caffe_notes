import cv2
import numpy as np
path = '/Users/frank/Desktop/test1.jpg'
crop_size = (28, 28)
img = cv2.imread(path)
img_new = cv2.resize(img, crop_size, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('/Users/frank/Desktop/test2.jpg', img)


