import pandas as pd #plot graph
import matplotlib.pyplot as plt #ylabel

#read file into data2 variable
#file = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/Python Github/testdata.txt'
file = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/Python Github/ToyotaCorolla.txt'
data2 = pd.read_csv(file, sep='\t')
#data2=pd.read_excel(file2, 'data', index_col=None, na_values=['NA'])
#data2 = pd.read_csv(file, sep='\t', index_col=None, parse_dates=False)

#create pivot table for Retail Price values categorized by Store Postcode
#plot as boxchart graph with specific values
#data2[data2['Store Postcode']==('N17 6QA')].append(data2[data2['Store Postcode']==('W4 3PH')]).boxplot(column='Retail Price',by='Store Postcode',rot='90')
pd.tools.plotting.scatter_matrix(data2[['Price','Age_08_04','KM','HP','cc','Weight','Mfr_Guarantee']], alpha=0.2, diagonal='hist')
#pd.tools.plotting.scatter_matrix(data2[['Weight','Height']], alpha=0.2, diagonal='hist')

#label y
#plt.ylabel("Retail Price")
#plt.show()
#plt.title('Scatter Matrix ToyotaCorolla')

#import numpy as np
#import matplotlib.pyplot as plt
#import pandas
#iris = pandas.read_csv("/home/vytas/iris.csv")
#df = pandas.DataFrame(iris, columns=['slength', 'swidth', 'plength', 'pwidth'])
#pandas.tools.plotting.scatter_matrix(df, alpha=0.2, diagonal='hist')
#plt.show()
