# list1 = [10, 20, 4, 45, 99]

# for i in list1:
#     if i%2==0:
#         print(i)

# input="a4b3c2d1"

# #op=aaaabbbccd

# num = 5
# def number(num):
#     for num in range(1,10):
#         if num%2==0:
#             print("prime number")
#         else:
#             print("not a prime number")
        
        
# number(5)


# list1 = ["K", "ee", "r", "th"]
# list2 = ["", "", "ha", "na"]
# # Keerthana

# list3 = list1+list2
# print(list3)
# list4 = list3.remove('')
# print(list4)

list1 = [10, 20, 4, 45, 99]

largest = list1[0]
second_largest = list1[0]

for num in list1:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and num > second_largest:
        second_largest = num

print("Second highest number is:", second_largest)


input = "a4b3c2d1"

output = ""
char = ""

for i in input:
    if i.isalpha():
        char = i
    else:
        count = int(i)
        for _ in range(count):
            output += char

print(output)


num = 5

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

list1 = ["K", "ee", "r", "th"]
list2 = ["", "", "ha", "na"]

result = ""

for i in range(len(list1)):
    result += list1[i] + list2[i]

print(result)

