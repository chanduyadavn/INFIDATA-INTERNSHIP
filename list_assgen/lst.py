l1=[]
for i in range (6):
    num=int(input('enter a num to the list'))
    l1.append(num)
print('elemet \t \t frequnecy')
for i in l1:
    print(i,end='\t\t\t')
    print(l1.count(i))