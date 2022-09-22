import cv2

img = cv2.imread('rose.png')

print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))

#Phân tách hình ảnh thành 3 kênh blue, green, red (BGR)
blue, green, red = cv2.split(img)

#Chuyển đổi hình ảnh thành màu Gray
img_gs = cv2.imread('rose.jpg', cv2.IMREAD_GRAYSCALE)




