#メイン関数
import individual as ind
import function as fn
import numpy as np
import math
import csv
import sys
import copy
import os
from config import Config as cf
import pandas as pd




if os.path.exists("results"):
    pass
else:
    os.mkdir("results")

if os.path.exists("results"+os.sep+"position"):
    pass
else:
    os.mkdir("results"+os.sep+"position")

# For Output
# results = open("results" + os.sep + "results.csv", "w")
# results_writer = csv.writer(results, lineterminator="\n")
# pso_results = open("results" + os.sep + "pso_results.csv", "w")
# pso_results_writer = csv.writer(pso_results, lineterminator="\n")
# cs_results = open("results" + os.sep + "cs_results.csv", "w")
# cs_results_writer = csv.writer(cs_results, lineterminator="\n")
# de_results = open("results" + os.sep + "de_results.csv", "w")
# de_results_writer = csv.writer(de_results, lineterminator="\n")

# OutputFiles = []
# OutputFiles.append(results)
# OutputFiles.append(pso_results)
# OutputFiles.append(cs_results)
# OutputFiles.append(de_results)

class Best:
    def __init__(self, b_fitness, b_position):
        self.__best_fitness = b_fitness
        self.__best_position = b_position

    # best fitness
    def get_best_fitness(self):
        return self.__best_fitness

    def set_best_fitness(self,fitness):
        self.__best_fitness = fitness

    # best position
    def get_best_position(self):
        return self.__best_position

    def set_best_position(self,position):
        self.__best_position = position



"""サブ関数"""
def OutputPosition(swarm, name, gen):
    # print(name)
    # if os.path.exists("results" + os.sep + str(name)):
    #     position = open("results" + os.sep + str(name) + os.sep + str(gen).zfill(6) +"_position.csv", "w")
    #     position_writer = csv.writer(position, lineterminator="\n")
    #     for i in range(swarm.population):
    #         position_writer.writerow(swarm.individual_array[i].position.tolist())
    #     position.close()
    # else:
    #     os.mkdir("results" + os.sep + str(name))
    #     position = open("results" + os.sep + str(name) + os.sep + str(gen).zfill(6) +"_position.csv", "w")
    #     position_writer = csv.writer(position, lineterminator="\n")
    #     for i in range(swarm.population):
    #         position_writer.writerow(swarm.individual_array[i].position.tolist())
    #     position.close()
    if not(os.path.exists("results" + os.sep + str(name))):
        os.mkdir("results" + os.sep + str(name))
    position = open("results" + os.sep + str(name) + os.sep + str(gen).zfill(6) +"_position.csv", "w")
    position_writer = csv.writer(position, lineterminator="\n")
    for i in range(swarm.population):
        position_writer.writerow(swarm.individual_array[i].position.tolist())
    position.close()

def Calc_Velocity(swarm):#各群の各個体の速度の総和
    sum_velocity = 0
    for num in range(len(swarm.individual_array)):#両手法導入の場合だと最終個体の速度が上がりすぎるのであまり意味なさげに見える
        sum_velocity = sum_velocity + np.linalg.norm(swarm.individual_array[num].velocity)
    return sum_velocity


def FileClose():#すべての出力用ファイルを閉じる
    for file in OutputFiles:
        file.close()

def UpdateBest(swarm_best, current):
    if (current.get_fitness() < swarm_best.get_best_fitness()):
        swarm_best.set_best_fitness(current.get_fitness())
        swarm_best.set_best_position(current.get_position())

def UpdateAllBest(all, pso, cs, de):
    if pso.get_best_fitness() < cs.get_best_fitness():
        if (pso.get_best_fitness() < de.get_best_fitness()):
            if(pso.get_best_fitness() < all.get_best_fitness()):
                all.set_best_position(pso.get_best_position())
                all.set_best_fitness(pso.get_best_fitness())
        else:
            if(de.get_best_fitness() < all.get_best_fitness()):
                all.set_best_position(de.get_best_position())
                all.set_best_fitness(de.get_best_fitness())
    else:
        if (cs.get_best_fitness() < de.get_best_fitness()):
            if(cs.get_best_fitness() < all.get_best_fitness()):
                all.set_best_position(cs.get_best_position())
                all.set_best_fitness(cs.get_best_fitness())
        else:
            if(de.get_best_fitness() < all.get_best_fitness()):
                all.set_best_position(de.get_best_position())
                all.set_best_fitness(de.get_best_fitness())

def fitness_update(fitness,best,improvement):
    if best > fitness:
        best = fitness
    improvement.append(best)
    return best,improvement

def main():
    for trial in range(cf.get_trial()):# seed = 試行回数
        np.random.seed(trial)

        if os.path.exists("results" + os.sep + "position" + os.sep + str(trial)):
            pass
        else:
            os.mkdir("results" + os.sep + "position" + os.sep + str(trial))

        results_list = [] # fitness list
        results_pso_list = []
        results_cs_list = []
        results_de_list = []

        pso_list = [] # pso list
        cs_list = [] # cs list
        de_list = []

        all_list = []

        eval = 0
        iteration = 0
        BestFitness = 10000
        improvement = []

        """Generate Initial Population"""
        for p in range(int(args[7])):
            pso_list.append(ind.Individual())
        for c in range(int(args[8])):
            cs_list.append(ind.Individual())
        for d in range(int(args[9])):
            de_list.append(ind.Individual())

        """Sort Array"""
        pso_list =  sorted(pso_list, key=lambda ID : ID.get_fitness())
        cs_list = sorted(cs_list,key=lambda ID : ID.get_fitness())
        de_list = sorted(de_list, key=lambda ID: ID.get_fitness())

        for i in range(len(pso_list)):
            all_list.append(pso_list[i])
            # print(pso_list[i].get_position())

        for i in range(len(cs_list)):
            all_list.append(cs_list[i])

        for i in range(len(de_list)):
            all_list.append(de_list[i])

        """Find Initial Best"""
        PSO_Best = Best(pso_list[0].get_fitness(), pso_list[0].get_position())
        CS_Best = Best(cs_list[0].get_fitness(), cs_list[0].get_position())
        DE_Best = Best(de_list[0].get_fitness(), de_list[0].get_position())

        """Find the Best"""
        if PSO_Best.get_best_fitness() < CS_Best.get_best_fitness():
            if(PSO_Best.get_best_fitness() < DE_Best.get_best_fitness()):
                ALL_Best = Best(PSO_Best.get_best_fitness(), PSO_Best.get_best_position())
            else:
                ALL_Best = Best(DE_Best.get_best_fitness(), DE_Best.get_best_position())
        else:
            if(CS_Best.get_best_fitness() < DE_Best.get_best_fitness()):
                ALL_Best = Best(CS_Best.get_best_fitness(), CS_Best.get_best_position())
            else:
                ALL_Best = Best(DE_Best.get_best_fitness(), DE_Best.get_best_position())

        for iteration in range(cf.get_iteration()):
            # if iteration == 150:
            #     BestFitness = 10000
            # cf.set_Rnd(np.random.randint(0,5000))
            # if(cf.get_function() == "ex21"):
            #     if(iteration >= 0 and iteration < 3000):
            #         if(iteration % 50 == 0):
            #             cf.set_Radisu(cf.get_Radius() + 1)
            # 環境変化後リセット用
            #
            # 記述
            #

            # if(iteration == 5000 or iteration == 10000):
	           #  """Generate Initial Population"""
	           #  for p in range(cf.get_population_size()):
	           #      pso_list.append(ind.Individual())
	           #      cs_list.append(ind.Individual())
	           #      de_list.append(ind.Individual())

            # 位置記録
            pos = open("results" + os.sep + "position" + os.sep + str(trial) + os.sep + str(iteration).zfill(6) + ".csv", "w")
            pos_writer = csv.writer(pos, lineterminator="\n")
            #
            # """Write Moved Position"""
            for i in range (len(all_list)):
                pos_writer.writerow(all_list[i].get_position())
                # print(all_list[i].get_position())

            # input()

            # 各群の解アップデート
            """>>>> PSO Update """
            for i in range(len(pso_list)):
                """Update Position"""
                pso_list[i].update_position()

                """Calculate Fitness"""
                pso_list[i].set_fitness(fn.calculation(pso_list[i].get_position(), iteration))

                """Update Personal Best # for minimize optimization"""
                if(pso_list[i].get_fitness() < fn.calculation(pso_list[i].get_p_best_position(),iteration)):
                    pso_list[i].set_p_best_fitness(pso_list[i].get_fitness())
                    pso_list[i].set_p_best_position(pso_list[i].get_position())

                """Update Global Best # for minimize optimization"""
                if (pso_list[i].get_fitness() < PSO_Best.get_best_fitness()):
                    PSO_Best.set_best_fitness(pso_list[i].get_fitness())
                    PSO_Best.set_best_position(pso_list[i].get_position())
                
                eval += 1
                BestFitness, improvement= fitness_update(fn.calculation(pso_list[i].get_position(),iteration),BestFitness,improvement)

            """<<<< End PSO """


            """>>>> CS Update """
            for i in range(len(cs_list)):
                cs_list[i].get_cuckoo()
                cs_list[i].set_fitness(fn.calculation(cs_list[i].get_position(),iteration))

                """random choice (say j)"""
                j = np.random.randint(low=0, high=len(cs_list)) # [say j]
                while (i == j):
                   j = np.random.randint(low=0, high=len(cs_list))  # [say j]

                # for minimize problem
                if(cs_list[i].get_fitness() < fn.calculation(cs_list[j].get_position(),iteration)):
                    cs_list[j].set_position(cs_list[i].get_position())
                    cs_list[j].set_fitness(cs_list[i].get_fitness())
                
                eval += 1
                BestFitness, improvement= fitness_update(fn.calculation(cs_list[j].get_position(),iteration),BestFitness,improvement)

            """Find the Best"""
            best_id = 0
            best_fitness = cs_list[0].get_fitness()
            for b in range(len(cs_list)):
                F = cs_list[b].get_fitness()
                if (F < best_fitness):
                    best_id = b
                    best_fitness = F

            """Abandon Solutions (exclude the best)"""
            for a in range(0,len(cs_list)):
                if (a != best_id): # To Keep the Best
                    r = np.random.rand()
                    if(r < cf.get_Pa()):
                        cs_list[a].abandon()
                        cs_list[a].set_fitness(fn.calculation(cs_list[a].get_position(),iteration))

            """<<<< End CS """


            """>>>> DE Update"""

            """Generate New Solutions"""
            for i in range(len(de_list)):

                candidate = copy.deepcopy(de_list[i])

                """select three points (a, b, c)"""
                a = np.random.randint(0, len(de_list))
                while (a == i):
                    a = np.random.randint(0, len(de_list))
                b = np.random.randint(0, len(de_list))
                while (b == i or a == b):
                    b = np.random.randint(0, len(de_list))
                c = np.random.randint(0, len(de_list))
                while (c == i or c == a or c == b):
                    c = np.random.randint(0, len(de_list))

                """Select Random Index (R)"""
                R = np.random.randint(0,cf.get_dimension())

                candidate.generate(a=de_list[a], b=de_list[b], c=de_list[c], R=R)

                """Calculate Solution"""
                candidate.set_fitness(fn.calculation(candidate.get_position(),iteration))
                de_list[i].set_fitness(fn.calculation(de_list[i].get_position(),iteration))

                if candidate.get_fitness() < de_list[i].get_fitness():
                    de_list[i] = copy.deepcopy(candidate)
                
                eval += 1
                BestFitness, improvement= fitness_update(fn.calculation(de_list[i].get_position(),iteration),BestFitness,improvement)

            de_list = copy.deepcopy(de_list)

            """<<<< End DE """


            """Sort Array"""

            all_list = []

            pso_list = sorted(pso_list, key=lambda ID: ID.get_fitness())
            cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())
            de_list = sorted(de_list, key=lambda ID: ID.get_fitness())

            for i in range(len(pso_list)):
                all_list.append(pso_list[i])

            for i in range(len(cs_list)):
                all_list.append(cs_list[i])

            for i in range(len(de_list)):
                all_list.append(de_list[i])

            PSO_Best.set_best_fitness(fn.calculation(PSO_Best.get_best_position(),iteration))
            CS_Best.set_best_fitness(fn.calculation(CS_Best.get_best_position(), iteration))
            DE_Best.set_best_fitness(fn.calculation(DE_Best.get_best_position(), iteration))
            ALL_Best.set_best_fitness(fn.calculation(ALL_Best.get_best_position(), iteration))

            # print("rnd",cf.get_Rnd())
            # print(fn.multimoving(PSO_Best.get_best_position(), cf.get_Rnd()))
            # print("pso", PSO_Best.get_best_fitness())
            # print("cs", CS_Best.get_best_fitness())
            # print("de", DE_Best.get_best_fitness())

            cs_list[0].set_fitness(fn.calculation(cs_list[0].get_position(),iteration))

            """Update Best"""
            UpdateBest(PSO_Best, pso_list[0])
            UpdateBest(CS_Best, cs_list[0])
            UpdateBest(DE_Best, de_list[0])

            UpdateAllBest(ALL_Best,PSO_Best,CS_Best,DE_Best)


            # 一番いいものを挿入
            # if(iteration % 100 == 0):
            pso_list[-1].set_position(ALL_Best.get_best_position())
            cs_list[-1].set_position(ALL_Best.get_best_position())
            de_list[-1].set_position(ALL_Best.get_best_position())

            """>>>> Update PSO """
            for i in range(len(pso_list)):
                """Reload Velocity"""
                pso_list[i].update_velocity(PSO_Best.get_best_position())

            """<<<< End PSO """

            # print("all_pos",ALL_Best.get_best_position())
            # print(fn.multimoving(ALL_Best.get_best_position(), cf.get_Rnd()))
            # print("all_fit",ALL_Best.get_best_fitness())

            ALL_Best.set_best_fitness(fn.calculation(ALL_Best.get_best_position(),iteration))

            sys.stdout.write("\r Trial:%3d , Iteration:%7d, BestFitness:%.6f" % (trial , iteration, ALL_Best.get_best_fitness()))
            # print()
            # input()

            results_list.append(str(ALL_Best.get_best_fitness()))
            # results_pso_list.append(str(PSO_Best.get_best_fitness()))
            # results_cs_list.append(str(CS_Best.get_best_fitness()))
            # results_de_list.append(str(DE_Best.get_best_fitness()))

        results_writer.writerow(results_list)
        # pso_results_writer.writerow(results_pso_list)
        # cs_results_writer.writerow(results_cs_list)
        # de_results_writer.writerow(results_de_list)

        all = pd.DataFrame(improvement)
        all.to_csv("./results/fitness_by_evaluation/trial"+str(trial)+".csv")

    """File Close"""
    FileClose()


if __name__ == '__main__':
    # pso_list = []  # pso list
    # cs_list = []  # cs list
    # de_list = []
    #
    # list = []
    #
    # for p in range(cf.get_population_size()):
    #     pso_list.append(ind.Individual())
    #     cs_list.append(ind.Individual())
    #     de_list.append(ind.Individual())
    #
    #
    # for i in range(cf.get_population_size()):
    #     print("pso[",i,"]",pso_list[i].get_position())
    #     list.append(pso_list[i])
    #
    # for i in range(cf.get_population_size()):
    #     print("cs[", i, "]", cs_list[i].get_position())
    #     list.append(cs_list[i])
    #
    # for i in range(cf.get_population_size()):
    #     print("de[", i, "]", de_list[i].get_position())
    #     list.append(de_list[i])
    #
    # print("--------------------------------------------------")
    #
    # for l in range(len(list)):
    #     print("list[", l, "]", list[l].get_position())
    #
    # print("###--------------------------------------------------")
    # cs_list[0].get_cuckoo()
    #
    # for i in range(cf.get_population_size()):
    #     print("cs[", i, "]", cs_list[i].get_position(), "id:", id(cs_list[i]))
    #
    # for l in range(len(list)):
    #     print("list[", l, "]", list[l].get_position(), "id:", id(list[l]))
    #
    # if(cs_list[0] is list[3]):
    #     print("same")
    if (len(sys.argv) > 1):
        args = sys.argv
        cf.set_function(args[1])
        cf.set_dimension(int(args[2]))
        cf.set_population_size(int(args[3]))
        cf.set_iteration(int(args[4]))
        cf.set_max_domain(float(args[5]))
        cf.set_min_domain(float(args[6]))

    results = open("results" + os.sep + cf.get_function() + str(cf.get_dimension()) + "_"+args[7]+"_"+args[8]+"_"+args[9]+"results.csv", "w")
    results_writer = csv.writer(results, lineterminator="\n")
    pso_results = open("results" + os.sep + cf.get_function() + str(cf.get_dimension()) + "_"+args[7]+"_"+args[8]+"_"+args[9]+"pso.csv", "w")
    pso_results_writer = csv.writer(pso_results, lineterminator="\n")
    cs_results = open("results" + os.sep + cf.get_function() + str(cf.get_dimension()) + "_"+args[7]+"_"+args[8]+"_"+args[9]+"cs.csv", "w")
    cs_results_writer = csv.writer(cs_results, lineterminator="\n")
    de_results = open("results" + os.sep + cf.get_function() + str(cf.get_dimension()) +  "_"+args[7]+"_"+args[8]+"_"+args[9]+"de.csv", "w")
    de_results_writer = csv.writer(de_results, lineterminator="\n")

    OutputFiles = []
    OutputFiles.append(results)
    OutputFiles.append(pso_results)
    OutputFiles.append(cs_results)
    OutputFiles.append(de_results)


    main()






