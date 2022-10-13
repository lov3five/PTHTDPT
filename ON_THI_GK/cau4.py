#viết code hiển thị hình anh,Chuyển đổi sang thang độ xám,làm mờ hinhf ảnh,Phát hiện cạnh
# giải thích code.
# Thêm thư viện cv2
import cv2

# Đọc hình ảnh
image = cv2.imread('./yasuo.jpg')

#Chuyển đổi sang thang gray-scale (mức xám)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# BLur hình ảnh
blurred_image = cv2.GaussianBlur(image, (7,7), 0)

# Phát hiện cạnh
canny = cv2.Canny(blurred_image, 10, 30)

# Hiển thị cả 3 hình ảnh lên màn hình
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blurred Image", blurred_image)
# Hiển thị hình ảnh sau khi sử dụng phát hiện cạnh
cv2.imshow("Canny with low thresholds", canny)
cv2.waitKey(0)
