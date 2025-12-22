a=input("Enter your name--")
index=0
b=0
while index < len(a):
    if a[index] in "aeiou":
        b+=1
        

    index+=1
print(b)    


