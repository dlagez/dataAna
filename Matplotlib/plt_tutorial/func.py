# author: roczhang
# file: func.py
# time: 2021/04/19

import matplotlib.pyplot as plt
import numpy as np


def my_pyplot(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_pyplot(ax, data1, data2, {"marker": "x"})

fig, (ax1, ax2) = plt.subplots(1, 2)
my_pyplot(ax1, data1, data2, {"marker": "x"})
my_pyplot(ax2, data3, data4, {"marker": "o"})

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp

y = np.random.rand(10000)
y[5000:] *= 2

y[np.geomspace(10, 5000, 400).astype(int)] = -1
mlp.rcParams['path.simplify'] = True

mlp.rcParams['path.simplify'] = 0.0
plt.plot(y)
plt.show()

mlp.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()
