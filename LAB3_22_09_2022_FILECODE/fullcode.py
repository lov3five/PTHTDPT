import cv2
import sys

# Đọc dữ liệu hình ảnh, sys.argv[1]: Ex: py [a.py] [b.jpg] thì sys.argv[1] = b.jpg
image = cv2.imread(sys.argv[1])