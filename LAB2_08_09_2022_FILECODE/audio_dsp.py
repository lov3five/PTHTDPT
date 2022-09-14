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

# 
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
 
# mở tệp "test.wav" và ghi
wav_file=wave.open(file, 'w')

# thiết lập thông số params
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# writeframes: hàm ghi sóng hình sin
# 
for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))

frame_rate = 48000.0

infile = "test.wav"

num_samples = 48000

wav_file = wave.open(infile, 'r')

data = wav_file.readframes(num_samples)

wav_file.close()

data = struct.unpack('{n}h'.format(n=num_samples), data)
data = np.array(data)
data = np.array(data)
data_fft = np.fft.fft(data)

# This will give us the frequency we want
frequencies = np.abs(data_fft)

# This will give us the frequency we want
frequencies = np.abs(data_fft)

plt.subplot(2,1,1)
plt.plot(data[:300])
plt.title("Original audio wave")
plt.subplot(2,1,2)
plt.plot(frequencies)
plt.title("Frequencies found")
plt.xlim(0,1200)
plt.show()

print("The frequency is {} Hz".format(np.argmax(frequencies)))


# frequency is the number of times a wave repeats a second
frequency = 1000
noisy_freq = 50
num_samples = 48000

# The sampling rate of the analog to digital convert
sampling_rate = 48000.0

#Create the sine wave and noise

sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]

#Convert them to numpy arrays

sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

# Add them to create a noisy signal
combined_signal = sine_wave + sine_noise

plt.subplot(3,1,1)

plt.title("Original sine wave")

# Need to add empty space, else everything looks scrunched up!

plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])
plt.subplot(3,1,2)
plt.title("Noisy wave")
plt.plot(sine_noise[:4000])
plt.subplot(3,1,3)
plt.title("Original + Noise")
plt.plot(combined_signal[:3000])
plt.show()







