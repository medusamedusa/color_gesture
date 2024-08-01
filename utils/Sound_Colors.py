# The color of a sound spectrum
import numpy as np
import colour

# from colour.plotting import plot_single_colour_swatch

f1 = 440  # base frequency for octave reduction to [f1,2f1]

# octave reduction


def integer(freq):  # ¡Warning: does not admit 0 frequencies!
    return np.floor(np.log2(freq / f1))


def redu(freq):
    return freq / (2 ** integer(freq))


# from wavelength to frequency


def f_(w):
    return 760 * f1 / w


# from frequency to wavelength


def w_(freq):
    return f_(redu(freq))


# CIE color matching functions
cmfs = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]

# conversion from linear RGB to standard RGB
# (electro-optical transfer function)


def mininon(c):
    if c <= 0.0031308:
        return c * 12.92
    elif c > 0.0031308:
        return 1.055 * (c) ** (1 / 2.4) - 0.055


def nonlin(RGB):
    return [mininon(c) for c in RGB]


# Color from sound spectrum


def RGBnl(f, a):
    XYZ = colour.wavelength_to_XYZ(w_(f), cmfs)  # CIE coordinates
    color = np.dot(a, XYZ)
    RGB = colour.XYZ_to_sRGB(color)  # CIE to linear RGB conversion
    RGBnonl = nonlin(RGB)  # RGB to usual (non linear) RGB
    return RGBnonl


# plot_single_colour_swatch(RGBnl(np.array([440]), np.array([0.1])))
