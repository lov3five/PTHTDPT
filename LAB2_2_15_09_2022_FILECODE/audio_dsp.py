""" 
Họ tên: Trần Thanh Lượng
MSSV: 19525521
"""

import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

import numpy as np
import wave
# struct là 1 thư viện của python lấy dữ liệu và đóng gói dưới dạng dữ liệu binary
import struct
import matplotlib.pyplot as plt

# frequency là tần số
frequency = 1000
# num_samples là số lượng mẫu
num_samples = 48000
# sampling_rate là tốc độ lấy mẫu của chuyển đổi từ tương tự sang kỹ thuật số
sampling_rate = 48000.0
# amplitutde là biên độ
amplitude = 16000
# file chứa định dạng âm thanh
file = "test.wav"
# sine_wave là hàm sin
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]


# nframes: số lượng khung hình
# comptype 
# compname
# nchannels: số kênh
# sampwidth: chiều rộng mẫu (byte)


nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2
