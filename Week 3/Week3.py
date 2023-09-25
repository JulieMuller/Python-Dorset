#libraries             
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#setting the standard color code ..styling
sns.set(color_codes=True) 

#upload dataset
auto = pd.read_csv('C:/Users/Mulle/Desktop/AI/Week 3/Automobile.csv') 

X = auto['engine_size']
Y = auto['city_mpg']
#sns.jointplot(x=X, y=Y, height=1.8)

#print(auto.describe().transpose())


# (1) Split de dataset in train and test datasets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3) #30 percent of data for test

# (2) Create a linear model
lr_model = LinearRegression() #creates a lr model

X_train = X_train.values.reshape(-1, 1) #reshape values to a 2d array
X_test = X_test.values.reshape(-1, 1) #reshape values to a 2d array
Y_train = Y_train.values.reshape(-1, 1) #reshape values to a 2d array
Y_test = Y_test.values.reshape(-1, 1) #reshape values to a 2d array
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

lr_model.fit(X_train, Y_train) #train the model

print("y = %sx + %s" % (lr_model.coef_[0], lr_model.intercept_[0])) # Get the train model
