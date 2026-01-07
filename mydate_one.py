# import datetime
# import math
# import json
import re

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(2020, 5, 17)
# print(x)


# x = datetime.datetime(2018, 4, 8)

# print(x.strftime("%G"))

# y = min(5,10,25)
# x = max(5,10,25)
# print(x)
# print(y)

# x = abs(-7.25)
# print(x)

# x = pow(4,3)
# print(x)

# x = math.sqrt(64)
# print(x)

# n =math.ceil(1.6)
# y = math.floor(1.4)
# print(n)
# print(y)

# c = math.pi
# print(c)
# json file example

# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y =json.loads(x)
# print(y["name"])

# x = {
#     "name" : "John",
#     "age" : 30,
#     "city" : "New york"
# }

# y = json.dumps(x)
# print(y)


# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# x = {
#  "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]

# }

# # print(json.dumps(x))

# json.dumps(x,indent=4)
# json.dumps(x, indent=4, separators=(". ", " = "))
# json.dumps(x,indent=4 , sort_key = True)

# txt = "The rain in spain"
# x = re.search("\s" ,txt )
# y = re.findall("portugal", txt)
# s = re.split("\s", txt  ,1)
# print(y)
# print("The first white-space character is located in position:", x.start())
# print(s)
# r = re.sub("\s" , "9" , txt , 1)
# print(r)

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())
# print(x.string)
# print(x.group())

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")


# x = -1
# if x<0:
#   raise Exception("sorry , no number below zero")

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integer are allowed")
# price = 49000
# fruit = "apple"
# item = 23
# txt = "The rpice of {:.2f} very low"
# print(txt.format(price,fruit,tax))


# print(txt.format(price))

# def myconverter(x):
#     return x* 0.308

# txt = f"The plane is flying at a {myconverter(30000)} meter alt"
# print(txt)

# myorder = "I want {1} of item {0} for {2:.2f} rupees"
# print(myorder.format(fruit,item,price))


# age = 36
# name = "John"

# txt = "His name is {1}. {1} is {0} years old"
# print(txt.format(age, name))

# myorder = "I have a {carname} , it is a {model}"
# print(myorder.format(carname = "Ford" , model = "Mustang"))

# x = None
# print(x)

# x = None
# print(type(x))

# result = None
# if result is not None:
#     print("No result yet")
# else:
#     print("Result is ready")

# print(bool(None))


# def myfunc():
#     5
# x = myfunc()
# print(x)

# print("Enter your name :")
# name = input()
# print(f"HELLO R{name}")

# name = input("Enter your name:")
# print(f"Hello {name}")


# name = input("Enter yout name:")

# print(f"Hello {name}")

# fav1 = input("What is your animal:")
# fav2 = input("what is your sports")
# fav3 = input("what is your color:")

# print(f"Do you play {fav2} {fav1} with {fav3} R")


import math

def get_square_root():
    try:
        # 1. Use float() directly to allow decimals like 2.5
        user_input = input("Enter a number: ")
        x = float(user_input)

        # 2. Check for negative numbers before calculating
        if x < 0:
            return "Error: Cannot calculate square root of a negative number."

        y = math.sqrt(x)
        return f"The square root of {x} is {y:.2f}" # Format to 2 decimal places

    except ValueError:
        # 3. Handle cases where user enters text or special characters
        return "Error: Please enter a valid numeric value."

print(get_square_root())


