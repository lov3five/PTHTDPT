import cv2
import sys

# Đọc dữ liệu hình ảnh, sys.argv[1]: Ex: py [a.py] [b.jpg] thì sys.argv[1] = b.jpg
image = cv2.imread(sys.argv[1])

# Hàm hiển thị hình ảnh ra màn hình
def displayImage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)

# Hàm chuyển đổi hình ảnh thành màu Gray
def convertImageToGray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hàm làm mờ hình ảnh và cho ra kích thước mong muốn
def blurImageWithPx(img, n):
    return cv2.GaussianBlur(img, (n,n), 0)

# Hàm phát hiện cạnh
def detectEdge(img, lowerLevel, upperLevel):
    return cv2.Canny(img, lowerLevel, upperLevel)

# Hàm tìm tất cả các cạnh và trả về 2 giá trị 
def findContoursImage(img):
    contours, hierarchy = cv2.findContours(detectEdge(img, 10, 30), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def drawContourImage(img, color, thickness):
    cv2.drawContours(img, findContoursImage(blurImageWithPx(image, 7)), -1, color, thickness)
    displayImage(img)

#displayImage(image)
#displayImage(convertImageToGray(image))
#displayImage(blurImageWithPx(image, 1))
#displayImage(detectEdge(blurImageWithPx(image, 7), 10, 30))
#print("Số lượng là: ", len(findContoursImage(blurImageWithPx(image, 7))))
#drawContourImage(image, (0,255,0), 2)
