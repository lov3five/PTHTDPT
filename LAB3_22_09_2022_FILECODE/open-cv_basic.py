import cv2
#from google.colab.patches import cv2_imshow

img = cv2.imread('rose.png')

print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))

#Phân tách hình ảnh thành 3 kênh blue, green, red (BGR)
blue, green, red = cv2.split(img)

#Chuyển đổi hình ảnh thành màu Gray
img_gs = cv2.imread('rose.png', cv2.IMREAD_GRAYSCALE)

#cv2.imshow("Channel RED",red) # Hiển thị kênh red
#cv2.imshow("Channel BLUE",blue) # Hiển thị kênh blue
#cv2.imshow("Channel GREEN",green) # Hiển thị kênh green
#cv2.imshow("Convert to GRAY", img_gs) # hiển thị hình ảnh màu xám

# Thực hiện ngưỡng nhị phân trên hình ảnh với T = 125
r, threshold = cv2.threshold( cv2.imread('image2.png'), 125, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded", threshold)
cv2.waitKey(0)

