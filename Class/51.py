# # #Iterating over a string
# # s="Engineering"

# # for i in s:
# #     print(i,end="")


# fruits=["apple","banana","cherry",1]
# for x in fruits:
#     print(x,end=",")
# a=0
# for x in fruits:
#     print(f"x[{a}]=",x)
#     a+=1

# #factorial

# num=int(input("Enter the number: "))
# fac=1
# for i in range(num):
#     fac+=fac*i
# print("factorial is: ",fac)
# # fibonaccii
# # 0 1 1 2 3 5 8 13 

# n=int(input("Enter the num:"))
# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c


# for x in range(4,7):
#     print(x, end=" ")
# print("\n")
# for x in range(0,20,2): #(start , end , steps)
#     print(x, end=" ")
# print("\n")
# for x in range(-50,25,7): #(start , end , steps)
#     print(x, end=" ")

Numbers=[x for x in range(11)]
print(Numbers)

#iterating over dict


for i in range(0,6):
    for j in range(0,i):
     print("* ",end="")
    print()

num=int(input("Enter no.:"))

# for x in num:
#    print(x)