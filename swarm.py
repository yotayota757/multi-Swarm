#ライブラリ
import numpy as np
#ファイル
import individual
import operator
import sys
import os
import  main

class Swarm:
    def __init__(self,n,t):
        self.population = n#群中の個体数
        self.individual_array = []#個体を入れる配列
        for i in range(n):#各個体の挿入
            self.individual_array.append(individual.Individual(dim,t))
        self.individual_array.sort(key=operator.attrgetter('fitness'))
        self.best_fitness = self.individual_array[0].fitness#群の中の最大評価値
        self.best_fitness_position = self.individual_array[0].position
        # self.SetAveFitness()#群の中の平均評価値
        # self.best_fitness_t = 0
        # self.ave_fitness_t = 0
        # self.contribution = 0

    def PrintSwarm(self):
        # print ("個体数：",self.population)
        # print ("最大評価値：",self.best_fitness)
        # print ("平均評価値：",self.ave_fitness)
        for i in range(self.population):
            #print("個体",i+1,"の：fitness",self.individual_array[i].fitness)
            print("座標["+ str(i) +"]：", self.individual_array[i].position,", 速度:" ,self.individual_array[i].velocity, ", 評価値:",self.individual_array[i].fitness)
            # print("partialbest_position:",self.individual_array[i].partial_best_position)

    def SetAveFitness(self):
        sum = 0
        for i in range(len(self.individual_array)):
            sum = sum + self.individual_array[i].fitness
        self.ave_fitness = sum / len(self.individual_array)

    def SetDiv(self):#一つ前のアベレージとベストを保存
        self.ave_fitness_t = self.ave_fitness
        self.best_fitness_t = self.best_fitness

    def SetContribute(self):
        # self.contribution = abs(self.best_fitness - self.best_fitness_t) / self.population
        self.contribution = abs(self.ave_fitness - self.ave_fitness_t) / self.population

    def Sort(self):
        self.individual_array.sort(key=operator.attrgetter('fitness'))#配列のソート

    def SortAndReload(self,t):#個体数の更新，配列のソート，平均評価値，最良評価値
        self.AllCalculation(t)
        self.population = len(self.individual_array)#個体数の更新
        self.individual_array.sort(key=operator.attrgetter('fitness'))#配列のソート
        # self.SetContribute()
        # self.SetAveFitness()
        if self.best_fitness > self.individual_array[0].fitness:
            self.best_fitness = self.individual_array[0].fitness
            self.best_fitness_position = self.individual_array[0].position
            #バグっぽい
            #self.best_fitness_position = self.individual_array[0].partial_best_position

    def SetPopulation(self):
        self.population = len(self.individual_array)#個体数の更新

    def AllCalculation(self,t):#評価値計算
        for i in range(len(self.individual_array)):
            self.individual_array[i].CalcIndividual(t)

    def AllReloadLevy(self,t):
        self.individual_array[0].ReloadLevyLocal(t)
        for i in range(1,len(self.individual_array)):
            self.individual_array[i].ReloadLevy(t)

    def AllReloadLevyLocal(self,t):
        for i in range(len(self.individual_array)):
            self.individual_array[i].ReloadLevyLocal(t)

    def AllReloadPSO(self):
        for i in range(len(self.individual_array)):
            self.individual_array[i].ReloadPSO()

    def AllReloadVelocity(self):
        for i in range(len(self.individual_array)):
            self.individual_array[i].ReloadVelocity(self.best_fitness_position)
        # input()

    def CompIndividual(self,i,num,t):
        # print (self.individual_array[i].fitness)
        # print (self.individual_array[num].fitness)
        if(self.individual_array[i].fitness < self.individual_array[num].fitness):
            self.individual_array[num].position = self.individual_array[i].position
            self.individual_array[num].fitness = main.Calculation(self.individual_array[num].position,t)
        if (self.individual_array[num].fitness < self.individual_array[i].fitness):
            self.individual_array[i].position = self.individual_array[num].position
            self.individual_array[i].fitness = main.Calculation(self.individual_array[i].position, t)
            # print ("###############更新#################")
            # print(self.individual_array[i].fitness)
            # print(self.individual_array[num].fitness)
            # print ("###################################")

    def DeleteIndividual(self):
        for i in range(1,self.population):#最良解以外の解全てについて25%で削除
            # print (i)
            if main.rnd.rand() < 0.25:
                #ランダムに初期化
                self.individual_array[i].position \
                     = (main.rnd.rand(self._dim) * (main.max_range - main.min_range)  + main.min_range)
                # self.individual_array[i].position = self.best_fitness_position
                # self.individual_array[i].reload_levy(main.gen)

    def Cuckoo(self,t):
        for i in range(self.population):
            # print (i)
            num = main.rnd.randint(0,self.population)
            if i == 0:
                self.individual_array[i].ReloadLevyLocal(t)
                self.CompIndividual(i,num,t)
            else:
                self.individual_array[i].ReloadLevy(t)
                self.CompIndividual(i,num,t)

    def GetBestPosition(self):
        return self.best_fitness_position


if __name__ == '__main__':
    test = Swarm(5,2)
    test.PrintSwarm()
    print (test.SetAveFitness())
    print (os.sep)
