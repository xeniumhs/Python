n=5
'''
*
**
***
****
*****
'''
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(i,n):
        print("*",end="")
    print()


'''
    *
   **
  ***
 ****
*****
'''
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

'''
*****
*****
*****
*****
*****
'''
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

'''
*****
 ****
  ***
   **
    *
'''
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()

# for i in range(n):
#     for j in range(i):
#         print(" ",end="")         #scalene triangle
#     for j in range(i+1):
#         print("*",end="")
    
#     print()

'''
Pyramid
  *
 * *
* * *
'''

for i in range(n):
    for j in range(i,n):
        print(" ", end="")
    for j in range(1,i):
        print("* ",end="")
    print()

for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()


'''
1
2 3
4 5 6
7 8 9 10'''

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
num=1
for i in range(1, n ):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
num=10
for i in range(1,n):
    for j in range(1, i + 1):
        print(num, end=" ")
        num -= 1
    print()

'''
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''
for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    # lower
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()


x="NEPAL"
l=len(x)
for i in range(l,0,-1):
    for j in range(i):
        print(x[j],end="")
    print()

for i in range(n):
    num=1
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i):
        print(num,end="")
        num+=1
    for j in range(i+1):
        print(num,end="")
        num-=1
    print()

for i in range(n):
    num=i
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i):
        print(num,end="")
        num-=1
    for j in range(i+1):
        print(num,end="")
        num+=1
    print()


for i in range(n):
    num=1
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i):
        print(num,end="")
        num+=1
    for j in range(i+1):
        print(num,end="")
        num+=1
    print()




for i in range(n):
    for j in range(i + 1):
        # Print alternating 1s and 0s based on the position
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()  # Move to the next line

n=10
for i in range(n):
    for j in range(i + 1):
        # Print alternating 1s and 0s based on the position
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()  # Move to the next line

n=5
num=1
for i in range(n):
    for j in range(2):
        print(num,end=" ")
        num+=1
    print()
num=0
for i in range(n):
    for j in range(i+1):
        print(num,end="")
    num+=1
    print()
    
j="hello"

def greet(name):print("Hello,",name) 
name=input("Enter your name: ")  
greet(name)
if name=="Alice" :print("Welcome, Alice!")  
else: print("Welcome, stranger!") 
for i in range(5):  print(i," ",end='') 
print("Done!")
