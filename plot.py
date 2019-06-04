# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import os
import glob

# def find_all_files(directory):
#     for root, dirs, files in os.walk(directory):
#         yield root
#         for file in files:
#         	if file == (*.csv):
# 	            yield os.path.join(root, file)

def main(file_name):
  data = np.genfromtxt(file_name,delimiter=",")
  name = file_name.replace(".csv","")
  fig_name = name.zfill(14)
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  ax.scatter(data[:,0], data[:,1]) # １列目のデータをx軸の値、3列目のデータをy軸の値として与える。
  ax.set_xlabel('x_1') # x軸
  ax.set_ylabel('x_2') # y軸
  # plt.show() # グラフの描画
  plt.ylim(-512,512)
  plt.xlim(-512,512)
  plt.grid(color='gray',linestyle="dashed")
  fig.savefig("fig" + os.sep + fig_name + ".png")
  plt.close()
  print (fig_name + ".png : 出力完了!")

if __name__ == '__main__':
    # main()
    files = glob.glob("*.csv")
    for file in files: 
        # print (file)
    	main(file)
