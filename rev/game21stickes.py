stickes=21
a=input("enter your name user 1 -- ")
b=input("enter your name user 2 -- ")
while True:
   usr1=int(input(a+" take sticks (1-4) - "))
   while usr1>4:
     usr1=int(input(" wrong input, take sticks again (1-4) - "))
   stickes-=usr1
   if stickes<=1 :
     print(" yaayy",a," you win hurrraaahhh!!!!🤩️🤩️🤩️")
     break
   usr2=int(input(b+" take sticks (1-4) - "))
   while usr2>4:
     usr2=int(input("wrong input,  take sticks (1-4) - "))

   stickes-=usr2
   if stickes<=1:
      print( "yyayyy",b,"you win hurraaahhh!!!!!🤩️🤩️🤩️") 
      break
   
