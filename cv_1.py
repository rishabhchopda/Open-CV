import cv2

img = cv2.imread("D:\images\images.jpg", 0)

print("Dimensions of the image: ",img.shape)

width = 400
height = 400
dim = (width,height)
resized = cv2.resize(img, dim)

cv2.imshow("window", resized)

# cv2.imwrite('D:\images\car.jpg', img)

cv2.waitKey(0)

cv2.destroyAllWindows()