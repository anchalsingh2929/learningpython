def get_num():
    try:
       return float(input("enter float digit -"))

    except:
        print("you are typing wrong value enter float digit only ")   
    
    finally:
        print("finally block")


print(get_num())
