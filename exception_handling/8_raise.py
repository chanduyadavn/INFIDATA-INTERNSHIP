print('raise keyword Demo')
try:
    raise ZeroDivisionError ('Demo Message')  #raise is used for to give explicit call to except block
except ZeroDivisionError as e:
    print('an at zeroDivisionError Except block')
    print('e value',e)
print('end')