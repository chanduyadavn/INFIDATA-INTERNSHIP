import numpy as np   #for array
import pandas as pd    #for data frame

example1_data=pd.DataFrame({'x':[0,1,2,3,4,],
                           'y':[1.5,2,3.5,5,4.5]})
print(example1_data)#dispaly example 1 data frame

x=example1_data['x'].values.reshape(-1,1)#choosing input value
y=example1_data['y'].values.reshape(-1,1)#choosing output value

from sklearn.linear_model import LinearRegression #importing alogo
linear_regression=LinearRegression()
linear_regression.fit(x,y)
print('[info] Linear regression model training model training complete....')

m=linear_regression.coef_[0][0]
c=linear_regression.intercept_[0]

print(f'm value is :{m}')
print(f'cvalue is :{c}')
print(f'equation of line is:y={m}x+{c}')

new_user_input=float(input('enter value of x:'))
new_user_input=[[new_user_input]]
new_output=linear_regression.predict(new_user_input)[0]
print(f'when x={new_user_input},y={new_output}')