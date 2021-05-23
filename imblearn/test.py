# author:roczhang
# file:test.py
# time:2021/04/13
import scipy.io as scio

import scipy

from imblearn.over_sampling import SMOTE

X = scio.loadmat("D:\workspace\matlab/aa/X2012.mat")["DATA"]

y = scio.loadmat("D:\workspace\matlab/aa/y2012.mat")["label"]

print(X.shape)  # (1447, 448)

print(y.shape)  # (1447, 1)

# 但是，SMOTENC仅当数据是数字和分类特征的混合时才有效。如果数据仅由分类数据组成，则可以使用SMOTEN变体[ CBHK02 ]。该算法有两种变化方式：

# 最近的邻居搜索不依赖于欧几里得距离。实际上，使用了在该类中也实现的值差度量（VDM） ValueDifferenceMetric。

# 生成一个新样本，其中每个特征值对应于在属于同一类的邻居样本中看到的最常见类别。

X_resampled, y_resampled = SMOTE().fit_resample(X, y)

print(X_resampled.shape)  # (2802, 448)

print(y_resampled.shape)  # (2802,)

print(y_resampled[1000:2000])

# 保存文件

scipy.io.savemat('daset_sklearn/data_resampled/X_resampled2012.mat', {'X_resampled': X_resampled})

from sklearn import svm

# parameter

# c:正则化参数。正则化的强度与C成反比。必须严格为正。

# gamma: “ rbf”，“ poly”和“ Sigmoid”的内核系数。

model = svm.SVC(kernel='linear', C=1, gamma=1)

# fit: 根据给定的训练数据拟合SVM模型。

model.fit(X_resampled, y_resampled)

# Predict Output

# predicted= model.predict(x_test)

#