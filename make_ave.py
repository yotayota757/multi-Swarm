
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv

if __name__ == '__main__':
    #ファイル確認部
    f_name = input("ファイル名を指定してください")
    out_file = input("出力ファイル名を指定してください")
    if os.path.exists("results" + os.sep + f_name +".csv") == 0:
        print (f_name + ".csvを参照できません")
        exit()
    else:
        print(f_name + ".csvを参照しています")

    print(f_name+ ".csvを変換しています．")
    data = pd.read_csv("results" + os.sep + f_name +".csv")

    l = len(data.columns)
    print (l)
    row = np.arange(len(data.columns)) 

    print ("平均値計算中")
    average = data.mean()

    #1次元の配列へ変換
    average_data = np.array(average)

    #行と列の変換
    average_data = average_data.T

    print("ファイル出力中")
    f = open(out_file + ".csv", "w")

    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(row)
    writer.writerow(average_data)

    f.close()

    print ("実行完了")


