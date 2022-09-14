import random
import winsound
import time

filename = 'test.wav'
#winsound.PlaySound(filename, winsound.SND_FILENAME)

#winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 100 ms
while True:
    winsound.Beep(1000, 400)
    time.sleep(0.5)
    winsound.Beep(1000, 200)
    winsound.Beep(1000, 300)
    winsound.Beep(1000, 700)
    winsound.Beep(1000, 500)
    winsound.Beep(1000, 600)
    winsound.Beep(1000, 900)
    
    winsound.Beep(1000, 800)
    
    #time.sleep(random.randrange(5,10))