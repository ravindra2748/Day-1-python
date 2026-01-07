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

# with init method
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

