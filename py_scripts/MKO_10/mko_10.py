import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

task = 1

if task == 1:
    # task 1
    step = 5
    max_att = 45
    int_att = 0
    att = np.arange(0, max_att+step, step)
    att = np.concatenate((att, att), axis=0)

    att_meas_0 = np.array([-26.7, -30.9, -35.1, -40.3, -45.1, -51.0, -55.8, -60.5, -64.7, -69.3])
    att_res_bw_200_sf_12 = np.apply_along_axis(lambda x: x + int_att, 0, att_meas_0)

    att_meas_1 = np.array([-28.9, -32.8, -38.8, -43.7, -48.8, -52.9, -58.3, -63.1, -68.4, -70.7])
    att_res_bw_1600_sf_5 = np.apply_along_axis(lambda x: x + int_att, 0, att_meas_1)

    # latex export
    for i in range(len(att_meas_1)):
        print(str("{:.1f}".format(float(att_meas_1[i]))) + " & ", end="")

    att_merged = np.concatenate((att_res_bw_200_sf_12, att_res_bw_1600_sf_5), axis=0)

    att_0_label = ["200kHz, SF12"] * len(att_res_bw_200_sf_12)
    att_1_label = ["1600kHz, SF5"] * len(att_res_bw_1600_sf_5)
    att_merged_labels = np.concatenate((np.array(att_0_label), np.array(att_1_label)), axis=0)

    data = pd.DataFrame(data={'Attenuation [dB]': att, 'Power [dBm]': att_merged, 'Labels': att_merged_labels})

    sns.lineplot(data=data, x="Attenuation [dB]", y="Power [dBm]", style="Labels")
    plt.grid()
    plt.show()

elif task == 2:
    step = 5
    max_att = 45
    int_att = 10
    att = np.arange(0, max_att+step, step)
    att = np.concatenate((att, att), axis=0)

    rssi_0 = np.array([-27, -32, -37, -41, -47, -52, -56, -62, -66, -72])
    rssi_1 = np.array([-27, -32, -37, -42, -46, -52, -56, -62, -67, -72])
    att_merged = np.concatenate((rssi_0, rssi_1), axis=0)

    # latex export
    for i in range(len(rssi_0)):
        print("\multicolumn{1}{l}{" + str("{:.1f}".format(float(rssi_0[i]))) + "} " + " & ", end="")

    print("")

    for i in range(len(rssi_1)):
        print("\multicolumn{1}{l}{" + str("{:.1f}".format(float(rssi_1[i]))) + "} " + " & ", end="")

    att_0_label = ["200kHz, SF12"] * len(rssi_0)
    att_1_label = ["1600kHz, SF5"] * len(rssi_1)
    att_merged_labels = np.concatenate((np.array(att_0_label), np.array(att_1_label)), axis=0)

    data = pd.DataFrame(data={'Attenuation [dB]': att, 'RSSI [dBm]': att_merged, 'Labels': att_merged_labels})

    sns.lineplot(data=data, x="Attenuation [dB]", y="RSSI [dBm]", style="Labels")
    plt.grid()
    plt.show()
