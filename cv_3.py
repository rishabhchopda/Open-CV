import cv2
import numpy as np

img = cv2.imread("D:\images\images.jpg")
# width = 600
# height = 850
# dim = (width,height)
# resized = cv2.resize(img, dim)
print('Size in bytes: ',img.size)
cv2.imshow("Original", img)

# flip = cv2.flip(img, 1)
# cv2.imshow("Horizontal", flip)

# flip_1 = cv2.flip(img, 0)
# cv2.imshow("Vertical", flip_1)

flip_2 = cv2.flip(img, -1)
cv2.imshow("Horizontal & Vertical", flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()