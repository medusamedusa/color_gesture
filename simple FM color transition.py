#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv as J
from numpy import log, floor, sign, array
import colour # interesting library for colorimetry
from colour.plotting import *

# operator frequencies 
f = 440
Q=[1,2]

# N is the list of subindices that we use from the color series
p=50
N=range(-p,p+1)

# base frequency for octave reduction
f1=440 

# octave reduction
def integer(freq):
    return floor(log(freq/f1)/log(2))

def redu(freq):
    return freq/(2**integer(freq))

# from wavelength to frequency
def f_(w):
    return 760*f1/w

# from frequency to wavelength
def w_(freq):
    return f_(redu(freq))                                        

# CIE color matching functions
cmfs = colour.MSDS_CMFS['CIE 1931 2 Degree Standard Observer']

# conversion from linear RGB to standard RGB 
# (electro-optical transfer function)
def mininon(c):
    if c<=0.0031308:
        out=c*12.92
    elif c>0.0031308:
        out=1.055*(c)**(1/2.4)-0.055
    return out

def nonlin(RGB):
    return [mininon(c) for c in RGB]    

# from a simple FM wave with carrier frequency f,
# modulator frequency Q[1]*f,
# and modulation index I to standard RGB
def RGBnl(f,Q,I):
    # dictionary assigning to frequency ratios
    # their amplitudes
    D={}
    # we 
    for n in N:
        # we turn all frequency signs positive 
        key=Q[0]+n*Q[1]
        s=sign(key)
        # we sum all amplitudes for the same frequency 
        D[s*key]=+ s*J(n,I)
    
    color=array([0,0,0])
    
    # the color series
    for key in D:
        D[key]=abs(D[key]) # we turn all negative amplitudes positive
        l=w_(f*key) # wavelength from frequency
        XYZ=colour.wavelength_to_XYZ(l, cmfs) # CIE coordinates
        color=color +D[key]*XYZ  # sum      
    
    RGB=colour.XYZ_to_sRGB(color) # CIE to linear RGB conversion
    RGBnl=nonlin(color) # RGB to standard RGB
    return RGBnl

# final transtion
transition=[RGBnl(f,Q,i/10) for i in range(201)]

# transition rendering
plot_multi_colour_swatches(transition,columns=10)

