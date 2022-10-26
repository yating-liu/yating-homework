import cv2

img = cv2.imread("lena.jpeg")
cv2.imshow('Image show', img)
cv2.waitKey(0)
