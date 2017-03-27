# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 17:11:52 2017

@author: Jeremy J. Yenko
"""

"""
This project will be based on the Titanic passenger dataset
"""

#Import relevant packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read in csv data using only relevant columns, as indicated by usecols()
df = pd.read_csv('titanicdata.csv', header=0, names=['PassengerID', 'Survived', 'Class',
                                                     'Sex', 'Fare'], usecols=(0,1,2,4,9))

#Check for missing values
print df.isnull().sum()

#Check data types
print "Raw data types:"
print df.dtypes

#Fix data types
def fix_data_types(col, newtype):
    df[[col]] = df[[col]].astype(newtype)

fix_data_types('PassengerID', object) #Change the PassengerID column to an object type
fix_data_types('Survived', bool) #Change the Survived column to a bool type

#Confirm data types
print "New data types:"
print df.dtypes

#Compute relevant statistics for the entire dataframe
print "Overall statistics:"
print df.describe()

#Compute relevant statistics for the fare column
print "Overall fare statistics:"
print df['Fare'].describe()

#Create a boxplot showing the distribution of fares for all passengers in the dataset
fig1 = plt.figure()
plt.boxplot(df['Fare'])
fig1.suptitle('Boxplot distribution of all fares')
plt.ylabel('Fare')
plt.show()

#Create groupby() objects for the survived and class columns
survivors = df.groupby(['Survived'])
cabin = df.groupby(['Class'])

#Compute the median fare for survivors and non survivors
print "Median fare based on survival status"
print survivors['Fare'].median()

#Compute the mean fare for survivors 
print "Mean fare based on survival status"
print survivors['Fare'].mean()

#Display the number of survivors and the number of non survivors
print "Total number of survivors and non survivors"
print survivors.size()

#Display the mean fare for each class
print "Mean fare based on class"
print cabin['Fare'].mean()

#Display the median fare for each class
print "Median fare based on class"
print cabin['Fare'].median()

#Display the percentage of survivors by class
print "Percentage of survivors by class"
print df.groupby(['Class'])['Survived'].mean()

#Display the total number of passengers in each class
print "Total number of passengers in each class"
print cabin.size()

#Display the percentage of survivors by gender
print "Percentage of survivors by gender"
print df.groupby(['Sex'])['Survived'].mean()

#Display the total number of male and female passengers in the dataset
print "Total number of passengers in the dataset by gender"
print df.groupby(['Sex']).size()

#Create a histogram showing the fare distributions for survivors and non survivors simultaneously
pas_survived = df.query('Survived==1')['Fare'] #Use the query() method to get the fare column for survivors
pas_perished = df.query('Survived==0')['Fare'] #Use the query() method to get the fare column for non survivors
fig2 = plt.figure()
plt.hist(pas_survived, bins=100) #Set the number of bins to 100 for the histogram
plt.hist(pas_perished, bins=100)
fig2.suptitle('Distribution of fares by survival status') #Set the title of the chart
plt.xlabel('Fare') #Label the x axis as Fare
plt.ylabel('Number of occurences') #Label the y axis as Number of occurences
plt.legend(("Survived", "Perished")) #Create a legend to distinguish each distribution
plt.show()

#Create a boxplot showing the fare distribution by survival status
sns.boxplot(data=df, y='Fare', x='Survived')
sns.plt.show()
