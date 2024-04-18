import pandas as pd #for creating and handling dataframe

df=pd.read_csv('data.csv')#loading data into dataframe

print(df.columns[df.isna().any()])#checking NaN before replacing

calorie_mean=df['Calories'].mean()#getiing calories column mean value
print(calorie_mean)

#replacing NaN value with mean value
df['Calories'].fillna(calorie_mean,inplace=True)
print(df.columns[df.isna().any()])#checking NAN after replacing
