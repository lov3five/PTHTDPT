from statistics import mode
import PIL
# Sử dụng Image của PIL để xem hình ảnh
from PIL import Image
from numpy import asarray
import numpy as np

# Kiểm tra version Pillow
print('Pillow Version:', PIL.__version__)

# Mở hình ảnh cần dùng với Image
image = Image.open('panda.png')

# Xem thông tin chi tiết của hình ảnh
""" print("Format: ", image.format)
print("Size: ", image.size)
print("Mode: ", image.mode)
image.show() """

# Tạo mảng array từ hình ảnh
data = asarray(image)
print("Data type of image: ",type(data))
print(data)

# Shape
print("Shape",data.shape)

# Tạo hình ảnh bằng Image của Pillow (tạo hình ảnh từ mảng array)
image2 = Image.fromarray(data)
print(type(image2))

# Thông tin chi tiết của hình ảnh
print("Mode: ",image2.mode)
print("Size: ",image2.size)
# image2.show()

# Chuyển đổi hình ảnh sang thang xám
im = np.array(Image.open('panda.png').convert('L')) #you can pass multiple arguments in single line
print(type(im))
print(im)

# Setup định dạng hình ảnh png/gif/peg...
gr_im= Image.fromarray(im).save('gray_panda.jpeg')

# Đổi kích cỡ hình ảnh (resize)
load_img_rz = np.array(Image.open('panda.png').resize((200,200)))
Image.fromarray(load_img_rz).save('resize_panda.png')
print("After resizing:",load_img_rz.shape)