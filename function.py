import numpy as np
from config import Config as cf

"""
[Reference]
https://www.sfu.ca/~ssurjano/index.html
"""

"""Parameters"""
# for ackley
a = 20
b = 0.2
c = np.pi


# def calculation(array, t):#as you want
#     fitness = singlemoving(array,t)
#     return fitness

def calculation(array, t):#as you want
    fitness = 0
    # # if(t < 3000):
    # #     fitness = rastrigin(array)
    # # if(t >= 3000 and t < 6000):
    # #     fitness = schwefel(array)
    # # fitness = rastrigin(array)

    # fitness = multimoving(array,t)
    # if(cf.get_function() == "case1"):
    #     if(t < 5000):
    #         fitness = rastrigin_stded(array)
    #     if(t >= 5000 and t < 10000):
    #         fitness = schwefel(array)
    if(cf.get_function() == "rast"):
        fitness = rastrigin_stded(array)

    if(cf.get_function() == "case1"):
        if(t < 150):
            fitness = schwefel(array)
        else:
            fitness = rastrigin_stded(array)
            
        # fitness = multimodal_10valley_move(array,t)

    # if(cf.get_function() == "case2"):
    #     if(t < 5000):
    #         fitness = rosenbrockstd(array)
    #     if(t >= 5000 and t < 10000):
    #         fitness = rastrigin_stded(array)

    if(cf.get_function() == "case2"):
        if(t < 3000):
            fitness = schwefel(array)
        if(t >= 3000 and t < 6000):
            fitness = rastrigin(array)

    if(cf.get_function() == "case3"):
        if(t < 5000):
            fitness = ackleystd(array)
        if(t >= 5000 and t < 10000):
            fitness = schwefel(array)
        if(t >= 10000 and t < 15000):
            fitness = rosenbrockstd(array)

    return fitness

def function(array,t):
    fitness = 0

    # Sphere
    if(cf.get_function() == "sphere"):
        for i in range(len(array)):
            fitness = fitness + array[i]**2

    # Ackley
    if(cf.get_function() == "ackley"):
        sum1 = 0
        sum2 = 0
        for i in range (len(array)):
            sum1 = sum1 + array[i]**2
        for i in range (len(array)):
            sum2 = sum2 + np.cos(c*array[i])
        fitness = - a * np.exp(-b * np.sqrt((1/len(array)) * sum1)) - np.exp((1/len(array)) * sum2) + a + np.exp(1)
    
    # Rosenbrock
    if (cf.get_function() == "rosenbrock"):
        sum1 = 0
        for i in range(len(array) - 1):
            sum1 = sum1 + (100 * (array[i+1] - array[i])**2 + (array[i] - 1)**2)
        fitness = sum1
    
    # Rastrigin
    if (cf.get_function() == "rastrigin"):
        sum = 0
        fitness = 0
        for x in array:
            sum = sum + x**2 - 10 * np.cos(2 * np.pi * x)
        fitness = 10.0 * len(array) + sum

    # Schwefel
    if (cf.get_function() == "schwefel"):
        sum = 0
        fitness = 0
        for x in array:
            sum = sum + x * np.sin(np.sqrt(np.abs(x)))
        fitness = 418.9829 * len(array) - sum


    return fitness


def singlemoving(array,t): #単峰性の動的環境
    # (0, 0)中心で半径125の半径の円
    a = ((array[0] - 125 * np.sin(0.01*t))**2 / (2 * 40**2))
    b = ((array[1] + 125 * np.cos(0.01*t))**2 / (2 * 40**2))
    fitness = 1 - np.exp(-a - b)
    return fitness

def multimoving(array,t):    #高野さんの動的環境
    sum = 0
    for i in range(cf.get_N()):
        v = 2*i*np.pi/cf.get_N()
        a = (np.cos((cf.get_Beta() * t) +v) + 1)/2
        b = (array[0] - cf.get_Radius() * np.cos(v))**2 / 40**2
        c = (array[1] - cf.get_Radius() * np.sin(v))**2 / 40**2
        sum = sum + a * np.exp(-1/2 * (b + c))

    return 1 - sum

def moving(array,t):
    if(cf.Config.get_function() == "case1"):
        cf.Config.set_Radisu(125)
        return singlemoving(array,t)

    if(cf.Config.get_function() == "case2"):
        return multimoving(array,main.rnd)

    if(cf.Config.get_function() == "case3"):
        if(t >= 0 and t < 5000):
            cf.Config.set_Radisu(350)
        elif(t >= 5000 and t < 10000):
            cf.Config.set_Radisu(700)
        return multimoving(array,t)

    if(cf.Config.get_function() == "case4"):
        return multimoving(array,t)

    if(cf.Config.get_function() == "case5"):
        if(t >= 0 and t < 3000):
            cf.Config.set_Beta(0.01)
        elif(t >= 3000 and t < 6000):
            cf.Config.set_Beta(0.1)
        elif(t >= 6000 and t < 9000):
            cf.Config.set_Beta(1.0)
        return multimoving(array,t)


def combination(array,t):
    if(t >= 0 and t < 3000):
        return multimoving(array,t)
    elif (t >= 3000 and t < 6000):
        if(t >= 3000 and t < 4500):
            cf.Config.set_Radisu(350)
        elif(t >= 4500 and t < 6000):
            cf.Config.set_Radisu(700)
        return multimoving(array,t)
    elif (t >= 6000 and t < 9000):
        if(t >= 6000 and t < 7000):
            cf.Config.set_Beta(0.01)
        elif(t >= 7000 and t < 8000):
            cf.Config.set_Beta(0.1)
        elif(t >= 8000 and t < 9000):
            cf.Config.set_Beta(1.0)
        return multimoving(array,t)


"""Benchmark Functions"""
def ackley(array):
    sum1 = 0
    sum2 = 0

    for i in range (len(array)):
        sum1 = sum1 + array[i]**2

    for i in range (len(array)):
        sum2 = sum2 + np.cos(c*array[i])

    fitness = - a * np.exp(-b * np.sqrt((1/d) * sum1)) - np.exp((1/d) * sum2) + a + np.exp(1)

    return fitness

def ackleystd(array):
    sum1 = 0
    sum2 = 0

    for i in range (len(array)):
        X = (array[i] / 500) * 32.768
        sum1 = sum1 + X**2

    for i in range (len(array)):
        X = (array[i] / 500) * 32.768
        sum2 = sum2 + np.cos(c*X)

    fitness = - a * np.exp(-b * np.sqrt((1/len(array)) * sum1)) - np.exp((1/len(array)) * sum2) + a + np.exp(1)

    return fitness

def rosenbrock(array):
    sum1 = 0

    for i in range(len(array) - 1):
        sum1 = sum1 + (100 * (array[i+1] - array[i])**2 + (array[i] - 1)**2)

    fitness = sum1
    return fitness

def rosenbrockstd(array):
    sum1 = 0

    for i in range(len(array) - 1):
        X1 = (array[i+1] / 500) * 2.048
        X2 = (array[i] / 500) * 2.048
        sum1 = sum1 + (100 * (X1 - X2)**2 + (X2 - 1)**2)

    fitness = sum1
    return fitness



def sphere(array):
    fitness = 0
    for i in range(len(array)):
        fitness = fitness + array[i]**2
    return fitness

def rastrigin(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x**2 - 10 * np.cos(2 * np.pi * x)
    fitness = 10.0 * len(array) + sum
    return fitness

def rastrigin_stded(array):
    sum = 0
    fitness = 0
    for x in array:
        X = (x / 500.0) * 5.12
        sum = sum + X**2 - 10 * np.cos(2 * np.pi * X)
    fitness = 10.0 * len(array) + sum
    return fitness

def schwefel(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x * np.sin(np.sqrt(np.abs(x)))
    fitness = 418.9829 * len(array) - sum
    return fitness

def michalewicz(array):#for the number of Dimension is 2
    sum = 0
    fitness = 0
    m = 10
    for (i,x) in enumerate(array, start=1):
        sum = sum + np.sin(x) * np.sin((i * (x**2) )/np.pi)**(2*m)
    fitness = -sum
    return fitness

def multimodal_10valley_move(array,iter):
    #関数設計パラメーター
    oneCycle_iteration = 150     #ピーク高さ変化の速さ 一巡までのiteration
    Npeaks = 10     #ピークの個数

    r = 350

    changeSpeed_Z = 1 * np.pi / oneCycle_iteration  #oneCycle_iteration得た変化係数
    changeSpeed_L = -1 * np.pi / oneCycle_iteration  #oneCycle_iteration得た変化係数

    top = 1
    for n in range(Npeaks):
        top -= (np.cos(changeSpeed_Z * iter + n *2*np.pi / Npeaks) + 1)/2 * np.exp(-(np.power(array[0] - r*np.cos(changeSpeed_L * iter + n*2*np.pi/Npeaks), 2)/np.power(40, 2) + np.power(array[1]- r * np.sin(changeSpeed_L * iter + n*2*np.pi/Npeaks), 2)/np.power(40, 2))/2)
    return top

if __name__ == '__main__':
    a = np.array([2.20,1.0])
    print (michalewicz(a))
