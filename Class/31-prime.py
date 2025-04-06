###find prime number

a=int(input("Enter a number: "))
i=2
while i<a:
    if a%i==0:
        print(f"{a} is not prime")
        break
    i+=1
if i>=a:
    print("prime")

# if a<=1:
#     print(f"{a} is not a prime number. ")
# if a==2 or a==3:
#     print(f"{a} is a prime number. ")
# if a%2==0 or a%3==0:
#     print(f"{a} is not a prime number. ")
# else:
#     print(f"{a} is a prime number. ")


### MATCH CASE STATEMENT

a=int(input("Enter no. "))

match a:
    case 1:
        print("One")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4|5|7|6:
        print("above")
    case a if a>8 & a<10:
        print("above above")
    case a if a>10:
        print("uppp")

    case _:  ##default
        print("Zero")