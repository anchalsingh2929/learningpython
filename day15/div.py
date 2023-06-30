a=int(input("enter your digit -- "))
if a%3==0 and a%5==0:
   print(a ,"is divisible by both ")
elif a%5==0:
   print(a,"is divisible by 5")
elif a%3==0 :
   print(a,"is divisible by 3")
else:
   print("not divisible ")
