import cv2

img = cv2.imread("bjt.jpg")

# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         b, g, r = img[i, j]
#         if b > 190 and g > 140 and r < 111:
#             img[i, j] = (255,255,240)
#     cv2.imwrite('bjt1.jpg', img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b < 80 and g < 90 and r < 120:
            if i < 300:
                img[i, j] = (219, 112, 147)
            if 299 < i < 350:
                if j < 230 or j > 380:
                    img[i, j] = (219, 112, 147)
    cv2.imwrite('bjt3.jpg', img)

cv2.imshow('show2', img)
cv2.waitKey(0)