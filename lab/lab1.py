import math
import sys

#1 print even no
for i in range (1,11):
 if i%2==0:
  print(i)

#2
print(5/2)
print(5//2)

#3
print(4*(6+5))
print(4*6+5)
print(4+6*5)
print(5>4,3==5)
print(not(5>4))
print(5>4 or 3==5)
print(True and True)
print(True==False)
print(not(True),not False)

#4
print(type(3*1.5+4))

#5
print(math.sqrt(9),9**2)

#6
a=4
b="hello"
c=5.5
print(type(a))
print(type(b))
print(type(c))

#7
a={3,3,3,4}
b=[a,b,c]
c=(111,22,233)
print(type(a))
print(type(b))
print(type(c))

#8
print("""Twinkle,Twinkle
                little star
                    how i wonder what you are""")

#9
print(sys.version)

#10
color_list=["Red","Green","Yellow","Black"]

#11
pi=3.14
r=6
print((4/3)*pi*r*r*r)

#12
# a=5
# b=4
# c=7
a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))


if(a==b==c):
 print(3*a)
else:
 print(a+b+c)
#13
a=int(input("Enter number: "))
b=int(input("Enter number: "))
sum=a+b

if sum>15 and sum<20:
 print(20)
else:
 print(sum)
#14
name="xenium"
age=19
address="bkt"
print(f"""name : {name}
addres:{address}
age:{age}""")

#15
x=4
y=3
print((x+y)*(x+y))

#16
print(name+address)

#17
x=30
y=20
print(x,"+",y,"=",x+y)

#18
a=4
b="hello"
c=5.5
print(type(a))
print(type(b))
print(type(c))

#19
name=input("Enter your name: ")
print("Good Morning ",name)

#20
a=input("Enter no. of roses: ")
b=int(a)
print(b)
print(type(a))