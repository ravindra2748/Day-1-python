def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")
    

print_kwargs(name = "shaki",power = "lazer",mount = "everest",ways ="railways")
print_kwargs(name = "shaki")
