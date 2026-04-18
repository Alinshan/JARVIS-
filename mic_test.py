import sounddevice as sd
import numpy as np
import time

def callback(indata, frames, time, status):
    # indata is numpy array [frames, channels]
    amplitude = np.max(np.abs(indata))
    print(f"Mic Peak Amplitude: {amplitude}", flush=True)

try:
    with sd.InputStream(samplerate=48000, channels=1, dtype="int16", callback=callback, blocksize=4800):
        print("Listening for 3 seconds...")
        time.sleep(3)
except Exception as e:
    print(f"Error: {e}")
