# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random

N = 100 # データ点の個数

np.random.seed(0) # データ点のために乱数列を固定(シードに 0 を与える場合)
X = np.random.randn(N, 2) # ランダムなN*2行列を生成 = 2次元空間上のランダムな点 N個

# データ点を特徴ベクトルに変換
def phi(x, y):
  return np.array([x, y, 1])

def h(x, y):
    return 5 * x + 3 * y - 1 # 適当に決めた真の分離平面 5x + 3y = 1

T = np.array([1 if h(x, y) > 0 else - 1 for x, y in X])
w = np.zeros(3) # 3次の0ベクトル

for i in range(1000):
  list = range(N)
  random.shuffle(list)

  misses = 0 # 予測を外した回数
  for n in list:
    x_n, y_n = X[n, :]
    t_n = T[n]

    # 予測
    predict = np.sign((w * phi(x_n, y_n)).sum())

    # 予測が不正解なら，パラメータを更新する
    if predict != t_n:
      w += t_n * phi(x_n, y_n)
      misses += 1

  # 予測が外れる点が無くなったら学習終了(ループを抜ける)
  if misses == 0:
      break

# 図を描くための準備
seq = np.arange(-3, 3, 0.02)
xlist, ylist = np.meshgrid(seq, seq)
zlist = np.array([np.sign((w * phi(x, y)).sum()) for x, y in zip(xlist, ylist)])

# 分離平面と散布図を描画
plt.pcolor(xlist, ylist, zlist, alpha=0.2, edgecolors='white')
plt.plot(X[T== 1,0], X[T== 1,1], 'o', color='red')
plt.plot(X[T==-1,0], X[T==-1,1], 'o', color='blue')
plt.show()