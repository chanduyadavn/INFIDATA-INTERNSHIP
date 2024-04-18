def create_account():
    global cname,cid,branch,bal
    cname=input('enter the coustmer name')
    cid=int(input('enter the id'))
    branch=input('enter the Branch name')
    bal=float(input('enter the balance amount'))
def deposite():
    global bal,dep
    dep=int(input('enter the amount'))
    bal+=dep
    print('the total amount',bal)
def withdraw():
    global bal,withdraw
    withdraw=int(input('enter the amount'))
    if withdraw<= bal:
        bal-=withdraw
        print(bal)
    else:
        print('Insufficent blance')

def display():
    print(cname)
    print(cid)
    print(branch)
    print(bal)

print('welcome to online banking')
while(True):
    choice=int(input('enter Your choice 1:create_account 2:deposite,3:withdraw, 4:display, 5:exit'))
    if choice==1:
        create_account()
    elif choice==2:
        deposite()
    elif choice==3:
        withdraw()
    elif choice==4:
        display()
    else:
        print('invalid choice')


