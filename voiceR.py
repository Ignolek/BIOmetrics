from os import remove
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import statistics

file = "voices/FHRO_Sr31.wav"

signal, sr = librosa.load(file, mono=True)

f0 = librosa.yin(signal, fmin = 80, fmax= 400)

times = librosa.times_like(f0)

print(statistics.median(f0))
if statistics.median(f0)> 165: print("female")
else: print("male")

fig, ax = plt.subplots()
ax.set(title='YIN fundamental frequency estimation')
ax.plot(times, f0, label='x', color='blue', linewidth=1)
ax.legend(loc='upper right')
plt.show()

