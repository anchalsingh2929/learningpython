# 0, 1, 1, 2, 3, 5, 8
def fib(s):
    r=[]
    
    a=0
    b=0
    c=1
    adding=0
    
    while a<=p:
        r.append(c)
        adding=b+c
        b=c
        c=adding
        a+=1
    return r
p=int(input("enter no."))
m=fib(p)    
print(m)