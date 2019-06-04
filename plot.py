# -*- coding: utf-8 -*-
from matplotlib import cm
from matplotlib import pyplot as plt
import math
import numpy as np
import os
import sys
import glob

# def find_all_files(directory):
#     for root, dirs, files in os.walk(directory):
#         yield root
#         for file in files:
#         	if file == (*.csv):
# 	            yield os.path.join(root, file)
def rastrigin(*X, **kwargs):
  A = kwargs.get('A', 10)
  return A*len(X) + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])

def main(file_name):
  each_population = 30
  pso_data = np.genfromtxt(file_name,delimiter=",",max_rows=each_population)
  cs_data = np.genfromtxt(file_name,delimiter=",",skip_header=each_population,max_rows=each_population)
  de_data = np.genfromtxt(file_name,delimiter=",",skip_header=each_population*2)
  name = file_name.replace(".csv","")
  fig_name = name.zfill(6)
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)

  # ヒートマップ用の値（配列）
  X = np.arange(-5.12, 5.12, 0.01)
  Y = np.arange(5.12, -5.12, -0.01)
  X,Y = np.meshgrid(X, Y)
  # 背景関数
  Z = rastrigin(X, Y, A=10)
  # ヒートマップの生成
  ax.imshow(Z, cmap=cm.rainbow, extent =[-5.12, 5.12, -5.12, 5.12])

  # 解集団のプロット
  ax.scatter(pso_data[:,0]/100, pso_data[:,1]/100, c = 'b',alpha=0.5) # １列目のデータをx軸の値、2列目のデータをy軸の値として与える。
  ax.scatter(cs_data[:,0]/100, cs_data[:,1]/100, c = 'm',alpha=0.5)
  ax.scatter(de_data[:,0]/100, de_data[:,1]/100, c = 'k',alpha=0.5)

  ax.set_xlabel('x_1') # x軸
  ax.set_ylabel('x_2') # y軸
  # plt.show() # グラフの描画
  plt.ylim(-5.12,5.12)
  plt.xlim(-5.12,5.12)
  # plt.grid(color='gray',linestyle="dashed")
  fig.savefig("../../figure/" + fig_name + ".png")
  plt.close()

  sys.stdout.write("\r" + fig_name + ".png : 出力完了!")

if __name__ == '__main__':
  os.chdir("./results/position/0/")
  files = glob.glob("*.csv")
  for file in files:
    main(file)