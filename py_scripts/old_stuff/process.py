import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

d1 = pd.read_csv("d1.csv", sep="\t")
d2 = pd.read_csv("d1.csv", sep="\t")
d3 = pd.read_csv("d1.csv", sep="\t")

print(d1.head())

target = ["IL [dB]"]
features = ["fGEN [MHz]"]

X = d1[features]
y = d1[target]

sns.lineplot(data=d1, x="fGEN [MHz]", y="IL [dB]")
plt.show()
