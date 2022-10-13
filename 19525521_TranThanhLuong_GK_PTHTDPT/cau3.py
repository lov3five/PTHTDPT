""" 
MSSV: 19525521
Họ và tên: Trần Thanh Lượng
"""

# Câu 3b
#b.Tần số tín hiệu f = 2000 Hz, tần số lấy mẫu là fs = 48000 Hz, biên độ 10000
# import thư viện numpy
import numpy as np
# import thư viện wave 
import wave
# struct là 1 thư viện của python lấy dữ liệu và đóng gói dưới dạng dữ liệu binary
import struct
# import thư viện matplotlib.pylot dùng để vẽ đồ thị
import matplotlib.pyplot as plt

# Tần số tín hiệu (là số lần sóng lặp lại một giây)
frequency = 2000
# Số lượng mẫu lấy
num_samples = 48000
# Tỷ lệ lấy mẫu của chuyển đổi từ tương tự sang kỹ thuật số
sampling_rate = 48000.0
# Biên độ
amplitude = 10000
# File âm thanh
file = "test.wav"
# Tạo sóng hình sin
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
# Gán số lượng mẫu cho khung hình
nframes=num_samples
comptype="NONE"
compname="not compressed"
# Số kênh âm thanh
nchannels=1
# sampwidth là chiều rộng mẫu tính bằng byte.
sampwidth=2
# Ghi sóng sin vào file
wav_file=wave.open(file, 'w')

wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    # writeframes là hàm ghi một sóng hình sin
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
struct.pack('h', int(s*amplitude))
