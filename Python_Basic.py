# num1 = 20
# num2 = 30

# def multi(a,b):
#     multiply=a*b
#     if multiply <= 1000:
#         return multiply
#     else:
#         return a+b
    
# result = multi(num1,num2)
# print("the result is" ,result)

# result = multi(40,30)
# print("The result is" , result)

# print("Printing current and previous number and their sum in a range(10)")
# previous_num =0
# # for i in range(1,11):
# #     x_sum = previous_num + 1
# #     print("current number", i , "previous number", previous_num,"sum:", x_sum)
# #     previous_num=1

# for i in range(11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i


# str = "PYnative"
# S =(str[0:8:2])
# for i in S:
#     print(i)


# # accept input string from a user
# word = input('Enter word ')
# print("Original String:", word)

# # get the length of a string
# size = print(len(word))

# # iterate a each character of a string
# # start: 0 to start with first character
# # stop: size-1 because index starts with 0
# # step: 2 to get the characters present at even index like 0, 2, 4
# print("Printing only even index chars")
# for i in range(0, size - 1, 2):
#     print("index[", i, "]", word[i])

# word = input("Enter word")
# print("original str", word)

# x = list(word)
# for i in x[0::2]:
#     print(i)

# str = "Pynative"
# u = str.replace("P","n")
# print(u)


# numbers_x = [10, 20, 30, 40, 90]

# x=(numbers_x[0])
# y=(numbers_x[-1:])

# def check(x,y):
#     if x==y:
#         return True
#     else:
#         return False

# print(check(x,y))

# def check(lst):
#     return lst[0] == lst[-1]

# print(check(numbers_x))


# list1 = [10, 20, 33, 46, 55]
# print("Divisible by 5")
# for i in list1:
#     if i%5==0:
#         print(i)

# str_x = "Emma is good developer. Emma is a writer"

# print("Emma appeared",str_x.count("Emma"), "times")

# def count_emma(stat):
#     print("given string", stat)
#     count=0
#     for i in range(len(stat) - 1):
#         count += stat[i: i+4] == "Emma"
#     return count

# count = count_emma("Emma us good developer, emma us es")
# print("eMMA Appperared" , count , "times")

# a = 5
# b = 10

# print(f"Before swap: a = {a}, b = {b}")

# a , b = b ,a
# print(f"after swap: a = {a}, b = {b}")



# num = 5
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i

# print(f"The factorial of {num} is {fact}")


# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits.append('fig')
# fruits.pop(1)

# print(fruits)

# S = "Python"
# G= S[::-1]
# print(f"original : {S}")
# print(f"Reversed : {G}")


# New = "STRING"
# new1 = New[::-1]
# print(new1)

# sentence = "Learning Python is fun!"
# vowels = "aeiou"
# count = 0

# for i in sentence.lower():
#     if i in vowels:
#         count += 1

# print(f"Number of vowels : {count}")



# for i in sentence.upper():
#     if i in vowels:
#         count +=1

# print(f"the number of upper case vowels{count}")

# nums = [45, 2, 89, 12, 7]
# largest = max(nums)
# smallest = min(nums)

# print(f"largest : {largest}")

# data = [1, 2, 2, 3, 4, 4, 4, 5]
# new_data = list(set(data))
# print(new_data)

# numbers_x = [75, 65, 35, 75, 30]

# numbers_x_new_f = numbers_x[0]
# numbers_x_new_L = numbers_x[-1]

# if numbers_x_new_f == numbers_x_new_L:
#     print(True)
# else:
#     print(False)

# num_list = [10, 20, 33, 46, 55]

# for i in num_list:
#     if i%5==0:
#         print(i)

# str_x = "Emma is good developer. Emma is a writer"

# count = str_x.count("Emma")
# print(f"Emma appeared {count} times")

# for num in range(1 , 6):
#     for i in range(num):
#         print(num , end = " ")

#     print("\n")

#     # Outer loop for rows
# for num in range(1, 6):
#     # Inner loop for repetition
#     for i in range(num):
#         print(num, end=" ") # end=" " keeps it on the same line
#     # New line after each row
#     print("\n")

# number1 = 121
# number2= 125

# new_num1 =str(number1)
# new_num2 =str(number2)

# s1 = new_num1[::-1]
# s2= new_num1[::1]

# s3 = new_num2[::-1]
# s4 = new_num2[::1]

# if s1==s2:
#     print("This is palendrome")
# else:
#     print("This is no palindrome")


# def check_palindrome(number):
#     print("Original number" , number)

#     original_str = str(number)
#     reversed_str = original_str[::-1]

#     if original_str == reversed_str:
#         print("This is palindrome")
#     else:
#         print("This is not palindrome")

# check_palindrome(121)
# check_palindrome(125)



# list3 = []

# def merge_list(list1,list2):
#     result_list = []
    
#     for i in list1:
#         if i % 2!= 0:
#             result_list.append(i)

#     for i in list2:
#         if i % 2 == 0:
#             result_list.append(i)

#     return result_list


# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# print("result list: " , merge_list(list1 , list2))


# def merge_list(list1,list2):
#     result_list = []

#     for i in list1:
#         if i % 2 !=0:
#             result_list.append(i)

#     for i in list2:
#         if i % 2 == 0:
#             result_list.append(i)
        
#     return result_list



# list1 = [20,33,43,23,20,10]
# list2 =  [20,33,43,23,20,10]

# print("result list", merge_list(list1, list2))

# number = 7536
# print("Given number", number)

# while number>0:
#     digit = number % 10

#     number = number // 10

#     print(digit ,  end= " ")

# while number > 0:
#     # Get the last digit
#     digit = number % 10
    
#     # Remove the last digit from number
#     number = number // 10

# income = 45000
# tax_payable = 0
# print("Given income:" , income)

# if income <= 10000:
#     tax_payable = 0
# elif income <=20000:
#     tax_payable = (income-10000) * 10/100
# else:
#     tax_payable = 0 + (10000 * 10/100)
#     tax_payable += (income- 20000) * 20/100

# print("Total income tax to pay is", tax_payable)

# Nested Loops for Multiplication
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print("\n")

# Downward Half-Pyramid Pattern
# for i in range(5,0,-1):
#     for j in range(0,i):
#         print("*", end= " ")
#     print("\n")


# def exponent(base, exp):
#     num = exp
#     result = 1
#     # Repeat multiplication 'exp' times
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is:", result)

# exponent(2, 5)
# exponent(5, 4)

# def check_palindrome(number):
#     print("Original number" , number)

#     original_str = str(number)
#     reversed_str = original_str[::-1]

#     if original_str == reversed_str:
#         print("This is palindrome")
#     else:
#         print("This is not palindrome")

# check_palindrome(121)
# check_palindrome(125)


# Terms=15
# num1=0
# num2=1
# for i in range(Terms):
#     print(num1 , end = " ")

#     res = num1+num2

#     num1=num2
#     num2 = res


# def is_leap(year):

#     if (year %4 == 0 and year %100 !=0) or (year % 400 ==0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not leap year ")

# is_leap(2020)

# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}


# merge_dict = dict1 | dict2
# print(merge_dict)

# mer = dict1.update(dict2)
# print(dict1)

# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]

# common_element = set(list_a) & set(list_b)
# print("common element :" ,common_element)

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
Evennumbers = []
oddnumbers = []
for i in numbers:
    if i%2==0:
        Evennumbers.append(i)
    else:
        oddnumbers.append(i)
        

print("Even number",Evennumbers)
print("odd number ", oddnumbers)