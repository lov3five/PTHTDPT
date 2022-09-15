import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

frame_rate = 48000.0
infile = "test.wav"
num_samples = 48000
wav_file = wave.open(infile, 'r')

# readframes() đọc tất cả các khung âm thanh từ một tập tin sóng.
data = wav_file.readframes(num_samples)
wav_file.close()

# sử dụng unpack để giải nén mẫu
data = struct.unpack('{n}h'.format(n=num_samples), data)

# chuyển đổi dữ liệu thành 1 mảng numpy
data = np.array(data)

