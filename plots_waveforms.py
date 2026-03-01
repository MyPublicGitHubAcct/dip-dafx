import numpy as np

from util_waveforms import wv_sine, wv_sawtooth
from util_plotting import plot_single_waveform, plot_fft_mag_phs

def plot_sine():
    fs = 48000
    nyquist_frequency = fs / 2
    seconds = 1
    t = np.linspace(0, seconds, fs * seconds)
    freq = 440
    # signal = wv_sine(t, freq)
    signal = wv_sawtooth(t, freq)

    # plot_single_waveform(t, signal, "A Sine Wave", "Time", "Amplitude")
    plot_fft_mag_phs(signal, width=nyquist_frequency, fs=fs, fft_size=fs)

if __name__ == '__main__':
    plot_sine()
