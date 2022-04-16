import pandas as pd
import matplotlib.pyplot as plt

f = open("data.csv", "r")
s = f.read().replace(",", ".")
f.close()

f = open("data.csv", "w")
f.write(s)
f.close()

data = pd.read_csv("data.csv", sep=";")

print(data.head())

x = data['S/N [dB]']
y1_per = data['EVM Data Carriers [%]']
y2_per = data['EVM Pilot Carriers [%]']

y1_db = data['EVM Data Carriers [dB]']
y2_db = data['EVM Pilot Carriers [dB]']

fig, ax = plt.subplots()
ax.plot(x, y1_per, label="EVM Data Carriers [%]", linestyle=":")
ax.plot(x, y2_per, label="EVM Pilot Carriers [%]", linestyle="-")
plt.xlabel("SNR [dB]")
plt.ylabel("EVM [%]")
plt.legend()
plt.grid()

fig2, ax2 = plt.subplots()
ax2.plot(x, y1_db, label="EVM Data Carriers [dB]", linestyle=":")
ax2.plot(x, y2_db, label="EVM Pilot Carriers [dB]", linestyle="-")
plt.xlabel("SNR [dB]")
plt.ylabel("EVM [dB]")
plt.legend()
plt.grid()

plt.show()
