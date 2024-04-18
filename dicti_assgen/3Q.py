d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
sum_of_pairs = sum(d1.values())
print("Sum of key-value pairs in the dictionary:", sum_of_pairs)

#correct one

d1={1:10,2:20,3:30}
l1=[]
for i in d1:
    {
        l1.append(i+d1[i])
    }
print('sum of key and value pair',l1)
