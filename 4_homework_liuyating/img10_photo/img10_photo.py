import cv2

img = cv2.imread("bjt.jpg")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b > 190 and g > 140 and r < 111:
            img[i, j] = (255,255,240)
    cv2.imwrite('bjt1.jpg', img)
