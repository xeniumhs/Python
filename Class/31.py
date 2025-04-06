#WAP to input 3 no. and display the largest and the smallest no. among them
while 1:
    x,y,z=int(input("Enter three numbers")),int(input("Enter three numbers")),int(input("Enter three numbers"))
    print("Given no. are ",x,y,z)
    if x>y and x>z:
        print("Largest no. ",x)
    elif y>z:
        # print("Given no. are ",x,y,z)
        print("Largest no. ",y)
    else:
        # print("Given no. are ",x,y,z)
        print("Largest no. ",z)

    if x<y and x<z:
        # print("Given no. are ",x,y,z)
        print("Smallest no. ",x)
    elif y<z:
        # print("Given no. are ",x,y,z)
        print("Smallest no. ",y)
    else :
        # print("Given no. are ",x,y,z)
        print("Smallest no. ",z)


    print(f"{x}is x in {x},{y},{z}")

