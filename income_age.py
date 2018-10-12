#! /urs/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#set up the variables
age = [i * 1 for i in range(18,82,3)]
income = [2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,\
          12000,13000,13000,13000,10000,5000,4500,4000,4000,3500,3000,3000]
housing = ['own','own','own','free','free','free','own','rent','own','own',
           'rent','rent','own','own','rent','own','own','own','free',\
           'own','own','rent']
gender = ['male','female','male','male','male','male','male','male','male',\
       'male','female','female','female','male','female','female','male',\
       'male','female','male','male','male']


F = np.polyfit(age,income,1)
print(F)
P = np.poly1d(F)
print(P)

L = pd.Series(income,index = age)
L.plot(kind='line')
plt.show()
