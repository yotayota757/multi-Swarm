import numpy as np
import math
import function as fn
from config import Config as cf

def levy_flight(Lambda):#generate step from levy distribution
    """
     Eq :
    """
    sigma1 = np.power((math.gamma(1 + Lambda) * np.sin((np.pi * Lambda) / 2)) \
                      / math.gamma((1 + Lambda) / 2) * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
    sigma2 = 1
    u = np.random.normal(0, sigma1, size=cf.get_dimension())
    v = np.random.normal(0, sigma2, size=cf.get_dimension())
    step = u / np.power(np.fabs(v), 1 / Lambda)
    # return np.array (ex. [ 3.12188518 -0.74306554 -4.66727534])
    return step


class Individual:
    def __init__(self):#dim=次元数
        self.__position = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()#位置座標
        self.__velocity = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()#速度ベクトル
        self.__fitness = fn.calculation(self.__position,0)#評価値
        self.__p_best_fitness = self.__fitness#各個体の最良値
        self.__p_best_position = self.__position

    # Position
    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    # Velocity
    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = velocity

    # Fitness
    def get_fitness(self):
        return self.__fitness

    def set_fitness(self, fitness):
        self.__fitness = fitness

    # p_best_position
    def get_p_best_position(self):
        return self.__p_best_position

    def set_p_best_position(self,p_best_position):
        self.__p_best_position = p_best_position

    # p_best_fitness
    def get_p_best_fitness(self):
        return self.__p_best_fitness

    def set_p_best_fitness(self,p_best_fitness):
        self.__p_best_fitness = p_best_fitness

    # Reset
    def reset(self,t):
        self.__position = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()#位置座標
        self.__velocity = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()#速度ベクトル
        self.__fitness = fn.calculation(self.__position,0)#評価値

    # Print
    def print_info(self,i):
        print("id:","{0:3d}".format(i),
              "|| fitness:",str(self.__fitness).rjust(14," "),
              "|| position:",np.round(self.__position,decimals=4))


    """Cuckoo Search"""
    def abandon(self):
        # abandon some variables
        for i in range(len(self.__position)):
            p = np.random.rand()
            if p < cf.get_Pa():
                self.__position[i] = np.random.rand() * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()

    def get_cuckoo(self):
        step_size = cf.get_step_size() * levy_flight(cf.get_lambda())

        # Update position
        self.__position = self.__position + step_size

        for i in range(len(self.__position)):
            if self.__position[i] > cf.get_max_domain():
                self.__position[i] = cf.get_max_domain()
            if self.__position[i] < cf.get_min_domain():
                self.__position[i] = cf.get_min_domain()


    """Differential Evolution"""
    def generate(self, a, b, c, R):
        for i in range(len(self.__position)):
            rnd = np.random.rand()
            if (rnd < cf.get_CR() or i == R):
                """update equation"""
                self.__position[i] = a.get_position()[i] + cf.get_F() * (b.get_position()[i] - c.get_position()[i])
                if (self.__position[i] > cf.get_max_domain()):
                    self.__position[i] = cf.get_max_domain()
                if (self.__position[i] < cf.get_min_domain()):
                    self.__position[i] = cf.get_min_domain()


    """Particle Swarm Optimization"""
    def update_position(self):
        self.__position = self.__position + self.__velocity

        """Simple Boundary Rule (if over boundary, set zero velocity)"""
        for i in range(len(self.__position)):
            if (self.__position[i] > cf.get_max_domain()):
                self.__position[i] = cf.get_max_domain()
                # self.__velocity = np.zeros(len(self.__velocity))
            if (self.__position[i] < cf.get_min_domain()):
                self.__position[i] = cf.get_min_domain()
                # self.__velocity = np.zeros(len(self.__velocity))

    def update_velocity(self, best_position):
        r_1 = np.random.rand()
        r_2 = np.random.rand()

        """
        [Reload Equation] (x indicate position vector)
        v = wv + c_1 * r_1 (x_pbest - x) + c_2 * r_2 (x_gbest - x)
        """
        self.__velocity = cf.get_W() * self.__velocity \
                          + cf.get_C1() * r_1 * (self.__p_best_position - self.__position) \
                          + cf.get_C2() * r_2 * (best_position - self.__position)



    # def CalcIndividual(self,t):#評価値を計算しパーソナルベストを更新する．
    #     #評価値の更新
    #     self.fitness = main.Calculation(self.position,t)
    #     self.partial_best = main.Calculation(self.partial_best_position,t)
    #     #パーソナルベストの更新
    #     if(self.fitness < self.partial_best):
    #         self.partial_best = self.fitness
    #         self.partial_best_position = self.position
    #         # print("更新")
    #         # print(self.partial_best)
    #         # input()
    #
    # def ReloadPSO(self):#位置の更新
    #     tmp_position = self.position + self.velocity
    #     #print (self.position)
    #     #print (self.velocity)
    #
    #     #print (self.position)
    #     #print (self.velocity)
    #     #print (tmp_position)
    #
    #     for i in range(len(tmp_position)):
    #         if tmp_position[i] > main.max_range:
    #             tmp_position[i] = main.max_range
    #
    #         elif tmp_position[i] < main.min_range:
    #             tmp_position[i] = main.min_range
    #
    #     self.position = tmp_position
    #
    #     # if max(tmp_position) < main.max_range and min(tmp_position) > main.min_range:
    #     #     self.position = self.position + self.velocity
    #     # else:
    #         # print("範囲外生成")
    #         # while
    #
    # def ReloadVelocity(self, swarm_best_position):
    #     # print(swarm_best_position)
    #     #パーソナルな評価値を考慮したもの
    #     self.velocity = w * self.velocity \
    #                     + 0.9 * main.rnd.rand() * (self.partial_best_position - self.position)\
    #                     + 0.95 * main.rnd.rand() * (swarm_best_position - self.position)
    #     # if max(self.velocity) > 500 or min(self.velocity) < -500:
    #     #     print("velocity:",self.velocity)
    #     #     print("partial_best:",self.partial_best_position)
    #     #     print("best_position:",swarm_best_position)
    #     #     print("self.positon:",self.position)
    #
    #     # #グローバルのみ評価
    #     # self.velocity = w * self.velocity \
    #     #                 + 0.9 * np.random.rand() * (swarm_best_position - self.position)
    #
    # def GetLevy(self):
    #     sigma1 = math.pow((math.gamma(1 + lam) * math.sin((math.pi * lam) / 2)) \
    #                       / math.gamma((1 + lam) / 2) * math.pow(2, (lam - 1) / 2), 1 / lam)
    #     sigma2 = 1
    #     # u = random.gauss(0, sigma=sigma1)
    #     u = main.rnd.normal(0,sigma1)
    #     # v = random.gauss(0, sigma=sigma2)
    #     v = main.rnd.normal(0,sigma2)
    #     step = u / math.pow(math.fabs(v), 1 / lam)
    #     # print (step)
    #     return step
    #
    # def ChangePosition(self, solution):
    #     self.position = solution.position
    #     self.fitness = solution.fitness
    #
    # def InitSolution(self,dim):
    #     self.position = (main.rnd.rand(dim) * (main.max_range - main.min_range)  + main.min_range)
    #     self.velocity = (main.rnd.rand(dim) * (main.max_range - main.min_range)  + main.min_range)#速度ベクトル
    #
    # def GetPosition(self):
    #     return self.position

    # def ReloadLevyLocal(self,t):#局所探索のやつ
    #     # alpha = (main.max_range - main.min_range) / 100
    #     alpha = 0.01
    #     tmp_position = np.zeros(len(self.position))
    #     # print("tmp_position",tmp_position)
    #     # print("移動前",self.position)
    #
    #     for dim in range(len(self.position)):
    #         # print(len(self.position))
    #         step = self.GetLevy()
    #         tmp_position[dim] = self.position[dim] + alpha * step
    #         # print("生成距離",step)
    #         if tmp_position[dim] > main.max_range:
    #             tmp_position[dim] = main.max_range
    #         if tmp_position[dim] < main.min_range:
    #             tmp_position[dim] = main.min_range
    #         # print("移動後", tmp_position[dim])
    #
    #     # print("配列", tmp_position)
    #     tmp_fitness = main.Calculation(tmp_position,t)
    #     # print(tmp_position)
    #
    #     if (tmp_fitness < self.fitness):
    #         self.position = tmp_position
    #         self.fitness = main.Calculation(self.position,t)

    # def ReloadLevy(self,t):#普通のやつ
    #     # alpha = (main.max_range - main.min_range) / 100
    #     alpha = 0.01
    #     tmp_position = np.zeros(len(self.position))
    #     # print("tmp_position",tmp_position)
    #     # print("移動前",self.position)
    #
    #     for dim in range(len(self.position)):
    #         # print(len(self.position))
    #         step = self.GetLevy()
    #         tmp_position[dim] = self.position[dim] + alpha * step
    #         # print("生成距離",step)
    #         if tmp_position[dim] > main.max_range:
    #             tmp_position[dim] = main.max_range
    #         if tmp_position[dim] < main.min_range:
    #             tmp_position[dim] = main.min_range
    #
    #     self.position = tmp_position
    #     # print("配列", tmp_position)
    #     # input()
    #     self.fitness = main.Calculation(self.position,t)


if __name__ == '__main__':#確認用
    pass


