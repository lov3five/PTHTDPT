import cv2
import sys

# Đọc dữ liệu hình ảnh, sys.argv[1]: Ex: py [a.py] [b.jpg] thì sys.argv[1] = b.jpg
image = cv2.imread(sys.argv[1])


cv2.imshow("Image", image)
# hình ảnh không đóng ngay lập tức. Nó sẽ đợi nhấn phím trước khi đóng hình ảnh.
cv2.waitKey(0) 