pay=50000
location='Chennai'
if location == "Mumbai":
 print ("I'll take it!")
#Statement 1
elif location == "Chennai":
     if pay < 100000:
       print ("No way")
#Statement 2
     else:
       print("I am willing!")
#Statement 3
elif location == "Delhi" and pay > 40000:
    print("I am happy to join")
#Statement 4
elif pay > 60000:
     print("I accept the offer")
#Statement 5
else:
     print("No thanks, I can find something better")
#Statement6