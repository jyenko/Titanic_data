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

#Phase 1 - Read and process csv data
#Read in csv data using only relevant columns, as indicated by usecols()
df = pd.read_csv('titanicdata.csv', header=0, names=['PassengerID', 'Survived', 'Class',
                                                     'Sex', 'Fare'], usecols=(0,1,2,4,9))

#Check for missing values
print df.isnull().sum()

#Check data types
print "Raw data types:"
print df.dtypes
print "---------------------------------------"

#Fix data types
def fix_data_types(col, newtype):
    df[[col]] = df[[col]].astype(newtype)

fix_data_types('PassengerID', object) #Change the PassengerID column to an object type
fix_data_types('Survived', bool) #Change the Survived column to a bool type

#Confirm data types
print "--------------------------------------"
print "New data types:"
print df.dtypes

print "--------------------------------------"

print "Overall statistics:"
print df.describe()

print "--------------------------------------"

print "Overall fare statistics:"

print df['Fare'].describe()

fig1 = plt.figure()
plt.boxplot(df['Fare'])
fig1.suptitle('Boxplot distribution of all fares')
plt.ylabel('Fare')
plt.show()


print "--------------------------------------"

survivors = df.groupby(['Survived'])
cabin = df.groupby(['Class'])
gender = df.groupby(['Sex'])

print "--------------------------------------"

print "Median fare based on survival status"
print survivors['Fare'].median()
print "++++++++++++++++++++++++++++++++++++++"

print "Mean fare based on survival status"
print survivors['Fare'].mean()
print "++++++++++++++++++++++++++++++++++++++"

print survivors.size()
print "======================================"

print "Mean fare based on class"
print cabin['Fare'].mean()
print "======================================"

print "Median fare based on class"
print cabin['Fare'].median()
print "======================================"

print cabin.size()
print "======================================"

print "--------------------------------------"

first_class = df.query('Class==1')
first_class_survivors = first_class.query('Survived==1')
first_survived = float(len(first_class_survivors))
first_total = float(len(first_class))
first_pct = (first_survived/first_total)*100
print "Approximately ", int(round(first_pct)), " percent of first class passengers survived"
print first_survived
print first_total

second_class = df.query('Class==2')
second_class_survivors = second_class.query('Survived==1')
second_survived = float(len(second_class_survivors))
second_total = float(len(second_class))
second_pct = (second_survived/second_total)*100
print "Approximately ", int(round(second_pct)), " percent of second class passengers survived"
print second_survived
print second_total

third_class = df.query('Class==3')
third_class_survivors = third_class.query('Survived==1')
third_survived = float(len(third_class_survivors))
third_total = float(len(third_class))
third_pct = (third_survived/third_total)*100
print "Approximately ", int(round(third_pct)), " percent of third class passengers survived"
print third_survived
print third_total

print "-----------------------------------------"

gender = df.groupby(['Sex'])

print gender.size()

women = df.query('Sex=="female"')
female_survivors = women.query('Survived==1')
female_survived = float(len(female_survivors))
female_total = float(len(women))
female_pct = (female_survived/female_total)*100
print "Approximately ", int(round(female_pct)), " percent of female passengers survived"
print int(female_survived), " out of ", int(female_total)

men = df.query('Sex=="male"')
male_survivors = men.query('Survived==1')
male_survived = float(len(male_survivors))
male_total = float(len(men))
male_pct = (male_survived/male_total)*100
print "Approximately ", int(round(male_pct)), " percent of male passengers survived"
print int(male_survived), " out of ", int(male_total)

print "+++++++++++++++++++++++++++++++++++++++++"

pas_survived = df.query('Survived==1')['Fare']
pas_perished = df.query('Survived==0')['Fare']

fig2 = plt.figure()
plt.hist(pas_survived, bins=100)
plt.hist(pas_perished, bins=100)
fig2.suptitle('Distribution of fares by survival status')
plt.xlabel('Fare')
plt.ylabel('Number of occurences')
plt.legend(("Survived", "Perished"))
plt.show()

survived = df.query('Survived==1')['Fare'].values
perished = df.query('Survived==0')['Fare'].values
                   
fig3 = plt.figure()                   
plt.boxplot(perished)
fig3.suptitle('Boxplot distribution of fares for non survivors')
plt.ylabel('Fare')
plt.ylim([0, 550])
plt.show()

fig4 = plt.figure()
plt.boxplot(survived)
fig4.suptitle('Boxplot distribution of fares for survivors')
plt.ylabel('Fare')
plt.ylim([0, 550])
plt.show()

sns.boxplot(data=df, y='Fare', x='Survived')













