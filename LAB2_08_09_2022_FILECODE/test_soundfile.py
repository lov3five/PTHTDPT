import soundfile as sf

data, samplerate = sf.read('test.wav')
sf.write('new_file.flac', data, samplerate)