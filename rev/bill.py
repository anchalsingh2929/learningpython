c= int(input("enter no. of calls-"))
if c<=100:
   print( c*2, "rs")
elif c<=300:
   print( (100*2)+(c-100)*3,"rs")
elif c<=500:
   print( (100*2) + (200*3) + (c-300)*4 , 'rs')  
elif c>500:
   print(  (100*2) + (200*3) + (200*4 ) + (c-500)*5 , 'rs')  
