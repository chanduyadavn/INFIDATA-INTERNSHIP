print("select a food category 1:veg 2:non-veg")
choice=int(input())
if(choice==1):
    print("you have slected veg category")
    menu=int(input("selcted menu 1:meals 2:Idli 3:dosa"))
    if(menu==1):
        print("you have selected meals")
    elif(menu==2):
        print("you have selected idli")
    elif(menu==3):
        print("you have selected dosa")
    else:
        print("menu not aviable")
elif(choice==2):
    print("you have selected no-veg")
    menu=int(input("selected menu 1:briyani 2:mutton 3:chiken"))
    if(menu==1):
        print("you have slected briyani")
    elif("menu==2"):
        print("you have slected mutton")
    elif(menu==3):
        print("you have slected chicken")
    else:
        print("menu not aviable")
else:
    print("invalid choice")
