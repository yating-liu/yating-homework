import cv2

img = cv2.imread("lena.jpeg")

img_resize_larger = cv2.resize(img,(1200,1200))

cv2.imshow("Image Resize larger",img_resize_larger)
cv2.imwrite('larger.jpg', img_resize_larger)
cv2.waitKey(0)
