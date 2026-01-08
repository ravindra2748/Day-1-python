class MyClass:
    x = 5

# p1 = MyClass()
# print(p1.x)

# del p1
# print(p1.x)

# Multiple object
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# class with init method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p1 = Person("Email" , 36)

print(p1.name)
print(p1.age)

# create class without init
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 23

print(p1.name)
print(p1.age)

# default value in init

class person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

p1 = person("yoy")
p2 = person("Tobia", 88)

print(p1.name , p1.age)
print(p2.name , p2.age)

#multiple perameter

class Person:
    def __init__(self,name,age,city,country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("lion",23,"Indore","India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def greet(self):
        print("Hello"+ self.name)

P1 = Person("Email", 23)
P1.greet()

class Person:
    def __init__(self , name):
        self.name = name

    def printname(self):
            print(self.name)

p1 = Person("TOT")
p2 = Person("ffg")

p1.printname()
p2.printname()


class Peraon:
    def __init__(self,name):
        self.name = name

    def printname(self):
        print(self.name)

p1 = Person("TOT")
p2 = Person("ffg")

p1.printname()
p2.printname()

# Use the words myobject and abc instead of self:

class person:
    def __init__(myobj,name):
        myobj.name = name

    def greet(abc):
        print("Hello " + abc.name)

p1 = person("uv")
p1.greet()

# Accessing Properties with self
# You can access any property of the class using self:

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year,self.model,self.brand}")

    
car1 = Car(1997,"corolla","Toyota")
car1.display_info()
