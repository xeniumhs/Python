#list example
emp1=["Hari",23,"ktm"]
emp=["ram",20,"Bkt"]
dep1=["Cs",1001]

print("Employee Data:\n")
print("Name: %s,ID: %d, Address: %s" %(emp[0],emp[1],emp[2]))
print("Name: %s,ID: %d, Address: %s" %(emp1[0],emp1[1],emp1[2]))
print("Name: %s , ID : %d"%(dep1[0],dep1[1]))
print("Name: %s , ID : %d"%(dep1[0],dep1[1]))
print(type(emp), type(dep1))

print(type(emp[0]),type(emp[1]))


##      Multi-Dimensional list

List=[['Welcome','to'],['Python','class']]

#accessing from multi-dimensional list

print(List[0][1],List[1][0])
print(List[0][0],List[1][1])

#we use list() constructor when creating new list

fruit_t=("a","b","c")  #tuple
fruits=list(fruit_t)
fruits_t=tuple(fruits)
print(fruit_t,type(fruit_t))
print(fruits,type(fruits_t))
print(fruits_t,type(fruits_t))

print(fruits[0:2])
print(fruits[-2:-1])

fruits=['a', 'b', 'c']

for a in fruits:
    print(True)

fruits[0]="Mango"
print(fruits)

fruits[1:3]=["apple"]
print(fruits)

fruits.insert(1,"banana")
print(fruits)

fruits.append("pear")
print(fruits)

fruits.remove("banana")
print(fruits)


list=['x','y','z']
fruits.append(list) #adding another list to existing fruits list
print(fruits)

fruits=['Mango', 'apple', 'pear']#redefining values
fruits.extend(list)     #adds elements of new list to existing fruits list
print(fruits)
def func():
   print(7)
   print("Inside")
print("Function")
func(); 