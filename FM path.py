#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import wave
import struct

# carrier frequency
fc = 440
wc=2 * np.pi * fc # 2 * np.pi * fc

# modulator frequency
fm = 2*fc # fm = 2*fc
wm= 2*np.pi * fm # 2 * np.pi * fm

# sampling rate
sampling_rate = 48000.0

# wave duration
ts=20

num_samples = int(sampling_rate*ts)

# amplitude
amp=1
amplitude = int(32767*amp) # for the writing process

#wave
FMpath=[]
for x in range(num_samples):
    t=x/sampling_rate 
    I=t #we identify modulation index and time
    FMpath.append(np.sin(wc* t + I*np.sin(wm* t))) # FMpath.append(np.sin(wc* t + I*np.sin(wm* t)))

# writing
file = "FM path.wav"
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in FMpath:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))

