# author:roczhang
# file:data_NearMiss.py
# time:2021/04/13
from collections import Counter
# 读取mat文件
import scipy.io as scio

dataFile = '/home/roczhang/D/file/data/SVM/data_NearMiss/2012/X.mat'
data = scio.loadmat(dataFile)['']

from imblearn.under_sampling import NearMiss
nm1 = NearMiss(version=1)
X_resampled_nm1, y_resampled = nm1.fit_resample(X, y)
print(sorted(Counter(y_resampled).items()))

