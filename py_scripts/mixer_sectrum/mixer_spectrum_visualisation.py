import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

f_lo = 460

f_rf_low = 0
f_rf_high = 30
rf_step = 1

prod_rank = 3

base_spect = np.arange(f_rf_low, f_rf_high, rf_step)
mixing_prod_ranks = np.arange(-prod_rank, prod_rank+1, 1)
double_balance = mixing_prod_ranks[mixing_prod_ranks%2!=0]

print(double_balance)
resulting_specs = pd.DataFrame()

vals = []
freqs = []
designators = []
val = 2
for i in range(len(double_balance)):
    for j in range(len(double_balance)):
        for k in range(len(base_spect)):
            # f = m * f_rf + n * f_lo
            _freq = base_spect[k] * double_balance[i] + f_lo * double_balance[j]
            freqs.append(_freq)
            designators.append(str(double_balance[i]) + str(double_balance[j]) +":"+ str(val))

            if k == 0 or k == len(base_spect)-1:
                vals.append(0)
            else:
                vals.append(val)

        val += 2

# add filter 320 - 390 MHz
freqs += [320, 321, 389, 390]
designators += ["filter 320-390", "filter 320-390", "filter 320-390", "filter 320-390"]
vals += [0, np.average(vals), np.average(vals), 0]

res = pd.DataFrame(data={'freqs': freqs, 'vals': vals, 'designator': designators})

sns.lineplot(data=res, x="freqs", y="vals", style="designator", hue="designator")
plt.show()
