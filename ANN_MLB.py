import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from numpy import loadtxt

dataframe = loadtxt('Batting_noSB.csv', delimeter=',')

dataframe.head()





