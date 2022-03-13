import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import linspace
from scipy.stats import linregress

"""
task 1 = vco
task 2 = phase noise
task 3 = SAW
"""

task_n = 3

if task_n == 1:
    data_vco = pd.read_csv("vco.DAT", sep=";")

    fig, ax = plt.subplots()
    sns.set_color_codes("pastel")

    # calc slope
    slope, intercept, r_value, p_value, std_err = linregress(data_vco['vco[V]'], data_vco['f[MHz]'])

    l1 = sns.regplot(data=data_vco, x="vco[V]", y="f[MHz]", ax=ax, color="red", label="frekvencie VCO [MHz]",
                     line_kws={'label':"y={0:.2f}x+{1:.2f}".format(slope, intercept)})

    ax2 = ax.twinx()
    l2 = sns.scatterplot(data=data_vco, x="vco[V]", y="P [dBm]", ax=ax2, color="blue", label="výkonu VCO [dBm]")

    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(lines + lines2, labels + labels2, loc='lower center')
    ax2.get_legend().remove()

    plt.grid()
    plt.show()
elif task_n == 2:
    data = pd.read_csv("phase_noise.DAT", sep=";")

    sns.set_color_codes("pastel")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="Offset Frequency[kHz]", y="Alpha(offset) [dBc/Hz]", ax=ax, color="blue")
    ax.set_ylim([-125, -102])
    plt.grid()
    plt.show()
elif task_n == 3:
    data = pd.read_csv("data.DAT", sep=";")

    # in Hz in data, to MHz now
    divisor = 1e6
    data["freq [MHz]"] = data["freq [Hz]"].apply(lambda x: x/divisor)
    data["L [dB]"] = data["L [dB]"].apply(lambda x: float(x.replace(",", ".")))

    sns.set_color_codes("pastel")
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x="freq [MHz]", y="L [dB]", ax=ax, color="blue")

    vals = np.array(data["L [dB]"].values)
    freqs = np.array(data["freq [MHz]"].values)

    max_val = vals.max(axis=0, initial=-9999)
    min_val = vals.min(axis=0, initial=0)

    vals_l, vals_r = np.array_split(vals, 2)
    freqs_l, freqs_r = np.array_split(freqs, 2)

    # max value - 3dB
    difference_array = np.absolute(vals_l - (max_val - 3))
    index_l_3 = difference_array.argmin()

    idxs = np.argwhere(freqs_r > 955)
    freqs_r = freqs_r[idxs]
    vals_r = vals_r[idxs]

    difference_array = np.absolute(vals_r - (max_val - 3))
    index_r_3 = difference_array.argmin()

    freq_l_3 = freqs_l[index_l_3]
    freq_r_3 = freqs_r[index_r_3]

    ax.axline((freq_l_3, max_val), (freq_l_3, min_val), color="red")
    ax.axline((freq_r_3[0], max_val), (freq_r_3[0], min_val), color="red")

    # max value - 30dB
    vals_l, vals_r = np.array_split(vals, 2)
    freqs_l, freqs_r = np.array_split(freqs, 2)

    difference_array = np.absolute(vals_l - (max_val - 30))
    index_l_30 = difference_array.argmin()

    idxs = np.argwhere(freqs_r > 950)
    freqs_r = freqs_r[idxs]
    vals_r = vals_r[idxs]

    difference_array = np.absolute(vals_r - (max_val - 30))
    index_r_30 = difference_array.argmin()

    freq_l_30 = freqs_l[index_l_30]
    freq_r_30 = freqs_r[index_r_30]
    print((freq_r_30[0], max_val), (freq_r_30[0], min_val))
    ax.axline((freq_l_30, max_val), (freq_l_30, min_val), color="green")
    ax.axline((freq_r_30[0], max_val), (freq_r_30[0], min_val), color="green")

    plt.ylim([float(min_val), float(max_val)])

    print("max. val [dB]:", max_val)
    print("f_cut [MHz] (left, right):", freq_l_3, freq_r_3[0])
    print("f_30dB [MHz] (left, right):", freq_l_30, freq_r_30[0])
    print("BW_3dB [MHz]: ", freq_r_3[0] - freq_l_3)
    print("BW_30dB [MHz]: ", freq_r_30[0] - freq_l_30)

    y_ticks_n = linspace(float(min_val), float(max_val), num=11)
    plt.yticks(list(range(-5, -55, -5)))
    plt.grid()
    plt.xlim([800, 1100])
    plt.show()

