import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

# Các chuyển đổi không gian màu mà OpenCV cung cấp
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flags)

# Danh sách số lượng flag
print(len(flags))


nemo = cv2.imread('nemo.jpg')
plt.imshow(nemo)
plt.show()

nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
plt.imshow(nemo)
plt.show()

# Phân chia hình ảnh thành 3 kênh R, G, B (đã convert COLOR_BGR2RGB)
r, g, b = cv2.split(nemo)
# Thiết lập 3D
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")


pixel_colors = nemo.reshape((np.shape(nemo)[0]*np.shape(nemo)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
#plt.show()

hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)

light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)

from matplotlib.colors import hsv_to_rgb

lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 255.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()


