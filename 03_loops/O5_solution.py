p_string = "teeterfdfsdao"

for char in p_string:
    print(char)
    if p_string.count(char) == 1:
        print("char is:", char)
        break

