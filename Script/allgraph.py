# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:50:20 2017

@author: UMENAI
"""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv("./pro_results.csv")
Data = data.T


Data.plot(logy=True)
plt.savefig("pro.png")
#plt.show()
