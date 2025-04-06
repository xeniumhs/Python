# Lab 6 
# Python Dictionary 
# 1. Write a Python program to create a python dictionary with the following key-value pairs: 
# ‘name’:’Hari’, ‘age’:’29’, ‘city’:’Bhaktapur’. Then print the value associated with the key ‘age’. 

# myDict={
#     'name':"Hari",
#     'age':29,
#     'city':'Bhaktapur'
# }
# print("Age: ",myDict['age'])


# 2. Write a Python program to add a key-value pair ‘occupation’: ‘Engineer’ into an existing dictionary.

# myDict={
#     'name':"Hari",
#     'age':29,
#     'city':'Bhaktapur'
# }

# myDict["occupation"]="Engineer"
# print(myDict)

# # 3. In the above dictionary, change the value of ‘city’ to ‘Kathmandu’. 
# myDict['city']="Kathmandu"
# print(myDict)

# # 4. Write a Python program to remove a key ‘age’ from the dictionary. 

# myDict.pop("age")
# print(myDict)


# 5. Write a python program to loop to iterate through the dictionary from the first question and print all 
# keys and their corresponding values. 
 
# # 6. Write a Python program to get the key, value and item in a dictionary. 
# print("Keys: ")
# for i in myDict.keys():
#     print(i)
# print("Values: ")
# for i in myDict.values():   
#     print(i)
# print("Items: ")
# for i in myDict.items(): 
#     print(i)
# # 7. Write a python script to check whether the key ‘email’ exists in the dictionary. If it does not exist 
# # print ‘key not found’. 
# if "email" not in myDict:
#     print("Keys not found!")

# # 8. Write a Python script to merge two Python dictionaries. 
# # dict1 = {‘a’: 1, ‘b’: 2} and dict2 = {‘b’: 3, ‘c’:4} merge them into a single dictionary. What happens 
# # to the value of the key ‘b’? 

# dict1={'a':1,'b':2}
# dict2={'b':3,'c':4}

# mydict=dict1|dict2
# print(mydict)

# dict1.update(dict2)
# print(dict1)

# 9. Create a script that converts a list of tuples, [(‘a’, 1), (‘b’, 2), (‘c’, 3)], into a dictionary.
# list_tuple=[('a',1),('b',2)]
# myDict=dict(list_tuple)
# print(myDict)
# print(type(myDict))

# 10. Use the get() method to fetch the value of ‘age’ from the above dictionary. If the ‘age’ is not a key, 
# it should return ‘Key not available’. 

# myDict={
#     'name':"Hari",
#     # 'age':29,
#     'city':'Bhaktapur'
# }
# age=myDict.get("age","keys not available")
# print(age)

# 11. Write a Python program to find all keys in a dictionary that have the given value. 
# myDict={
#     'a':1,
#     'b':1,
#     'c':3
# }

# value1=1

# print([key for key, value in myDict.items() if value==value1])

# 12. Write a Python program to sort a dictionary by its keys. 

# myDict={
#     'name':"Hari",
#     'age':29,
#     'city':'Bhaktapur'
# }

# myDict=dict(sorted(myDict.items()))
# print(myDict)


# 13. Write a Python program to sort a dictionary by values instead of keys

# myDict={
#     'name':"Hari",
#     'age':"29",
#     'city':'Bhaktapur'
# }

# # Sort by values
# sorted_dict = dict(sorted(myDict.items(), key=lambda item: item[1]))

# print(sorted_dict)  

# # 14. Write a Python script to check whether a given key already exists in a dictionary

# n=input("Enter keys: ")
# if n in myDict.keys():
#     print("Keys is present")
# else:
#     print("Keys not found")

# 15. Write a Python program to sort a list alphabetically in a dictionary. 
# Sample: num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 
# Output: {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

mydict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 
mydict=dict(sorted(mydict.values()))
print(mydict)