import numpy as np   #for array
import pandas as pd    #for data frame

example2_data=pd.DataFrame({'x':[-5,-4,-3,-2,-1,0,1,2,3,4,5],
                           'y':[0,0,0,0,0,1,1,1,1,1,1]})
print(example2_data)#dispaly example 1 data frame

x=example2_data['x'].values.reshape(-1,1)#choosing input value
y=example2_data['y'].values.reshape(-1,1)#choosing output value

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

sigma=1/(1+np.exp(-new_output[0]))
print(f'sigma value={sigma}')
