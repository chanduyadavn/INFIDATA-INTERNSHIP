#Create a dataframe/dataset

import pandas as pd
#how to convert dictonary to dataframe

data=pd.DataFrame({
    'name':['ali','khan','mahesh','vinit'],
    'age':[20,25,30,25],
     'branch':['cse','me','ise','ece'],
     'place':['banglore','delhi','mysore','porbandar']
})
print(data)

#saving the data frame created as csv file
data.to_csv('id.csv',index=False)