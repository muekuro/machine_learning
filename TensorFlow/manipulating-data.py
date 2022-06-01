# file __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow as tf

# load dataset
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
print(dftrain.head()) # 最初の5行表示
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')
print(dftrain.head()) # survivedが格納されていることを確認

print(dftrain.describe()) # データの詳細
print(dftrain.shape) # データの形状
# dftrain.age.hist(bins=20).plot()
# dftrain.sex.value_counts().plot(kind='barh')
# dftrain['class'].value_counts().plot(kind='barh')
pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh')
plt.show()