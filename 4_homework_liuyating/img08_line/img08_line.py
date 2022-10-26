import cv2

img = cv2.imread("lena.jpeg")

img_line = cv2.line(img,(200,950),(800,950),(255,191,0),3)

cv2.imshow("Image line",img_line)
cv2.imwrite('line.jpg', img_line)
cv2.waitKey(0)
