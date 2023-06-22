a=int(input("digit --"))
b=int(input("digit --"))
c=int(input("digit --"))
"""if a>b:
    if a>c:
      print("a bada h")
    else:
       print("C bada h")
else:
   if b>c:
    print("b  bada h")
   else:
      print("c bada h")"""
if a>b and a>c:
  print( a, "bada h")
elif b>a and b>c:
  print(b, "bada hai")
else:
   print(c ,"bada h")
