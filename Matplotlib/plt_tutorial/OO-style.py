# author: roczhang
# file: OO-style.py
# time: 2021/04/19

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.set_ylabel('y label')
ax.set_xlabel('x label')
ax.set_title('Simple Plot')
ax.legend()