import cv2
import sys

# Đọc dữ liệu hình ảnh, sys.argv[1]: Ex: py [a.py] [b.jpg] thì sys.argv[1] = b.jpg
image = cv2.imread(sys.argv[1])

cv2.imshow("Image", image)
# hình ảnh không đóng ngay lập tức. Nó sẽ đợi nhấn phím trước khi đóng hình ảnh.
cv2.waitKey(0) 

# Chuyển đổi hình ảnh thành màu Gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", gray_image)
cv2.waitKey(0) 

# Làm mờ hình ảnh và cho ra kích thước 7x7 pixel
blurred_image = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("Image", blurred_image)
cv2.waitKey(0) 

# Phát hiện cạnh với ngưỡng dưới = 10, ngưỡng trên = 30
canny = cv2.Canny(blurred_image, 10, 30)
cv2.imshow("Canny with low thresholds", canny)
cv2.waitKey(0) 

contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Số lượng đường viền được tìm thấy
print("Number of objects found = ", len(contours)) # Number of objects found =  7489

cv2.drawContours(image, contours, -1, (0,255,0), 2)
cv2.imshow("objects Found", image)
cv2.waitKey(0)




