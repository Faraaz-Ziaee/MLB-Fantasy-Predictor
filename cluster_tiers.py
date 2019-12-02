import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error, r2_score
import os

## Read in file and only use players from 2016 - 2018
df = pd.read_csv('Batting_Cluster.csv', delimiter=',')
df = df[(df.yearID == 2018) | (df.yearID == 2017) | (df.yearID == 2016)]

## Group by each player and only use those that appear in all 3 years
gb = df.groupby('playerID')
finalGroup = gb.filter(lambda x: len(x) > 2)

##
print(df)
print(finalGroup)



  #  print(gb.get_group(key), "\n\n")