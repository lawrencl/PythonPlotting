# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 19:31:38 2014

Homework1 for MIT ESD.756J /15.062 Data Mining 

@author: laml
"""
import pandas as pd #plot graph
import matplotlib.pyplot as plt #ylabel

#read file into data2 variable
#file1 = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/LaptopSalesJanuary2008.txt'
#file2 = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/ToyotaCorolla.txt'
data1 = pd.read_csv(file2, sep='\t')file = 'testdata.txt'
#data2 = pd.read_csv(file, sep='\t', index_col='Date', parse_dates=True)

#2.11a Matrix plot histogram diagonal
#pd.tools.plotting.scatter_matrix(data2[['Price','Age_08_04','KM','HP','cc','Weight','Mfr_Guarantee']], alpha=0.2, diagonal='hist')

#3.3a Bar plot pivot table
#data2.pivot_table(values='Retail Price', index=['Store Postcode']).plot(kind='bar', title="Mean Retail Price per Store Postcode", legend=True)

#testing column logic for specific value
#print data2[data2['Store Postcode']=='W4 3PH']

#3.3b Boxplot side by side view
data2[data2['Store Postcode']==('N17 6QA')].append(data2[data2['Store Postcode']==('W4 3PH')]).boxplot(column='Retail Price',by='Store Postcode',rot='90')

#label y
plt.ylabel("Retail Price")