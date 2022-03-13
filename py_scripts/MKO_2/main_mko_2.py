import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

max_power = 33
"""
freq = [100, 200, 250, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
power_max = [0.5, -30, -33, -60, -60, -60, -60, -60, -60, -60, -63]
measured = [-8.4, -34.7, -40.8, -67.4, -68.8, -69.2, -70.7, -70.6, -70.1, -70.1, -70.8]
"""

freq = [400, 600, 1200, 1800]
power_max = [-23, -26, -32, -36]
measured = [-69.4, -70.5, -73, -72.6]

for f in freq:
    print(str(f) + "\t", end="")
print()

for m in measured:
    print(str(m) + "\t", end="")
print()

for pm in power_max:
    print(str(pm) + "\t", end="")

exit(1)

freq = freq + list(map(lambda x: x * (-1), freq[::-1]))
power_max = power_max + power_max[::-1]
measured = measured + measured[::-1]

data_measured = pd.DataFrame({
    "freq": freq,
    "data": measured,
})

data_reference = pd.DataFrame({
    "freq": freq,
    "data": power_max,
})

fig, ax = plt.subplots()
sns.set_color_codes("pastel")

sns.scatterplot(data=data_measured, x="freq", y="data", ax=ax, color='blue')
sns.lineplot(data=data_reference, x="freq", y="data", ax=ax, color='r')

ax.set_ylabel('Namerané výkonové úrovne a tolerančné pásmo [dB]')
ax.set_xlabel('Frekvenčný offset od nosnej [kHz]')
plt.grid()
plt.show()
