n1=int(input('enter the first nnumber'))
n2=int(input('enter the second number'))
try:
    div=n1/n2
    print('res of div:',div)
except ZeroDivisionError as e:
    print('u r trying to dived a intger num by zero')
    print('e value:',e)
print('end')