import simpleaudio as sa

filename = 'example.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
print("Start play audio...")
play_obj = wave_obj.play()
play_obj.wait_done()
print(">>><<<")