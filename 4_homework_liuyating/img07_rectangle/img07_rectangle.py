import cv2

img = cv2.imread("lena.jpeg")

img_rectangle = cv2.rectangle(img,(540,500),(200,360),(255,191,0),2)

cv2.imshow("Image rectangle",img_rectangle)

cv2.imwrite('rectangle.jpg', img_rectangle)
cv2.waitKey(0)
