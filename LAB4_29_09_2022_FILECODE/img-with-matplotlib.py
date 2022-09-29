# Tải và hiển thị hình ảnh với Matplotlib
from matplotlib import image
from matplotlib import pyplot as plt

# Đọc hình ảnh
image = image.imread('panda.png')

print("Data type: ",image.dtype)
print(image.shape)

# Hiển thị hình ảnh
plt.imshow(image)
plt.show()