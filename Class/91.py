# #using dict
# myDict = dict({1:"one",2:"two"})
# print(myDict)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x=car.keys()
# print(x)
# car["color"]="White"
# print(x)

# def keysMod(dictName):
#     key= dictName.keys()
#     print(key)
#     choice=0
#     while choice!='n':
#      choice=input("Enter Choice") 
#      key=input("Enter Keys: ")
#      value=input("Enter Values: ")
#      dictName[key]=value

# # xen={'Name':'xenium',
# #      'address':'bkt',
# #      'age':19}
# xen={}

# keysMod(xen)
# print(xen)



car={}
print(car)
choice=input("Enter y/n: ")
while choice!='n':
    key=input("Enter key: ")
    value=input("ENter values: ")
    car[key]=value
    print(car)
    print("add?")
    choice=input("ENter y/n: ")

#adding dict into dict  at first it is null
# (nested dict)