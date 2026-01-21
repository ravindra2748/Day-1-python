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
## Update Log
# - Jan 8, 2026: Added new OOP examples and datetime utilities

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


# Python Class Properties

# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Email",22)

print(p1.name)
print(p1.age)

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota","Corolla")
print(car1.brand)
print(car1.model)

# modify properties

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Tobias" , 25)
print(p1.age)

p1.age = 26
print(p1.age)

# del perameter

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("nom", 90)

del p1.age
print(p1.name)
# print(p1.age)

# Class Properties vs Object Properties

# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

class Person:
    species = "Human"

    def __init__(self,name):
        self.name = name

p1 = Person("Email")
p2 = Person("fgd")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Modifying Class Properties
# When you modify a class property, it affects all objects:

class Peraon:
    lastname = ""

    def __init__(self,name):
        self.name = name

p1 = Peraon("nam")
p2 = Peraon("kam")

Peraon.lastname = "fres"


print(p1.lastname)
print(p2.lastname)

class Person:
    def __init__(self,name):
        self.name = name

p1 = Person("monkr")

p1.age = 23
p1.city = "oslo"

print(p1.name)
print(p1.age)
print(p1.city)

# Python Class Methods
# Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class

class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

class Calculator:
    def add(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a*b
    
calc = Calculator()
print(calc.add(5,3))
print(calc.multiply(5,8))

# Methods Accessing Properties
# Methods can access and modify object properties using self:

class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} year old"
    
p1 = Person("lool", 90)
print(p1.get_info())

# Methods Modifying Properties
# Methods can modify the properties of an object:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! you are now {self.age}")

p1 = Person("lola", 89)
p1.celebrate_birthday()
p1.celebrate_birthday()


# The __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed:

# Without the __str__() method:
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

p1 = Person ("mai", 90)
print(p1)

# With the __str__() method:

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = person("lol", 90)
print(p1)


# class Playlist:
#     def __init__(self,name):
#         self.name = name
#         self.songs = []

#     def add_songs(self,song):
#         self.songs.append(song)
#         print(f"Added : {song}")

#     def remove_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"Remove : {song}")

#     def show_songs(self):
#         print(f"playlist '{self.name} :")
#         for song in self.songs
#         print(f)

# new oce polymorphism


# class Playlist:
#     def __init__(self,name):
#         self.name = name
#         self.songs = []

#     def add_songs(self,song):
#         self.songs.append(song)
#         print(f"Added : {song}")

#     def remove_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"Remove : {song}")

#     def show_songs(self):
#         print(f"playlist '{self.name} :")
#         for song in self.songs
#         print(f)

def add(a,b):
    return a+b

add(7,8)

def multiply(a,b):
    return a*b

multiply(8,9)


def sub(a,b):
    return a-b

print(sub(5,3))

# Polymorphism

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")
    

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("FLY!")

car1 = car("maruti", "mustange")
boat1 = Boat("moris","mou")
plane1 = plane("Boeing","778")

for x in (car1,boat1,plane1):
    x.move()

# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail!")

class plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibia","IBIA20")
plane1 = plane("aakazu","990")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()