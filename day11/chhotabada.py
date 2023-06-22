a=int(input("digit --"))
b=int(input("digit --"))
c=int(input("digit --"))
"""if a>b:
    if a>c:
      print("a is large")
    else:
       print("C is large")
else:
   if b>c:
    print("b is large")
   else:
      print("c is large")"""
if a>b and a>c:
  print( a, "large")
elif b>a and b>c:
  print(b, "large")
else:
   print(c ,"large")
