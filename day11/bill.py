c=int(input("enter your calls --"))
if c<=100:
  print(c*2, "rs/-")
elif c<=300:
   print((c-100)*3+100*2, "rs/-")
elif c<=500:
   print(100*2+200*3 +(c-300)*4.5, "rs/-")
elif c>500:
  print(100*2+200*3+200*4.5+ (c-500)*5 , "rs/-")
