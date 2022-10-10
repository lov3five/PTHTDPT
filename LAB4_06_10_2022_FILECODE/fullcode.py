from statistics import mode
import PIL
# Sử dụng Image của PIL để xem hình ảnh
from PIL import Image
from numpy import asarray
import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt

# Hàm đọc và show hình ảnh bằng Image from PIL
def loadImageUsePIL(img):
    image = Image.open(img)
    return image

# loadImageUsePIL('resize_panda.png').show()

# Hàm hiển thị hình ảnh bằng Matplotlib
def showImageUseMatplotlib(img):
    image_out = image.imread(img)
    print("Data type: ",image_out.dtype)
    print(image_out.shape)
    # Hiển thị hình ảnh
    plt.imshow(image_out)
    plt.show()
# showImageUseMatplotlib('panda.png')

# Hàm chuyển đổi hình ảnh thành mảng array
def convertImageToArray(img):
    data = asarray(loadImageUsePIL(img))
    return data
# print(convertImageToArray('panda.png').shape)

# Hàm tạo hình ảnh từ mảng array bằng Pillow
def convertArrayToImage(array):
    image = Image.fromarray(array)
    return image
""" array = convertImageToArray('panda.png')
print(array)
print(convertArrayToImage(array).show()) """

# Hàm xem thông tin chi tiết của hình ảnh
def viewDetailImage(img):
    image = loadImageUsePIL(img)
    print("Format: ", image.format)
    print("Size: ", image.size)
    print("Mode: ", image.mode)
# viewDetailImage('panda.png')

# Hàm chuyển đổi hình ảnh sang thang xám
def convertImage2GrayImage(img1, img2):
    im = np.array(loadImageUsePIL(img1).convert('L'))
    img2 = convertArrayToImage(im).save(img2)
# print(convertImage2GrayImage('panda.png', 'panda_convert.gif'))

# Hàm đổi lại kích cỡ hình ảnh
def resizeImage(img1, img2, weight, height):
    load_img_rz = np.array(loadImageUsePIL(img1).resize((weight, height)))
    img2 = convertArrayToImage(load_img_rz).save(img2)
print(resizeImage('panda.png', 'panda_resize_150_270.png', 150, 270))
