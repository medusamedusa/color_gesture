import numpy as np
from scipy.io.wavfile import write

# carrier frequency
fc = 440
wc = 2 * np.pi * fc

# modulator frequency
fm = 2 * fc
wm = 2 * np.pi * fm

sampling_rate = 48000

# número de segundos que quiero que dure el sonido (dominio de la onda)
ts = 20

num_samples = int(sampling_rate * ts)

# amplitude
amplitude = np.iinfo(np.int16).max  # format

# wave
t = np.linspace(0, ts, num_samples)
FMpath = np.sin(wc * t + t * np.sin(wm * t))  # I=t (ranges from 0 to ts)

write("FM_path.wav", sampling_rate, (amplitude * FMpath).astype(np.int16))
