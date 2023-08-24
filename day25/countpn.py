x=1
y=0
z=0
v=0
while x<=5:
   i=int(input("enter no - "))
   if i<0:
      y=1+y
   elif i>0:
      z=z+1
   else:
     v=v+1
   x+=1
print(y,"negative and ", z, "positive and",v,"zeroes")
      

