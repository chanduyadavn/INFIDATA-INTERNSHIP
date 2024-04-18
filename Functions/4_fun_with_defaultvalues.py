print('function with default value')
def addition(a=5,b=20):
    sum=a+b
    print('add of {0} and {1} is{2}'.format(a,b,sum))
print("addition program using function")
n1=int(input('enter the num'))
n2=int(input('enter the num'))
addition()
addition(n1,n2)
addition(n1)
print('end of code')
