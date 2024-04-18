#asuming a dataframe/dataset is already present,
#this is how we read/load it
import  pandas as pd
#jasong=JavaScript object Notation,
df=pd.read_json('data.json')
print(df)