import numpy as np

from util_waveforms import wv_sine
# from matplotlib import pyplot as plt
from util_plotting import plot_single_waveform

def plot_sine():
    fs = 100
    seconds = 1
    t = np.linspace(0, seconds, fs * seconds)
    freq = 1
    signal = wv_sine(t, freq)
    plot_single_waveform("A Sine Wave", "Time", "Amplitude", t, signal)

if __name__ == '__main__':
    plot_sine()
