from os import remove
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import statistics

file = "6m.wav"
file_fem = "6f.wav"

signal, sr = librosa.load(file, mono=True)
signal2, sr2 = librosa.load(file_fem, mono=True)

#librosa.display.waveshow(signal, sr=sr)

#plt.xlabel("Time")
#plt.ylabel("Amplitude")
#plt.show()

f0 = librosa.yin(signal, fmin = 120, fmax= 400)
#print(f0.shape)
#print(f0)

f0_fem = librosa.yin(signal2, fmin = 120, fmax= 400)
#print(f0_fem.shape)
#print(f0_fem)
#print(f0_fem[0])
for i in range(len(f0_fem)):
    if f0_fem[i]>350: f0_fem[i] = f0_fem[i-1] 

print(statistics.median(f0_fem))
print(statistics.median(f0))

for i in range(len(f0)):
    if f0[i]>350: f0[i] = f0[i-1] 

times = librosa.times_like(f0)
timesf = librosa.times_like(f0_fem)

fig, ax = plt.subplots()
ax.set(title='YIN fundamental frequency estimation')
ax.plot(times, f0, label='male', color='blue', linewidth=1)
ax.plot(timesf, f0_fem, label='female', color='orange', linewidth=1)
ax.legend(loc='upper right')
plt.show()

#fft = np.fft.fft(signal)

#magnitude = np.abs(fft)
#frequency = np.linspace(0, sr ,len(magnitude))
#plt.plot(frequency, magnitude)
#plt.xlabel("Frequency")
#plt.ylabel("Magnitude")
#plt.show()