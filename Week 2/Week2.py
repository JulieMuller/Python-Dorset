import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

#read csv file, put it in datatframe
df = pd.read_csv("C://Users//Mulle//Desktop//AI//Week 2//Salaries.csv")


#list first and last n records
print(df.head(5))
print(df.tail(5))

#gives type of the column
print(df['service'].dtype)

#Find how many records this data frame has
print(df.shape)

#How many elements are there?     
print(df.size)

#What are the column names?   
print(df.columns)

#What types of columns we have in this data frame?
print(df.dtypes)

#Give the summary for the numeric columns in the dataset
print(df.describe())

#Calculate standard deviation for all numeric columns;
print(df.select_dtypes('int64').std())

#What are the mean values of the first 50 records in the dataset?
print(df.select_dtypes('int64').mean())


#Calculate the basic statistics for the salary column;
print(df['salary'].describe())

#Find how many values in the salary column (use count method);
print(df['salary'].count())

#Calculate the average salary;
print(df['salary'].mean())
