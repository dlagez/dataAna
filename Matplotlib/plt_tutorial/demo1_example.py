# author: roczhang
# file: demo1_example.py
# time: 2021/04/19

import matplotlib.pyplot as plt
import numpy as np
import pandas

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 3, 2])

plt.plot([1, 2, 3, 4], [1, 4, 3, 2])

fig = plt.figure()
fig, ax = plt.subplots()
fig, axs = plt.subplots(2, 2)

a = pandas.DataFrame(np.random.rand(4, 5), columns=list('abcde'))
a_asarray = a.values

b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)

