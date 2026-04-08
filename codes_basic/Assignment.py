# age = int(input("Enter your age :-"))
# if age<13:
#     print("child")
# elif age >=13 and age <=19:
#     print("Teenager")
# elif age >=20 and age <=59:
#     print("Adult")
# elif age>=60:
#     print("Senior")

# age = int(input("Enter your age :- "))

# if age < 13:
#     print("Child")
# elif 13 <= age <= 19:
#     print("Teenager")
# elif 20 <= age <= 59:
#     print("Adult")
# else:
#     print("Senior")

age = int(input("Enter your age :- "))
day = str(input("enter your day:- "))

# if age>=18:
#     print("Movie ticked price $12")
# elif age<=18:
#     print("Movied ticket price $8")
# elif 0>age<100 and day == "Wednesday":
#     print("for adult 10 and children 6$ ")

price = 12 if age >=18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $ ", price)