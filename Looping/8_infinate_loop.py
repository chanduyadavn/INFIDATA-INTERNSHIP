l=int(input("enter the length"))
b=int(input("enter the bredth"))
h=int(input("enter the height"))
while(True):
    choice=int(input('enter the choice 1:Area ,2:volume, 3:Exit'))
    if(choice==1):
        area=l*h
        print('area is',area)
    elif(choice==2):
        vol=l*b*h
        print('volume is',vol)
    elif(choice==3):
        exit(0)
    else:
        print("invalid choice")
