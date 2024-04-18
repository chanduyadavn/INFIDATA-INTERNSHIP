s1={10,30,20,10,40,50}
print("s1 is",s1)
s1.remove(20)
print("after remove(20)",s1)
s1.discard(30)
print("after discard(30)",s1)
s1.remove(30)
print("after remove",s1)   #it shows error if it has not the value is not their
s1.discard(30)
print("after discard",s1)  #it does not show any error if it does not contain any value