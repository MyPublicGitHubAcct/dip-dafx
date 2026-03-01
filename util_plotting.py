import numpy as np
from scipy.fft import fft, ifft, fftfreq, fftshift
import matplotlib.pyplot as plt


def plot_single_waveform(title, x_label, y_label, t, X):
    '''
    Call like
        plot_waveform('My Title', 'my x label', 'my y label', t, X)
    '''
    fig, ax1 = plt.subplots(1)
    ax1.set_title(title)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.plot(t, X)
    plt.tight_layout()
    plt.show()


def plot_fft_mag_phs(signal, \
                     mtitle='Magnitude response', mx_label='frequencies (f)',
                     my_label='Magnitude', \
                     ptitle='Phase response', px_label='frequencies (f)',
                     py_label='Phase', \
                     width=100, fs=41000, fft_size=41000):
    '''
    Call like
        plot_fft_mag_phs('freq domain', 'frequencies (f)', 'Magnitude', 'phase response', \
                         'frequencies (f)', 'phase', fs, fs, X)
    '''
    fig, (ax1, ax2) = plt.subplots(2)
    df = fs / fft_size  # frequency resolution
    X_fft = 1 / fft_size * fftshift(fft(signal, fft_size))  # fft of the signal
    sampleIndex = np.arange(start=-fft_size // 2, stop=fft_size // 2)  # raw index for
    # FFT plot
    xf = sampleIndex * df  # x-axis converted to freq
    phase = np.arctan2(np.imag(X_fft), np.real(X_fft)) * 180 / np.pi
    ax1.set_title(mtitle)
    ax1.set_xlabel(mx_label)
    ax1.set_ylabel(my_label)
    ax1.stem(xf, abs(X_fft))
    ax1.set_xlim(-width, width)
    ax2.set_title(ptitle)
    ax2.set_xlabel(px_label)
    ax2.set_ylabel(py_label)
    ax2.plot(xf, phase)
    plt.tight_layout()
    plt.show()
