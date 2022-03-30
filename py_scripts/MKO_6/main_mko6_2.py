import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

files_1 = ["11", "22", "33", "44", "55", "66", "77", "88", "99", "100"]
files_2 = ["2200", "2211", "5500", "77001"]
condts_1 = ["LoS 1", "LoS 2", "LoS 3", "LoS 4", "LoS 5", "LoS 6", "LoS 7", "LoS 8", "LoS 9", "LoS 10"]
condts_2 = ["Obstacle (human)", "Obstacle (ipad)", "Obstacle (wall)", "Change of polarization"]

path = "data/"

o_file_1 = "output_1.dat"
o_file_2 = "output_2.dat"

preprocess = False

if preprocess:
    # file 1
    txt = ""
    for i in range(len(files_1)):
        print("File: " + str(i))
        _fr = open(path + files_1[i], "r")

        lines_txt = ""
        lines = _fr.readlines()
        _fr.close()

        cnt = 0
        for j in range(len(lines)):
            if cnt != 0 or i == 0:
                lines_txt += lines[j][:-2] + ";" + condts_1[i] + "\n"
            cnt += 1

        txt += lines_txt
    _fw = open(path + o_file_1, "w")
    _fw.write(txt)
    _fw.close()

    # file 2
    txt = ""
    for i in range(len(files_2)):
        print("File: " + str(i))
        _fr = open(path + files_2[i], "r")

        lines_txt = ""
        lines = _fr.readlines()
        _fr.close()

        cnt = 0
        for j in range(len(lines)):
            if cnt != 0 or i == 0:
                lines_txt += lines[j][:-2] + ";" + condts_2[i] + "\n"
            cnt += 1

        txt += lines_txt
    _fw = open(path + o_file_2, "w")
    _fw.write(txt)
    _fw.close()

power = 0

data_1 = pd.read_csv(path + o_file_1, sep=";")
data_1["Frequency [MHz]"] = data_1["Frequency [Hz]"] / 10**6
data_1["Attenuation [dB]"] = power - data_1["Attenuation [dB]"]
print(data_1.head())

data_2 = pd.read_csv(path + o_file_2, sep=";")
data_2["Frequency [MHz]"] = data_2["Frequency [Hz]"] / 10**6
data_2["Attenuation [dB]"] = power - data_2["Attenuation [dB]"]
print(data_2.head())

fig, ax = plt.subplots()
sns.lineplot(data=data_1, x="Frequency [MHz]", y="Attenuation [dB]", hue="Conditions", ax=ax)
plt.grid()

fig2, ax2 = plt.subplots()
sns.lineplot(data=data_2, x="Frequency [MHz]", y="Attenuation [dB]", hue="Conditions", ax=ax2)
plt.grid()
plt.show()