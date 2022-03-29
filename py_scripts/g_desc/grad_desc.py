import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns


pts_cnt = 10


def mse(_y, _yh):
    return np.square(_y - _yh).mean()


# linear regression ax + b
def calc_deriv(_pts_x, _pts_y, _a, _b):
    _sum_a = 0
    _sum_b = 0
    for i in range(len(_pts_x)):
        _sum_b += (_pts_x[i]*_a + _b) - _pts_y[i]
        _sum_a += ((_pts_x[i] * _a + _b) - _pts_y[i]) * _pts_x[i]

    return _sum_a, _sum_b


def calc_reggression(pts_x, pts_y):
    a = 1
    b = 1
    alpha = 0.01

    epsilon = 0.001
    max_iter = 100000

    As = []
    Bs = []
    iter = []
    prev_err = 100000
    current_iter = 0
    while prev_err > epsilon and max_iter > current_iter:
        sum_a, sum_b = calc_deriv(pts_x, pts_y, a, b)
        a = a - alpha * (1/pts_cnt)*sum_a
        b = b - alpha * (1/pts_cnt)*sum_b

        As.append(a)
        Bs.append(b)
        iter.append(current_iter)

        """if (abs(prev_err - mse(pts_y, np.array(pts_x) * a + b))) < epsilon:
            break
        else:
            prev_err = mse(pts_y, np.array(pts_x) * a + b)
        """
        current_iter += 1

    return a, b, As, Bs


fig, axs = plt.subplots(nrows=2, ncols=2)
for k in range(0, 2):
    for j in range(0, 2):
        range_x = (10, 15)
        range_y = (2, 3)

        _pts_x = []
        _pts_y = []
        for i in range(pts_cnt):
            _x = rd.uniform(range_x[0], range_x[1])
            _y = rd.uniform(range_y[0], range_y[1])
            _pts_x.append(_x)
            _pts_y.append(_y)

        _pts_x = np.array(_pts_x)

        x_max =  np.max(_pts_x)

        _pts_x /= x_max

        a, b, As, Bs = calc_reggression(_pts_x, _pts_y)
        x = np.arange(0, 15/x_max, 0.1)
        y = x * a + b

        ys = []
        xs = []
        iter = []
        _itr = 0

        for i in range(0, len(As), 50):
            ys = np.concatenate((np.array(ys), x*As[i] + Bs[i]), axis=0)
            xs = np.concatenate((np.array(xs), np.array(x)), axis=0)

            for m in range(len(x)):
                iter.append(_itr)
            _itr += 50

        datas = pd.DataFrame(data={'iter': iter, 'x': xs, 'y': ys})

        axs[j][k].scatter(_pts_x, _pts_y)
        #sns.lineplot(data=datas, x="x", y="y", hue="iter", ax=axs[j][k])
        axs[j][k].plot(x, y, color="red")

plt.show()