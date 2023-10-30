a=input("enter your string--")

i=""
r=len(a)-1
while r>=0:

   i=i+a[r]
   r=r-1
   print(i)
if i==a:
  print("its palindrom")
else:
  print("its not")
