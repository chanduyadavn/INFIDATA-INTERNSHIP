#assuming a dataframe/dataset is already present,
#this is now me read/load it

import pandas as pd #for creating and handling dataframe
#loading id.csv into pands dataframe
data=pd.read_csv('diabetes.csv')
print(data)#displaying that dataframe
#
print("display specfic colums")
print(data['Glucose'])#display single column
print(data[['Glucose','BMI']])#display multiple column
#
print(data.shape)#display shape of dataset

print(data.size)#display size of data

#indexing
print(data.head())#print first 5 rows data

print(data.tail())#print first 5 rows data