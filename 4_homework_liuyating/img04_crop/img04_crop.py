import cv2

img = cv2.imread("lena.jpeg")

img_crop = img[360:720, 360:720]

cv2.imshow("Image crop",img_crop)
cv2.imwrite('crop.jpg', img_crop)
cv2.waitKey(0)
