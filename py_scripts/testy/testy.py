import numpy as np
import matplotlib.pyplot as plt

"""
Power calculation of signal
"""

freq = 10
f_samp = freq*100
amplitude = 2
resistance = 1

t = np.arange(start=0.0, stop=1.0/freq, step=1.0/f_samp)

s_vals = amplitude*np.sin(2*np.pi*freq*t)
sum = 0
inst_power = []
for i in range(len(s_vals)):
    sum += (s_vals[i]**2)/resistance
    inst_power.append((s_vals[i]**2)/resistance)

sum = (freq/f_samp)*sum
sig_power = [sum] * len(inst_power)

fig, ax = plt.subplots()
plt.plot(s_vals, label="Voltage [V]")
plt.plot(inst_power, label="Instantaneous power [W]")
plt.plot(sig_power, label="Signal power [W]")
plt.grid()
plt.legend()
plt.show()
