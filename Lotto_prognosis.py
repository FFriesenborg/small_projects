# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:40:01 2022

@author: fabic
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#------------------------CHANGE THESE PARAMETERS---------------------------------

weeks_to_include = 15 #the last 15 weeks will be included in plots and analysis (must not exceed amount of total games/rows)

#change directory to location of lotto numbers file on respective computer
df = pd.read_csv(r'C:/Users/fabic/Desktop/Lotto_shenanigans/Eurojackpot.csv') #read sv as dataframe

#color of the boxplots (for color overview go to https://matplotlib.org/2.0.1/examples/color/named_colors.html)
color = 'midnightblue'

#------------------------------------------------------------------------------



print(df)

numbers = pd.DataFrame.to_numpy(df) #create numpy array
super_zahlen = numbers[:,5:] #seperate superzahlen
numbers = numbers[:,:5] #seperate numbers from superzahlen


numbers_amounts_dec = np.zeros([numbers.shape[0],5]) #create array for amounts of decades


for i in range(numbers_amounts_dec.shape[0]): #iterate through amounts_array rows
    for j in range(numbers_amounts_dec.shape[1]): #iterate though amounts_array columns
        if j < 4: #if is necessary so we can include >= 40 in one cell
            numbers_amounts_dec[i,j] = np.count_nonzero((numbers[i]/10).astype(int) == j) #write amounts of values in decade in array cell
        else:
            numbers_amounts_dec[i,j] = np.count_nonzero((numbers[i]/10).astype(int) >= j) #write amounts of values in decade in array cell
 
#create arrays for last 15 weeks
numbers_recent = numbers[-1*(weeks_to_include):]   
numbers_recent_amounts_dec = (numbers_amounts_dec[-1*(weeks_to_include):]).astype(int)

#plot histograms
fig1, axe1 = plt.subplots(2)
labels, counts = np.unique(numbers_recent, return_counts=True)
axe1[0].bar(labels, counts, align='center',color = color, ec = 'black')
axe1[0].set_xticks(labels)
axe1[0].set_title('Frequency distribution of single values')
labels, counts = np.unique(((numbers_recent/10).astype(int)), return_counts=True)
axe1[1].bar(list(range(5)), numbers_recent_amounts_dec.sum(axis=0), color = color, align='center', ec = 'black')
axe1[1].set_title('Frequency distribution of decades')
fig1.suptitle('Frequency distribution of values', fontsize=16)



#plot developement of decades over last games
fig2, axe2 = plt.subplots()
for i in range(numbers_recent_amounts_dec.shape[1]):
    axe2.plot(numbers_recent_amounts_dec[:,i])
axe2.legend(['1-9','10-19','20-29','30-39','40-50'])
fig2.suptitle('Developement of decades', fontsize=16)


