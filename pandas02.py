#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:46:08 2024

@author: blessingmkhonazi
"""

import pandas as pd
#pd can be called whatever, it is not restricted to pd.
#remember, when putting the command print it should be what pd is
#eg: file=pd.read_csv("country_data_index.csv")
     #print(file)

df = pd.read_csv("country_data_index.csv")

print (df)

df = pd.read_csv("iris.csv")
print (df)
"""
Absolute path
/Users/blessingmkhonazi/CSS2024_Day2
Absolute path gives the full path on the computer

Relative path
iris.csv
Gives the location were you are currently are
"""

#This if for importing data from a website
import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

print(df)

#you van add the headers and columns from the website data by doing this:
  #  column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

#print(df)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
print(df)
 

#Different types of data

#text file
df = pd.read_csv("Geospatial Data.txt", sep=";")

#excel file
#df = pd.read_excel("residentialdoctors.xlsx"), #can specify the sheet

#df= data frames: stores data ina tabular manner

# url = "https://github.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

# df=pd.read_csv(url)

df= pd.read_csv("Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])

print(df)

#ETL: Extraction, transformation and loading of files

"""
Transformation

"""

df =pd.read_csv("country_data_index.csv", index_col=0)

#need to do skip rows and columns

df=pd.read_excel("residentdoctors.xlsx")
print(df.info())

# creating a new column

df["LOWER_AGE"]=df["AGEDIST"].str.extract('(\d+)-')
df["UPPER_AGE"]=df["AGEDIST"].str.extract('(\d+)-')
# AGEDIST is age distribution
print(df.info())

#Object is a variable that contains data and function

#converting the obtect to an integer
df["LOWER AGE"]=df["LOWER_AGE"].astype(int)
df["UPPER AGE"]=df["LOWER_AGE"].astype(int)
print(df.info())

"""
WORKING WITH DATES

dates are read as strings eg: 'Date'

read about regular expressions
Regular expressions
example \d+ any degit less than 9, and should be positive
30-01-2024 UK
01-30-2024 (cannot have this) US

"""

# df = pd.read_csv("time_series_data.csv")

df=pd.read_csv("time_series_data.csv", index_col=0)
print(df.info())

# df['Date']=pd.to_datetime(df['Date'],format="%d-%m-%y")
# print(df.info())
df['Date']=pd.to_datetime(df['Date'])
"""
extracting data such as day, month and year
"""



"""
manupulating a table

.str
.extract
.astype
.dt

know what each represent
"""

df['Year'] = df['Date'].dt.year


df = pd.read_csv("patient_data.csv")

print(df)

df = pd.read_csv("time_series_data.csv")
# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Split the 'Date' column into separate columns for year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day


import pandas as pd

df = pd.read_csv('patient_data_dates.csv')

# Allows you to see all rows
pd.set_option('display.max_rows',None)

print(df)

df.drop(['Index'],inplace=True,axis=1)

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True) 

# df['Date'] = pd.to_datetime(df['Date'])

"""
Applying data transformation
"""


df=pd.read_csv("iris.csv")

# print(df.columns)
col_names=df.columns

print(col_names)
df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq"] = df["sepal_length"].apply(lambda x:x**2)

grouped= df.groupby("class")

# Calculate mean, sum, and count for the squared values
mean_squared_values = grouped['sepal_length_sq'].mean()
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

"""
Filtering data
"""
# Filtering data
print(df[df['age'] > 30])























