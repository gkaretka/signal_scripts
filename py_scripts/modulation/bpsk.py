import numpy as np
import matplotlib.pyplot as plt

size = 5
carrier_freq = 4
symbol_freq = carrier_freq / 2
sample_freq = carrier_freq * 100

data = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1]#np.random.randint(2, size=size)


def bpsk(data, symbol_freq, carrier_freq, sample_freq):
    t_duration = len(data)*1/symbol_freq
    t_step = 1.0/sample_freq

    # carrier
    t = np.arange(start=0.0, stop=t_duration, step=t_step)
    c = np.sin(2*np.pi*carrier_freq*t)

    # change data to +-1, repeat data by time
    data = np.array(list(map(lambda x: -1 if x == 0 else 1, data)))
    data = np.repeat(data, len(t)/len(data), axis=0)
    mod_signal = c * data

    return mod_signal, c, data, t


def dbpsk(data, symbol_freq, carrier_freq, sample_freq):
    vals = []
    prev_val = 1
    for i in range(len(data)):
        prev_val = prev_val ^ data[i]
        vals.append(prev_val)
        prev_val = data[i]

    t_duration = len(data)*1/symbol_freq
    t_step = 1.0/sample_freq
    # carrier
    t = np.arange(start=0.0, stop=t_duration, step=t_step)
    data_res = np.repeat(vals, len(t) / len(vals), axis=0)

    return bpsk(vals, symbol_freq, carrier_freq, sample_freq)[0], data_res


mod_sig_dbpsk, vals = dbpsk(data, symbol_freq, carrier_freq, sample_freq)
mod_signal, c, data, t = bpsk(data, symbol_freq, carrier_freq, sample_freq)

#fft_data_in = c
#res = np.abs(np.fft.fft(fft_data_in)/len(fft_data_in))

fig, axs = plt.subplots(nrows=5)
axs[0].plot(t, data)           # input
axs[0].set_title("Input data")

axs[1].plot(t, vals)           # xor-ed
axs[1].set_title("XOR-ed input data")

axs[2].plot(t, c)              # carrier
axs[2].set_title("Carrier")

axs[3].plot(t, mod_signal)     # bpsk
axs[3].set_title("BPSK")

axs[4].plot(t, mod_sig_dbpsk)  # dbpsk
axs[4].set_title("DBPSK")

#fig2, ax2 = plt.subplots()
#ax2.plot(res)

plt.show()