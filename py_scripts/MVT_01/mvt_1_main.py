import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data.DAT", sep=";")

# prepare dataframe
freqs = np.concatenate((data["f0 [MHz]"].values, data["fOT [MHz]"].values))
ds = np.concatenate((data["d [mm]"].values, data["d [mm]"].values))

strs_1 = ["f0 [MHz]"] * len(data["f0 [MHz]"].values)
strs_2 = ["fOT [MHz]"] * len(data["fOT [MHz]"].values)
types = np.concatenate((strs_1, strs_2))

data_res = pd.DataFrame(data={"d [mm]": ds, "f [MHz]": freqs, "types": types})

fig, ax = plt.subplots()

sns.set_palette("Set1", 8, .75)
sns.lineplot(data=data_res, x="d [mm]", y="f [MHz]", hue="types", style="types", markers=True)

x_ticks = np.arange(1, 15.5, 0.5)
y_ticks = np.arange(8500, 9800, 100)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)

plt.grid()
plt.show()
