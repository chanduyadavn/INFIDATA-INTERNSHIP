#removing method using pop()
# remove an item with provdd key and retun the value
#clear() all @ once will be removed
#popitem() used to remove and return an arboatry value(key,value)

d1={1:2,2:4,3:9,4:16,5:25,6:36}
print(d1)

print('pop value is:',d1.pop(2))
print('update dictonary is:',d1)

print('pop item is:',d1.popitem())     #remove an arbitary item,retuen(key,value)
print('update dictonary is:',d1)

d1.clear()                               #remove all the elements
print('update dictinoary is:',d1)

del d1            #delete thye dic itself
print(d1)         #error