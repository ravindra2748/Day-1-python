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