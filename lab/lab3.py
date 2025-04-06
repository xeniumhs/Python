# Lab 3
# # Python Control Statement and Loops
# 1. Write a python program to find the sum of n natural numbers

# n=int(input("Enter the n: "))
# sum=0
# for i in range(n+1):
#     sum+=i
# print("Sum= ",sum)

# # 2. Write a program to read an integer from user. For all non-negative integers i < n, print i2.

# n=int(input("Enter the integer: "))

# for i in range(1,n):
#     print(i,"^2=",i**2)


# 3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note: Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# for i in range(7):
#     if i==3 or i==6:
#         continue
#     print(i)

# 4. Write a Python program to get the Fibonacci series up to n terms.

# n=int(input("Enter the number: "))
# a,b=0,1
# print(a,end=" ")
# for i in range(n-1):
#     c=a+b
#     a=b
#     b=c
#     print(a,end=" ")

# 5. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
# between 1500 and 2700 (both included).

# for i in range(1499,2701):
#     if(i%7==0 and i%5==0):
#         print("numbers which are divisible by 7 and multiples of 5, between 1500 and 2700: ",i)


# 6. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again
# until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the
# program will exit. Import random.

# import random

# while 1:
#     guessNum=int(input("Guess the number: "))

#     Num=random.randint(1,9)
#     print(Num)
#     if Num==guessNum:
#         print("Well Guessed! ")
#     else:
#         print("Try again..")


# 7. Write a Python program to input n numbers from user; count the number of even and odd numbers
# from the input numbers and exit until the user input ‘0’.
# Input numbers = (7, 4, 3, 8, 5, 6, 1, 2, 9)
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

# while True:
#     inputNum=int(input("Enter the num:"))
#     if inputNum==0:
#         break
#     print(inputNum,end=",")




# 8. Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
# Note: Use isdigit, isalpha and pass functions.

# strData="Python 3.2"
# countAlpha=0
# countDigit=0
# for i in strData:
#     print(i,end="")
# for i in strData:
#     if(i.isalpha()):
#         countAlpha+=1
#     elif(i.isdigit()):
#         countDigit+=1
# print("\nLetters",countAlpha)
# print("Digit",countDigit)


# 9. Write a Python program to develop a rock paper scissors game, restart the game until the user
# press ‘n’ when the game ends.
# import random
# rps=['r','p','s']
# n=True
# while n==True:
#     char=input("Enter the rock(r),paper(p),scissor(s):\nUser choice: ")

#     if char=='n':
#         n=False
    
#     elif char=='r' or char=='p' or char=='s':
#         compChar=random.choice(rps)
#         print(compChar)
#         if char=='r' and compChar=='p' or char=='p' and compChar=='s' or char=='s' and compChar=='r':
#             print("Computer Wins")
            
#         elif char=='s' and compChar=='p' or char=='r' and compChar=='s' or char=='p' and compChar=='r':
#             print("You Won!")
           
#         else:
#             print("Draw!")
#     else:
#         print("Try Again!")

# import random
# rps=['r','p','s']
# n=True

# def rpsName(char):
#     if char=='r':
#         print("Rock",end=" ")
#     if char=='p':
#         print("Paper",end=" ")
#     if char=='s':
#         print("Scissors",end=" ")


# while n==True:
#     print()
#     char=input("Enter the rock(r),paper(p),scissor(s):\nUser choice: ")

#     if char=='n':
#         n=False
    
#     elif char=='r' or char=='p' or char=='s':
#         print("User VS Computer")
#         rpsName(char)
#         compChar=random.choice(rps)
#         print("VS",end=" ")
#         rpsName(compChar)
#         print()
#         if char=='r' and compChar=='p' or char=='p' and compChar=='s' or char=='s' and compChar=='r':
#             print("Computer Wins")
            
#         elif char=='s' and compChar=='p' or char=='r' and compChar=='s' or char=='p' and compChar=='r':
#             print("You Won!")
           
#         else:
#             print("Draw!")
#     else:
#         print("Try Again!")


# 10. Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:
# Input a number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60

# num=int(input("Enter a num: "))

# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

# 11. Write a Python program that accepts a word from the user and reverses it.

# word=input("Enter a word: ")

# print( "Reversed word is: ", word[::-1])


# 12. Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# * 

n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()