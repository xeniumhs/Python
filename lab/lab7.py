# Lab 7 
# Python function 


# 1. Create a function named “greet” that prints “Hello World!”. 

# def greet():
#     print("Hello World!")

# greet()

# 2. Write a Python function to find the maximum of three input numbers. 

# def maximum(a,b,c):
#     newList=[a,b,c]
#     newList.sort()
#     print("Maximum =",newList[2])

# a,b,c=int(input("Enter number")),int(input("Enter number")),int(input("Enter number"))
# maximum(a,b,c)


# 3. Write a Python function to calculate the factorial of a number (a non-negative integer) with and without 
# using recursion. The function accepts the number as an argument.  


# 4. Write a python function that takes two parameters length and width and returns the area and perimeter 
# of a rectangle. 
# 5. Modify above function so that it has default values of 2 for both length and width. 
# 6. Write a python function that accepts radius and returns the area and circumference of a circle. Import Pi from Math. 

# import math
# def circle(r):
#     area=math.pi*r*r
#     circumference=2*math.pi*r
#     print("Area =",area)
#     print("circumference =",circumference)

# circle(7)

# 7. Write a function that takes two arguments, name and age and returns a dictionary with these as keys and 
# their respective values. 

def dictMaker(name,age):
    dict={'Name':name,
          'Age':age}
    print(dict)

dictMaker('xen',18)

def dict_maker(n,a):
    return dict(
        name = n,
        age=a
    )
print(dict_maker('wwww',32))
# 8. Write a Python function to find the maximum and minimum value, sum and multiplication of all the 
# numbers in a list. 
# 9. Write a python program to demonstrate positional argument and functional arguments in function. 
# 10. Create a function that takes a list and a number, return a list after adding the number to the list preventing 
# it from changing the original list. 
# 11. Write a function that takes a list of numbers and print each number doubled. 

# def listDouble(x):
#     for i in x:
#         a=2*i
#         newList.append(a)
#     print(newList)

# list=[1,2,4,5]
# newList=[]
# listDouble(list)

# 12. Defines a function called calculate_average that takes a list of numbers as input and calculate the 
# average of list. Finally, the function returns the average of that list. 

def calculate_average(x):
    sum=0
    n=len(x)
    for i in x:
        sum+=i
    print(sum/n)   

list=[1,2,3,4]
calculate_average(list)     

# 13. Write a Python function that checks whether a passed string is a palindrome or not. 
# 14. Write a Python function that takes a string as input and counts the number of uppercase and lowercase 
# characters in the string.  

# 15. Write a Python recursive function to find out factorial of any given number.

# def factorial(n):
#     if n==0 or n==1:
#         return(1)
#     else:
#         return n*factorial(n-1)

# a=int(input("Enter number: "))
# print(factorial(a))