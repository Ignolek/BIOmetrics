
import librosa
import librosa.display
import matplotlib.pyplot as plt
import statistics

file = "voices/MTLS_Sr18.wav"

signal, sr = librosa.load(file)

f0 = librosa.yin(signal, fmin = 60, fmax= 400)

times = librosa.times_like(f0)

print(statistics.median(f0), "Hz")
if statistics.median(f0)> 165: print("female")
else: print("male")

fig, ax = plt.subplots()
ax.set(title='YIN fundamental frequency estimation')
ax.plot(times, f0, label='f0', color='blue', linewidth=1)
ax.legend(loc='upper right')
plt.show()

