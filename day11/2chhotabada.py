a=float(input("enter your digit --"))
b=float(input("enter your digit --"))
c=float(input("enter your digit --"))
d=float(input("enter your digit --"))
e=float(input("enter your digit --"))
if  a>b and a>c and a>d and a>e:
  print(a, " is large ")
elif b>a and b>c and b>d and b>e:
    print(b, " is large")
elif c>a and c>b and c>d and c>e:
   print(c, "is large")
elif d>a and d>b and d>c and d>e:
   print(d , "is large")
else:
 print(e, "is large")
