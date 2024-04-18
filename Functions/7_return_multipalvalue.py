print("function with return multiple values")
def arthmetic(n1,n2):
    sum=n1+n2
    mul=n1*n2
    return sum,mul
print('arithametic operation using Fun')
n1=int(input('enter num'))
n2=int(input('enter num'))
res1,res2=arthmetic(n1,n2)
print('add of{0} and {1} is {2}'.format(n1,n2,res1))
print('mul of{0} and {1} is {2}'.format(n1,n2,res2))