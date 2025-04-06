#######        LAB 2
        # Python Basics 2
# 1. Write a Python program to calculate the difference between a given number and 17. If the
# number is greater than 17, return twice the absolute difference. 
# 
num=int(input("Enter the number: "))
if num>17:
    print(2*(num-17))
else:
    print(num-17)
# 2. Write a Python program that determines whether a given number (accepted from the user) is
# even or odd, and prints an appropriate message to the user. 
# 
num=int(input("Enter a num: "))
if num%2==0:
    print(num," is even.")
else:
    print(num," is odd.")
# 3. Write a Python program to count the number 4 in a given list. 
# 
list=[1,2,4,5,6,4,23,4,4,9]

count=list.count(4)
print("Count of 4 = ",count)

# 4. Write a Python program to swap two variables. 
#
x=int(input("Enter the num x : "))
y=int(input("Enter the num y : "))

x,y=y,x
print("x=",x,"y=",y)
 
# 5. Write a Python program to check whether a variable is an integer, or string, or a list, or tuple, or
# set. 
# 

# 6. Write a Python script that takes two numbers as input and prints their sum, difference, product,
# and quotient.
# 
num1=int(input("Enter the 1st num: "))
num2=int(input("Enter the 2nd num: "))

print("Sum=",num1+num2)
print("Difference=",num1-num2)
print("Product=",num1*num2)
print("Quotient=",num1/num2)
# 7. Take an input from user then reverse the string using slicing.
# 
s=input("Enter the string: ")
print(s[::-1])
# 8. Write code to take input from user and store it in a variable spam then print Hello if 1 is stored
# in spam, print Hi if 2 is stored in spam, and print Greetings! if anything else is stored in spam. 
# 
spam=int(input("Enter the num "))
match spam:
    case 1:
        print("Hello")
    case 2:
        print("HI")
    case _:
        print("Greetings!")
# 9. Write a Python script that takes two numbers as input and prints their sum, difference, product,
# and quotient using match case.
# 
num1=int(input("Enter the 1st num: "))
num2=int(input("Enter the 2nd num: "))

opt=int(input('''Enter operation:
                1. sum
                2. Difference
                3. Product
                4. Quotient
                '''))
match opt:
    case 1:
        print("Sum=",num1+num2)
    case 2:
        print("Difference=",num1-num2)
    case 3:
        print("Product=",num1*num2)
    case 4:
        print("Quotient=",num1/num2)
# 10. Write a script that asks the user for their name and age, then prints a message that tells them the
# year in which they will turn 100 years old.
# 
name=input("Enter the name: ")
age=int(input("Enter age: "))

year=2081
byear=year-age
year=byear+100
print("Hello! ",name," You will turn 100 in the year ",year)
# 11. Create a Python script that converts temperature from Fahrenheit to Celsius and vice versa, based
# on user input
# 
temp=input("Enter the temperature: ")
choice=int(input("""Enter if it is 
                 1. Fahrenheit or 
                 2. Celsius"""))
match choice:
    case 1:
        print("IN Celsius:",(temp-32)*(5/9))
    case 2:
        print("IN Fahrenheit:",(temp*(9/5))+32)
    case _:
        print("Invalid")
# 12. Create a program that asks for an age and prints “Child” if the age is less than 12, “Teenager” if
# the age is between 13 and 19, and “Adult” for ages 20 and above
# 
age=int(input("Enter age: "))

if age<=12:
    print("Child")
elif age>12 and age<=19:
    print("Teenager")
else:
    print("Adult")
# 13. Write a python script that takes a letter grade (A, B, C, D, F) as input and prints the
# corresponding grade point average (GPA). For example, A = 4.0, B = 3.0, C = 2.0, D = 1.0,
# F=0.0. Include an else statement to handle invalid inputs.
# 
grade=input("Enter grade: ")

match grade:
 case 'A':
        print("A=4.0")
 case 'B':
        print("A=3.0")
 case 'C':
        print("A=2.0")
 case 'D':
        print("A=1.0")
 case 'F':
        print("A=0.0")
 case _:
        print("Invalid")
# 
# 14. Write a python program that takes a number and prints whether it is “Even”, “Odd”, “Zero”, or
# “Invalid” for non-integer inputs. This program should first check if the input is a valid integer
# and then check for the other conditions.
# 
num=input("Enter the number: ")

if(int(num)==True):

 if int(num)%2==0:
    print("Even")
 elif int(num)==0:
    print("Zero")
 else:
    print("odd")
else:
    print("invalid")

# 
# 15. An extra day is added to the calendar almost every four years as February 29, and the day is
# called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25
# days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
#           • The year can be evenly divided by 4, is a leap year, unless: 
#           • The year can be evenly divided by 100, it is not a leap year, unless: 
#           • The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800,
# 1900, 2100, 2200, 2300 and 2500 are not leap years.
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True
# otherwise return False.

year=int(input("Enter year"))

if year%4==0:
#      print(year," Leap year")
  if year%100==0:
     #print(year, " is Not Leap year")
     if year%400==0:
              print (year," Leap year")
     else:
          print("Not Leap Year")
  else:
        print("Leap Year")
else :
     print(False)

