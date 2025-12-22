string=input("Enter your name--")
char=input("Enter Your Character--")
index=0
count=0
while index<len(string):
    if char==string[index]:
        count=1
        
    index+=1  
if count:
    print(True)

else :
    print(False)    



