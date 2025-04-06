# animals=['cat','dog','rabbit']
# animals.remove('dog')
# # animals.remove('fish')

# print(animals)

num=[1,2,3,4,5,6,7,8,19,11,15,12,13,14]
# print(num)
# num.remove(3)
# num.remove(5)
# print("list num after removing 2 elements: ")
# print(num)

# for i in range(6,9):
#     num.remove(i)
#     print(num)
# num.pop()       #removes from last
# print(num)
# removedElement=num.pop(3)      #removes from that certain position
# print(num)
# print("Removed Element: ",removedElement)

print(num)
# del num           #deletes whole list
# num.clear()         #clear the whole list/removes all items from list but null list remains
# print(num)

num.sort()
print(num)

fruits=['banana','apple','strawberry','mango']
fruits.sort(reverse=True)       #descending order
print(fruits)

fruits.sort()       #ascending order
print(fruits)
fruits=['banana','apple','strawberry','mango']
print(fruits)
print(sorted(fruits))
#sorting A-Z the a-z
#capitals always first

#sort and sorted is different
#sorted(iterable,key,reverse)

print(fruits)       #when used sorted original list is unchanged
print("Descending Order = ",sorted(fruits,reverse=True))
print(sorted(fruits,key=len))

#sorted----list,tuple,string,dict,set,frozen set


a=[]
for i in range(10):
    a=list(range(i))
    print(a)
print(a)
print("Length = ",len(a))
for i in range(len(a)):
    print(a[i],end=" ")

for x in a:
    print(x,end=" ")


##LIST Comprehension_____----Not in Syllabus
#   Syntax:
#  newlist=[expression(element) for element in oldlist if condition]
newList=[x for x in a if 2 in a]
print(newList)

squares=[x**2 for x in range(1,11)]
print(squares)

#filter even,odd
#upper();  capitalize all elements in list

#matrix using list comprehension

matrix=[[j for j in range(3)]for i in range(3)]
print(matrix)

#Slice in list

L=['a','b','c','d','e','f']
print(L[1:4])


#COPY in List
myL=L.copy()
print(myL)
h="hello"

