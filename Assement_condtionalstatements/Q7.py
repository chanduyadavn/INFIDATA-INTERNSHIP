present=int(input("enter the total number of working days"))
absent=int(input("enter the total number absent days"))
per=(present-absent)/present*100
print("class attended",per)
if per<75:
    print("you will not able to sit in exam")
else:
    print("you will be able to attend the exam")