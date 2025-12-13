
cars = ["Ford", "Volvo", "BMW"]

# '''
# # What is an Array?
# # An array is a special variable, which can hold more than one value at a time.

# # If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

# '''

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

x = cars[0]
print(x)
cars[0] = "toyota"
print(cars[0])
x = len(cars)
print(x)

for x in cars:
  print(x)

cars.append("Honda")
cars.pop(1)
print(cars)
cars.remove("Honda")
print(cars)
cars.copy()
cars

# Python Iterators


# Python Iterators
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)

class Mynumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a +=1
    return x
  
myclass = Mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# for i in myiter:
#   print(i)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a +=1
      return x
    else:
      raise StopIternation
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
