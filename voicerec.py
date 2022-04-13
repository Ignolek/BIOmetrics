import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

file = "3.wav"

signal, sr = librosa.load(file,sr = 22050)

librosa.display.waveshow(signal, sr=sr)

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr ,len(magnitude))
plt.plot(frequency, magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()