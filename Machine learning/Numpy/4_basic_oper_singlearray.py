import numpy as np

a1=np.array[1,2,3,4,5,6]
#add 1 to every element
print('adding 1 to every element:',a1+1)

#substract 2 from each element
print('substracting 2 from each elements:',a1-2)

#multiply each element by 10
print('multiply each elements:',a1*10)

#square each element
print('sqauring  each elements:',a1**2)

#modify existing array
a1*=2 #a1=a1*2
print('doubled each element of orignal array:',a1)

#transpose of array
a2=np.array([[1,2,3],[3,4,5],[9,6,0]])

print('\n orginal array:\n',a2)
print('transpose of array:\n',a2.T)