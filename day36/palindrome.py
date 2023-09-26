a=input(" string -- ")
i=len(a)-1
b=""
while i>=0:
 b=b+a[i]
 i=i-1
if b==a:
   print("its palindrome")
else:
    print("its not a palindrome")
