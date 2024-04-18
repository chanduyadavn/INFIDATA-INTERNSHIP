import pandas as pd
df=pd.read_csv('diabetes.csv')#loading data into  a dataframe
#head
print("accessing from the dataset from first 10 rows \n",df.head(10))
print("accessing from the dataset from first 5 rows \n",df.head())

#tail
print("accessing from the dataset from last 5 rows \n",df.tail())
print("accessing from the dataset from last 10 rows \n",df.tail(10))

print(df.shape)#rows and colums values
print(df.columns[df.isna().any()])#to check null values

#inforamtion data
print('basic info:\n',df.info)

#basic statical information
print('satistical info:\n',df.describe())