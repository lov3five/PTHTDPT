import numpy as np
import cv2

img = cv2.imread('rose.png')
#Chuyển đổi hình ảnh thành màu Gray
img_gs = cv2.imread('rose.png', cv2.IMREAD_GRAYSCALE)
# Adding salt & pepper noise to an image
def salt_pepper(prob):
      # Extract image dimensions
      row, col = img_gs.shape
      # Declare salt & pepper noise ratio
      s_vs_p = 0.5
      output = np.copy(img_gs)
      # Apply salt noise on each pixel individually
      num_salt = np.ceil(prob * img_gs.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in img_gs.shape]
      output[coords] = 1
      # Apply pepper noise on each pixel individually
      num_pepper = np.ceil(prob * img_gs.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in img_gs.shape]
      output[coords] = 0
      cv2.imshow("Output",output)
      return output
# Call salt & pepper function with probability = 0.5
# on the grayscale image of rose
sp_05 = salt_pepper(0.5)
# Store the resultant image as 'sp_05.jpg'
cv2.imwrite('sp_05.jpg', sp_05)
cv2.waitKey(0)