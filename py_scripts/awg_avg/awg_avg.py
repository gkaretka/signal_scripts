import numpy as np
import matplotlib.pyplot as plt

def averaging_noise_influence(t_duration=1):
    """
    :type t_duration: int - duration in seconds
    """
    sample_freq = 1000
    carrier_freq = 10

    t_step = 1.0 / sample_freq

    # signal
    t = np.arange(start=0.0, stop=t_duration, step=t_step)
    c = np.sin(2 * np.pi * carrier_freq * t)

    # SNR in [-]
    SNR = 0.1
    n_amp = max(c)/SNR

    # normal (gaussian)
    noise_volts = np.random.normal(size=c.shape, scale=n_amp)

    # uniform
    #noise_volts = np.random.uniform(size=c.shape, low=-n_amp, high=n_amp)

    # add noise
    c_awgn = c + noise_volts

    # fft
    spect = abs(np.fft.fft(c_awgn))/len(c_awgn)
    spect = np.fft.fftshift(spect)

    fig, axs = plt.subplots(2, 1)

    axs[0].plot(t, c)
    axs[0].plot(t, c_awgn)
    axs[1].plot(spect)

"""
Frequency 10 Hz
Sampling frequency 1 kHz
-------------------------------------------
How does number of samples influence noise.
"""
averaging_noise_influence(1)
averaging_noise_influence(10)
averaging_noise_influence(100)
averaging_noise_influence(1000)

plt.show()