a=[1,2,-3,0,0,55]
p=0
n=0
z=0
for x in a:
  if x<0:
    n+=1
  elif x>0:
    p+=1
  elif x==0:
    z+=1
print(n,"neg and ",p,"positive and " , z, "zeros")    
    
