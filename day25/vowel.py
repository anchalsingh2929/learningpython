s=1
v=0
c=0
while s<=5:
   w=input("enter alpha -- ")
   if w=="a" or w=="i" or w=="e" or w=="o" or w=="u":
       v=v+1
   else:
       c=c+1
   s=s+1  
print(v,"vowel and " , c, "consonant")
   
