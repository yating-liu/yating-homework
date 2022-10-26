import cv2

img = cv2.imread("lena.jpeg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Image gray",img_gray)

cv2.imwrite('gray.jpg', img_gray)
cv2.waitKey(0)
