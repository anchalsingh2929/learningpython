a=open("fruit.txt")
b=a.readlines()
for x in b:
  print(x ,end="")
a.close()