#メイン関数
import individual
import swarm
import random
import function
import numpy as np
import math
import csv
import sys
import time
import os

"""パラメータたち"""
Dimension = 2# 次元数
Iteration = 10 #最大世代数
Trial = 1# 試行回数
rnd = np.random
max_range = 500.0
min_range = -500.0
g_best_position = (rnd.rand(Dimension) * (max_range - min_range)  + min_range)
g_best_value = 0
seed = 0
global gen


if os.path.exists("results"+os.sep+"position"):
    pass
else:
    os.mkdir("results"+os.sep+"position")

if os.path.exists("results"+os.sep+"direction"):
    pass
else:
    os.mkdir("results"+os.sep+"direction")


"""ファイル作成"""
Files = []
# 結果用ファイル作成
CuckooMod_results = open("results" + os.sep + "CS_Mod" + os.sep + "CuckooMod_results.csv", "w")
CuckooMod_results_writer = csv.writer(CuckooMod_results, lineterminator="\n")

Files.append(CuckooMod_results)

def Initialize(seed):
    gen = 0
    g_best_position = (rnd.rand(Dimension) * (max_range - min_range)  + min_range)
    g_best_value = function.SingleMoving(g_best_position, gen)
    rnd.seed(seed=seed)

def FileClose():#すべての出力用ファイルを閉じる
    for file in Files:
        file.close()

def OutputPosition(swarm, name, gen, seed):
    # print(name)
    if os.path.exists("results"+os.sep+"position"+os.sep+str(name)):
        pass
    else:
        os.mkdir("results"+os.sep+"position"+os.sep+str(name))

    if os.path.exists("results"+os.sep+"position" + os.sep + str(name) + os.sep + str(seed)):
        pass
    else:
        os.mkdir("results"+os.sep +"position" + os.sep + str(name) + os.sep + str(seed))

    position = open("results"+os.sep+ "position" + os.sep + str(name) + os.sep + str(seed) + os.sep + str(gen).zfill(6) +"_position.csv", "w")
    position_writer = csv.writer(position, lineterminator="\n")
    for i in range(swarm.population):
        position_writer.writerow(swarm.solution_array[i].position)
    position.close()

def OutputDirection(swarm, name, gen, seed):
    # print(name)
    if os.path.exists("results"+os.sep+"direction" + os.sep + str(name)):
        pass
    else:
        os.mkdir("results"+os.sep+"direction" + os.sep + str(name))

    if os.path.exists("results"+os.sep+"direction" + os.sep + str(name) + os.sep + str(seed)):
        pass
    else:
        os.mkdir("results"+os.sep +"direction" + os.sep + str(name) + os.sep + str(seed))

    direction = open("results"+os.sep+ "direction" + os.sep + str(name) + os.sep + str(seed) + os.sep + str(gen).zfill(6) +"_direction.csv", "w")
    direction_writer = csv.writer(direction, lineterminator="\n")
    for i in range(swarm.population):
        direction_writer.writerow([np.degrees(swarm.solution_array[i].vector)])
    direction.close()

class Mod(swarm.Swarm):
    def __init__(self,n,dim,t):
        swarm.Swarm.__init__(self,n,dim,t)
        self.solution_array = []  # 個体を入れる配列
        for i in range(n):#各個体の挿入
            self.solution_array.append(solution(dim,t))
        self.direction =0
        self.step = 0

    def ReloadDirection(self):#各移動方向の平均を計算
        Sum = 0
        for i in self.individual_array:
            if i.dirFlag == 1:
                print(i.vector)
                Sum += i.vector
        self.direction = Sum / len(self.individual_array)

    def ReloadMod(self):#上位個体はdirectionに従い,下位個体は削除
        pass


class solution(individual.Individual):
    def __init__(self, dim, t):
        individual.Individual.__init__(self,dim,t)
        self.dirFlag = 1
        self.vector = rnd.rand() * np.pi



if __name__ == '__main__':
    for seed in range(Trial):  # seed = 試行回数
        print (seed+1)
        Initialize(seed)  # グローバルベストの座標と評価値を設定
        gen = 0
        CuckooMod = Mod(10,Dimension,gen)

        Cuckoo_fitness_list = []

        for gen in range(Iteration):# gen = 世代数
            sys.stdout.write("\r gen: %d" % gen)
            sys.stdout.write("\r fitness: %d" % CuckooMod.best_fitness)



            OutputPosition(CuckooMod,"Mod",gen,seed)
            OutputDirection(CuckooMod,"Mod",gen,seed)




    FileClose()