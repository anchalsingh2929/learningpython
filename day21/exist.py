while True:
    a=input("enter --")
   # if a=="exit" and len(a)<1:
       #else:
      # print("undefine alpha")
     #  break#
    if a=="a" or a=="i"  or a=="o" or a=="e" or a=="u":
        print("vowel")
    elif a!="exit" and  len(a)>1:
        print("undef.")
        break
    elif a=="exit":
        break
    else :
       print("consonant")
