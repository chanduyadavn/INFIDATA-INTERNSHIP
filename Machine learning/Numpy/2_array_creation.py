import numpy as np
#create an array from list with type float
a1=np.array([[1,2,3],[4,5,6]],dtype='float') #creating an array with all float numbers
print("array contents are:",a1) #displaying the created array

#create array from tuple
a2=np.array((1,2,3))#creating an array from tuples
print("array created from tuple is",a2) #displaying the created array

#create a 16*173 array with all zeros
a3=np.zeros((16,173))
print("\n array initialized with all zeros:\n",a3)

#creating a 17*17 array with all ones
one=np.ones((17,17))
print("\n an array intialized with all ones:\n",one)

#create a matrix full one number
a4=np.full((17,17),-24.6782)
print("\n an array intializes with all 24.6782 is :\n",a4)

#create an array with random values
a5=np.random.random((3,2))
print("\n a random arrray:\n",a5)

#create a sequence of integers from 0 to 40 with steps of 5
a6=np.arange(0,40,5)#start value is displayed,end value is
print("\n a sequential array with steps of 5:\n",a6)

#a7=np.arange(0,40,4.44)
#print("sequential array",a7)

#create a sequence of 10 values in range 0 to 40
a7=np.linspace(0,40,10)#both starting and end point is displayed in result
print("\n a sequential array with 10 values between 0 and 5:\n",a7)

#flatten array
all=np.array([[1,2,3],[4,5,6]])
reshaped_array=all.reshape((1,-1))
reshaped_array_2=all.reshape((-1,1))

print("\n original array:\n",all)
print("reshaped array:\n",reshaped_array)
print("reshaped array:\n",reshaped_array_2)

