a = input("enter string : ")
rev = ""
last_index = len(a)-1

while last_index >= 0:
    rev += a[last_index]
    last_index -= 1
    
if a == rev:
    print("yes")
else:
    print("no")
    
