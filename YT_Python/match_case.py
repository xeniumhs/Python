while 1:
 x=int(input("Enter the number : "))

 match x:
    case 0:
        print("it is zero")
    case 1:
        print("It is one")

    case _ if x==10:
        print("It is 10")
    
    # case _ if x!=10:
    #     print(x," Not equals 10 either ")
    
    case _: # _ for default
        print("Default")