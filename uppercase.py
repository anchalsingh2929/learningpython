a= input ("Enter Your name :- ")
index=0
b=c=d=0

while index<len(a):
    if a[index]>="A" and a[index]<="Z":
        b+=1
    elif a[index] >= "a" and a[index]<="z":
        c+=1
    else :
         d+=1 

    index +=1
print(f'A-Z are {b}, a-z are {c} and others are {d}.')
