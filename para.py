import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

housing = ['own','own','own','free','free','free','own','rent','own','own',
           'rent','rent','own','own','rent','own','own','own','free',\
           'own','own','rent']
gender = ['male','female','male','male','male','male','male','male','male',\
       'male','female','female','female','male','female','female','male',\
       'male','female','male','male','male']

count_own = 0
count_rent = 0
for i in housing:
	if i == 'own':
		count_own+=1
	else:
		count_rent+=1

print("own housing: ",count_own)
print("No housing: ",count_rent)
print("Total number: ",count_own+count_rent)

female = 0
male = 0
for j in gender:
	if j == 'male':
		male+=1
	else:
		female+=1

print("male: ",male)
print("female: ",female)
print("Total: ",male+female)


plt.figure(figsize = (count_own,count_rent))
