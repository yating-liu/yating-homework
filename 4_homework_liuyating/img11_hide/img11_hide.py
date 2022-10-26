

import cv2
import numpy as np


img = cv2.imread('t2.png')
shape = img.shape

height = shape[0]
width = shape[1]
hide = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        b, g, r = img[i, j]
        if b < 251 and g < 251 and r < 251:
            #read_color =  (r, g, b)
            #print(read_color)
            img[i, j] = (254, 254, 254)
        hide[i, j] = img[i, j]
    cv2.imwrite('test3.png', hide)

