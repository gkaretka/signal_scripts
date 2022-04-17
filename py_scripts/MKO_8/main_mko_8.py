import matplotlib.pyplot as plt

x = [
    0.25,
    0.5,
    0.75,
    1,
]

y0 = [
    0.422,
    0.844,
    1.265,
    1.687,
]

y1 = [
    7.472,
    14.944,
    22.415,
    29.887,
]

plt.plot(x, y0, label="BW 1.4 MHz", linewidth=3, linestyle="dotted")
plt.plot(x, y1, label="BW 20 MHz", linewidth=3)
plt.title("Porovnanie QPSK v závislosti na rôznych kódových pomeroch")
plt.ylabel("Throughput [Mbit/s]")
plt.xlabel("CR (Code Rate) [-]")
plt.legend()
plt.show()


