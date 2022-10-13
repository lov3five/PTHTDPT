#a,Phân biệt tần số lấy mẫu và tần số tín hiệu
#b,Viết code tạo ra một sóng hình sin với tần số là 2000,biên độ là 10000,tần số lấy mẫu là 48000
#Giải thích code
import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

# Tần số là số lần sóng lặp lại một giây
frequency = 2000
# Lấy mẫu
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


