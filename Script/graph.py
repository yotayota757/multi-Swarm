#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:44:28 2017
@author: YutaUmenai
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

if __name__ == '__main__':

    file_name = input("入力ファイル名を入力してください")
    out_graph = input("出力画像名を入力してください")
    file_path = file_name + ".csv"


    # 縦軸の最大値
    # plt.ylim(0.0, 0.0001)

    # ラベル
    x_label = "Iteration"
    y_label = "Fitness"

    # 桁
    plt.gca().ticklabel_format(style="sci", scilimits=(0, 0), axis="y")

    #ファイル確認部
    if os.path.exists(file_path) == 0:
        print ("対象ファイルを参照できません")
        exit()
    else:
        print("対象ファイルを参照しています")

    #ファイル読み込み部(pandasでcsv読み込みしています)
    data = pd.read_csv(file_path)
    # print (data)
    '''このように表示されます
    |  1  |  2  |  3  | ... | n - 1 |  n  |
    |  f  |  f  |  f  | ... |   f   |  f  | <-  f = fitness
    '''

    # pandas形式のデータをnumpy形式にして配列に格納
    vertical = np.array(data.values[0])
    '''このように表示される
    array([f^0,f^1,f^2,...,f^(n-2),f^(n-1)])
    '''

    #pandas data_frame の列の長さ与えて横軸の配列を作成
    horizontal = np.arange(len(data.columns))
    '''このように作成される
    array([0,1,2,3,...,n-2,n-1])
    '''

    plt.plot(horizontal,vertical)
    plt.yscale('log')
    # plt.show()
    plt.savefig(out_graph + ".png")


