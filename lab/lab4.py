#11


# myList=[1,2,2,4,5,6,6,7,9]
# print(myList)
# myList=list(set(myList))
# print(myList)

# 12.Write a Python Program to merge two lists and removes all duplicates from the combined 
# list. 

# a=[1,2,2,4,5,6,6,7,9]
# b=[3,4,5,6,7,3,9,10]

# a+=b
# a=list(set(a))
# print(a)



# 19.

mylist = [1, 2, 3, 4, 5]

for i in mylist:
    a = str(i)
    index = mylist.index(i)
    b = "emp" + a
    mylist[index] = b

print(mylist)
