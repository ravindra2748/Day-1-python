Distance = 8


if Distance < 3:
    Mode = "Walk"
elif Distance <= 15:
    Mode = "Bike"
else:
    Mode = "Car"

print(Mode)