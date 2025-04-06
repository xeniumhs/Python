# Lab 8
# Python functions 2
# 1. Write a Python program to reverse a string.

# def strrev (x):
#     print(x[::-1])

# str1='xenium'
# strrev(str1)



# 2. Write a Python function to check whether a number falls within a given range.

# def numRange(x,y,z):
#     if x>=y and x<=z:
#         print(f"{x} lies under the range({y},{z})")
#     else:
#         print(f"{x} doesn't lies under the range({y},{z})")

# x=int(input("Enter the number: "))
# y,z=int(input("Enter range: ")),int(input(":"))

# numRange(x,y,z)

# 3. Write a Python function that accepts a string and counts the number of vowel and consonant letters.

# def strCount(x):
#     vowelCount=0
#     consonantCount=0
#     x=x.lower()
#     for i in x:
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             vowelCount+=1
#         else:
#             consonantCount+=1
#     print(f"No. of Vowels is {vowelCount}")
#     print(f"No. of Consonant is {consonantCount}")

# strCount("HEllo")

# 4. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# def distList(list):
#     newlist=[]
#     for i in list:
#         if i not in newlist:
#             newlist.append(i)
#     print(newlist)


# list=[1,2,2,4,6,7,3,4,5]
# distList(list)


# 5. Write a Python function to create and print a list where the values are the squares of numbers between
# 1 and 20 (both included).

# def square ():
#     list=[]
#     for i in range(1,21):
#         x=i*i
#         list.append(x)
#     print(list)

# square()

# 6. Write a Python program to access a function inside a function.

# def num(a,b):
#     print("Outer function num")
#     def square(a,b):
#         print("Inner function square")
#         print(a*a,b*b)
#     square(a,b)
#     return square

# inner_func=num(5,4)

# result=inner_func(7,2)


# 7. Write a Python program to detect the number of local variables declared in a function.

# a=2
# def func():
#     x=1
#     y=2
#     z=5
#     count=0
#     localvars=locals()
#     print("Local varaibles are: ")
#     for i in localvars:
#         count+=1
#         print("\t",i)
#     print("Count of local variable is ",count)

# func()




# 8. Write a Python program to count the even and odd numbers from a given list and also print them
# separately.

# def listCount(list):
#     evenCount=0
#     oddCount=0
#     evenList=[]
#     oddList=[]
#     for i in list:
#         if i%2==0:
#             evenCount+=1
#             evenList.append(i)
#         else:
#             oddCount+=1
#             oddList.append(i)
#     print(f"Even count is {evenCount}")
#     print(evenList)
#     print(f"Odd count is {oddCount}")
#     print(oddList)

# listCount([1,2,2,3,4,5,6])

# 9. Write a Python program to find the power of a number using recursion function.
# Input: N = 2, P = 3 Output: 8
# Input: N = 5, P = 2 Output: 25

# def power(n,p):
#     if p==0:
#         return 1
#     else:
#         n*=power(n,p-1)
#         return n

# n,p=int(input("Enter number: ")),int(input("Enter power: "))

# print(power(n,p))

# 10. Write a Python function that takes a sentence as a parameter and print the words in ascending order.

# def ascedingSentence(sentence):
#     words=sentence.split()
#     # Sort the words in ascending order (case-insensitive)
#     sorted_words = sorted(words, key=str.lower)
    
#     # Print the sorted words
#     for word in sorted_words:
#         print(word,end=" ")


# x="Hello this is Xenium abc xyz pqr"
# ascedingSentence(x)


# 11. Write a Python a function that takes a string as argument and print the most common character in that
# string.

# 12. Write a Python function that takes a date in string format DD/MM/YYYY and checks if it is a valid
# date and in the correct format.

# 13. Write a Python function that takes a name (string) as argument and capitalizes the first and fourth letters
# of the input name.

# def capitalize_first_and_fourth(name):
#     if len(name) < 4:
#         # If the length of the name is less than 4, only capitalize the first letter
#         return name.capitalize()
#     else:
#         # Capitalize the first and fourth letters
#         result = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
#         return result

# # Example usage
# name = "xenium"
# result = capitalize_first_and_fourth(name)
# print(result)  

# 14. Write a Python function that takes a sentence, and return a sentence with the words reversed.

def reverse_word_Sentence(sentence):
    words=sentence.split()

    reverseWords=words[:-1]
    
    


x="Hello this is Xenium abc xyz pqr"
reverse_word_Sentence(x)

# 15. Write a Python function takes a two-word strings and find if both words begin with same letter or not. 