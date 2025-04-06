class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __str__(self):
        return f"{self.name} is {self.age} year(s) old."
    def bark(self):
        print("bark bark!")
    def doginfo(self):
        print( self.name + " is "+str(self.age) + " year(s) old.")
    def birthday(self):
        self.age+=1
    
breed=Dog("Shepherd",2)
print(breed.name)
print(breed.age)
breed.bark()
