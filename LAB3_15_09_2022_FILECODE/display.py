import cv2
import sys
""" 
OpenCv làm điều đó theo cách khác - vì vậy màu xanh lam là đầu tiên, sau đó là màu xanh lá cây, sau đó là màu đỏ. =>> BGR
 """

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