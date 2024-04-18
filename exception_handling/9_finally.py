l1=[6,7,8,9]
print('list l1 is:',l1)
try:
    print('l1[2]',l1[2])
    print('l1[5]',l1[5])

except ZeroDivisionError as e:
    print('an at ZeroDivisionError except Block')
    print('e value',e)
finally:
    print('am at finally block')
    print('executing at finally')
print('end')