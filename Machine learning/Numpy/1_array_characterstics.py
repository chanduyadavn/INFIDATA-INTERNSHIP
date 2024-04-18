#importing necessary libraries
import numpy as np #used for matrix calculation

#matrix A
a=np.array([[1,2,3],[4,5,6]])  #array creation
print("array elements are:")
print(a) #displaying the created matrix
print("type of array is:",type) #data type of array
print("shape of array",a.shape) #shape of array
print("size of the array is",a.size) #size of array

#example1
example_1=np.array([[1,'i',0],[0,'pi',-1]])
print("array elements are")
print(example_1)
print("type of array is:",type(example_1))
print("shape of array",example_1.shape)
print("size of the array is",example_1.size)

#example2
example_2=np.array([[1],[0]])
print("array elements are")
print(example_2)
print("type of array is:",type(example_2))
print("shape of array",example_2.shape)
print("size of the array is",example_2.size)

#example3
example_3=np.array([[1,0]])
print("array elements are")
print(example_3)
print("type of array is:",type(example_3))
print("shape of array",example_3.shape)
print("size of the array is",example_3.size)
