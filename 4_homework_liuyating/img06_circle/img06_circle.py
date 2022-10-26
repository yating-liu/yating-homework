import cv2

img = cv2.imread("lena.jpeg")

img_circle = cv2.circle(img,(360,360),100,(255,191,0),2)

cv2.imshow("Image circle",img_circle)


cv2.imwrite('circle.jpg', img_circle)
cv2.waitKey(0)
