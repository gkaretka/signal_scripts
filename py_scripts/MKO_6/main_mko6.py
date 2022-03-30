import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("data/part1.csv", sep=";")
print(data.head())

power = -30.0
data['Attenuation [dB]'] = power - data['Measured [dBm]']

# average
average_att = []
for i in range(int(len(data['Attenuation [dB]'].values)/3)):
    vals = data['Attenuation [dB]'].values
    average_att.append((vals[i] + vals[i+10] + vals[i+20]) / 3)
new_data = pd.DataFrame(data={'Distance [m]': list(range(1, 11)), 'Attenuation [dB]': average_att})

#for v in new_data['Attenuation [dB]'].values:
#    print(v)

# theoretical calculation
d = np.arange(1, 10+1, 1)

c = 3*10**8
f = 900*10**6
G_t_db = 12
G_r_db = 2

G_t = 10**(G_t_db/10)
G_r = 10**(G_r_db/10)

#print(G_t, G_r)

lambda_2 = (c/f)**2

y = -10*np.log10((G_t*G_r*lambda_2)/((4*np.pi)**2*(d**2)))

for v in y:
    print(v)

# plot
plt.plot(new_data['Distance [m]'].values, new_data['Attenuation [dB]'], label="Average", linestyle=":")
plt.plot(d, y, label="Theoretical", linestyle="-")

plt.ylabel("Attenuation [dB]")
plt.xlabel("Distance [m]")
plt.xticks(d)
plt.grid()
plt.legend()
plt.show()



