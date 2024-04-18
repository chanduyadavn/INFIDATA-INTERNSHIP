n1=int(input('enter 1st num'))#num10          ##num10
n2=int(input('enter 2nd num'))#num0           ##num5
l1=[4,5,6,7,8]
print('list l1 is:',l1)
try:
    div=n1/n2
    print('res of div:',div)
    print('l1[2]:',l1[2])
    print('l1[5]',l1[5])
except ZeroDivisionError as e: #print
    print('u r trying to dived a int number by zero')
    print('e value:',e)
except Exception as e:
    print('am at genarlized except block')
    print('e value:',e)
print('end')