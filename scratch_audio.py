import sounddevice as sd
import time
def callback(*args):
    pass
with sd.InputStream(samplerate=16000, channels=1, callback=callback):
    time.sleep(1)
print("Sounddevice Test OK")
