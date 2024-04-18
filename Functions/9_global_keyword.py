def read():
    global n1,n2
    n1=int(input('enter first num'))
    n2=int(input('enter sencond num'))
def add1():

        sum1=n1+n2
        print('add of {0} and {1} is {2}'.format(n1,n2,sum1))
def add2():
    n3=int(input('enter tird num'))
    sum2=n1+n2+n3
    print('add of{0} and {1} and {2} is {3}'.format(n1,n2,n3,sum2))
print('gobal keyword Demo')
read()
add1()
add2()