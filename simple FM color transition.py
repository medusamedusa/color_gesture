import time
import numpy as np
from scipy.special import jv as J
from numpy import sign
from colour.plotting import plot_multi_colour_swatches
from utils.Sound_Colors import RGBnl

# operator frequencies
f_base = 440
Qvec = [1, 2]

# N is the list of subindices that we use from the color series
p = 50
N = range(-p, p + 1)


def FM_RGBnl(f, Q, I):
    """from a simple FM wave with carrier frequency f,
    modulator frequency Q[1]*f,
    and modulation index I to standard RGB"""
    # dictionary assigning to frequency ratios
    # their amplitudes
    D = {}
    for n in N:
        # turn all frequency signs positive
        key = Q[0] + n * Q[1]
        s = sign(key)
        # sum all amplitudes for the same frequency
        if s * key in D:
            D[s * key] += s * J(n, I)
        else:
            D[s * key] = s * J(n, I)

    freq = f * np.array(list(D.keys()))
    a = np.abs(list(D.values()))
    RGBnonl = RGBnl(freq, a)
    return RGBnonl


start = time.time()
shade = [
    FM_RGBnl(f_base, Qvec, i / 10) for i in range(201)
]  # final transition, 20 seconds
print("Runtime: {} seconds".format(time.time() - start))

plot_multi_colour_swatches(shade, columns=10)  # transition rendering
