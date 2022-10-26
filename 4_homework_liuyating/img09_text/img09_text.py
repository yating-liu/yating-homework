import cv2

img = cv2.imread("lena.jpeg")

img_putText = cv2.putText(img,"Hello, Lena!",(500,950),cv2.FONT_HERSHEY_COMPLEX,2,(255,191,0),2)


cv2.imshow("Image putText",img_putText)
cv2.imwrite('putText.jpg', img_putText)
cv2.waitKey(0)
