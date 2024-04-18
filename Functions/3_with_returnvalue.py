print('function with return value Demo')
def addition(a,b):
    sum=a+b
    return sum
print('program of addition')
n1=int(input('enter the num'))
n2=int(input('entyer the num'))
res=addition(n1,n2)
print('add of {0} and{1} is{2}'.format(n1,n2,res))
print('add of {0} and {1} is {2}'.format(n1,n2,addition(n1,n2)))
print('end of code')
