# WAP to take n num from users and sum them until 0 is entered
sum=0
num= int (input("Enter a number: "))

while num!=0:
    sum=sum+num
    num= int (input("Enter a number: "))
print("SUM =",sum)