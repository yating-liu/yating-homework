import cv2

img = cv2.imread("image.png")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b < 92 and g < 92 and r > 167:
            img[i, j] = (237,149,100)
    cv2.imwrite('yy.png', img)
