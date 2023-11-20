a=int(input("enter no --"))
w=0
for i in range(2,a):
   if a%i==0:
     w=1
     print("not prime no.")
     break   
if w==0:
   print("its a prime no.")
     
