import cv2

img = cv2.imread("lena.jpeg")

img_resize_smaller = cv2.resize(img,(500,500))

cv2.imshow("Image Resize smaller",img_resize_smaller)

cv2.imwrite('smaller.jpg', img_resize_smaller)
cv2.waitKey(0)
