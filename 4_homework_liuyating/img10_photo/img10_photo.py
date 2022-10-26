import cv2
import numpy as np

img = cv2.imread("image.png")
#cv2.imshow('Image show', img)
#cv2.waitKey(0)


shape = img.shape
height = shape[0]
width = shape[1]

chager_color = np.zeros((height, width, 3), np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b >247 and g>247 and r>247:
            img[i, j] = (237,149,100)
        chager_color[i, j] = img[i, j]
    cv2.imwrite('lyt.png', chager_color)
