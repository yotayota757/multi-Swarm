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

    # file_name = input("入力ファイル名を入力してください")
    out_graph = input("出力画像名を入力してください")
    # file_path = file_name + ".csv"

    Cuckoo = "Cuckoo.csv"
    PSO = "PSO.csv"
    Pro = "Pro.csv"

    # 縦軸の最大値
    # plt.ylim(0.0, 0.0001)

    # ラベル
    x_label = "Iteration"
    y_label = "Fitness"

    # 桁
    plt.gca().ticklabel_format(style="sci", scilimits=(0, 0), axis="y")

    #ファイル確認部
    if os.path.exists(Cuckoo) == 0:
        print (Cuckoo+"を参照できません")
        exit()
    else:
        print(Cuckoo+"を参照しています")

    if os.path.exists(PSO) == 0:
        print (PSO+"を参照できません")
        exit()
    else:
        print(PSO+"を参照しています")

    if os.path.exists(Pro) == 0:
        print (Pro+"を参照できません")
        exit()
    else:
        print(Pro+"を参照しています")

    #ファイル読み込み部(pandasでcsv読み込みしています)
    data_cuckoo = pd.read_csv(Cuckoo)
    data_pso = pd.read_csv(PSO)
    data_pro = pd.read_csv(Pro)
    # print (data)
    '''このように表示されます
    |  1  |  2  |  3  | ... | n - 1 |  n  |
    |  f  |  f  |  f  | ... |   f   |  f  | <-  f = fitness
    '''

    # pandas形式のデータをnumpy形式にして配列に格納
    vertical_cuckoo = np.array(data_cuckoo.values[0])
    vertical_pso = np.array(data_pso.values[0])
    vertical_pro = np.array(data_pro.values[0])
    '''このように表示される
    array([f^0,f^1,f^2,...,f^(n-2),f^(n-1)])
    '''

    #pandas data_frame の列の長さ与えて横軸の配列を作成
    horizontal_cuckoo = np.arange(len(data_cuckoo.columns))
    horizontal_pso = np.arange(len(data_pso.columns))
    horizontal_pro = np.arange(len(data_pro.columns))
    '''このように作成される
    array([0,1,2,3,...,n-2,n-1])
    '''

    plt.plot(horizontal_cuckoo,vertical_cuckoo,label = "Cuckoo")
    plt.plot(horizontal_pso,vertical_pso,label = "PSO")
    plt.plot(horizontal_pro,vertical_pro,label = "Proposed")
    plt.legend()
    plt.xlabel(x_label,fontsize=18)
    plt.ylabel(y_label,fontsize=18)
    plt.yscale('log')
    # plt.show()
    plt.savefig(out_graph + ".png")


