Pass = "Ravindrashah"


if len(Pass) <6:
    password = "Weak"
elif len(Pass) <=10:
    password = "Medium"
else:
    password = "Strong"

print(password)