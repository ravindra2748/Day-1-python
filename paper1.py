'''
1. Print all prime numbers between two numbers

Input: 10, 20
Output: [11, 13, 17, 19]
'''
# CODE Answer 1st method
start = 10
end = 20

for num in range(start, end+1):
    if num >1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            print(num)

print("code answer 2nd method")

start = 10
end = 20

for num in range(start, end+1):
    count= 0

    for i in range(1,num+1):
        if num% i == 0:
            count +=1
    if count ==2:
            print(num)

# 2. Pyramid Pattern using *
#     *
#    ***
#   *****
#  *******
# *********

# Code answer
print("Pyramid Pattern using")

rows = 5

for i in range(rows):
    print(" "* (rows-i-1)+ "*"*(2*i+1))


for i in range(rows):
    print(" "*(rows-i-1),end="")
    print("*"*(2*i+1))

# 3. Merge Two Dictionaries
# Input

# {'a':1}, {'b':2}

# Output

# {'a':1, 'b':2}
print("Merge Two Dictionaries")

dict1 = {'a':1}
dict2  = {'b':2}

result = {**dict1, **dict2}
print(result)

dict3 = dict1 | dict2
print(dict3)

# 4. Count Uppercase and Lowercase Letters
# Input

# "Hello World"

# Output

# {'upper': 2, 'lower': 8}
print("Count Uppercase and Lowercase Letters")

text = "Hello World"

lower = 0
upper = 0

for ch  in text:
    if ch.isupper():
        upper += 1
    if ch.islower():
        lower +=1

print({'upper': upper, 'lower':lower})

#5. Extract All Numbers From a String

# Input

# abc123xyz45

# Output

# [123, 45]

print("Extract All Numbers From a String")

text = "abc123xyz45"

numbers = []
current_num = ""

for ch in text:
    if ch.isdigit():
        current_num = current_num +ch
    else:
        if current_num != "":
            numbers.append(int(current_num))
            current_num = ""
if current_num != "":
    numbers.append(int(current_num))

print(numbers)


