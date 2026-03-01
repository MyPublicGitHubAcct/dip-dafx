import numpy as np
from scipy.fft import fft, ifft, fftfreq, fftshift
import matplotlib.pyplot as plt


def plot_single_waveform( time, signal, title, x_label='Time', y_label='Magnitude'):
    """
    Call like
    plot_waveform('My Title', 'my x label', 'my y label', t, X)
    """
    fig, ax1 = plt.subplots(1)
    ax1.set_title(title)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.plot(time, signal)
    plt.tight_layout()
    plt.show()


def plot_fft_mag_phs(signal,
                     axis_one_title='Magnitude response',
                     mx_label='frequencies (f)',
                     my_label='Magnitude',
                     axis_two_title='Phase response',
                     px_label='frequencies (f)',
                     py_label='Phase',
                     width=41000/2, fs=41000, fft_size=41000):
    """
    Call like
    plot_fft_mag_phs(signal, width=fs/2, fs=fs, fft_size=fs)
    """
    fig, (ax1, ax2) = plt.subplots(2)
    df = fs / fft_size  # frequency resolution
    x_fft = 1 / fft_size * fftshift(fft(signal, fft_size))  # fft of the signal
    sample_index = np.arange(-fft_size // 2, fft_size // 2)  # raw index for
    # FFT plot
    xf = sample_index * df  # x-axis converted to freq
    phase = np.arctan2(np.imag(x_fft), np.real(x_fft)) * 180 / np.pi
    ax1.set_title(axis_one_title)
    ax1.set_xlabel(mx_label)
    ax1.set_ylabel(my_label)
    ax1.stem(xf, abs(x_fft))
    ax1.set_xlim(0, width)
    ax2.set_title(axis_two_title)
    ax2.set_xlabel(px_label)
    ax2.set_ylabel(py_label)
    ax2.plot(xf, phase)
    plt.tight_layout()
    plt.show()
