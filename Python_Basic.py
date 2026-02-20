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

# numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
# Evennumbers = []
# oddnumbers = []
# for i in numbers:
#     if i%2==0:
#         Evennumbers.append(i)
#     else:
#         oddnumbers.append(i)
        

# print("Even number",Evennumbers)
# print("odd number ", oddnumbers)

# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# for i in words:
#     print(i ,len(i))

# from collections import Counter
# import re
# text = "apple banana apple cherry banana apple"


# words = re.findall(r'\b\w+\b', text.lower())
# word_counts = Counter(words)
# print(word_counts)

# text = "apple banana apple cherry banana apple"

# words = text.split()
# print(words)
# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] +=1
#     else:
#         frequency[word] = 1

# print(frequency)

# Print Alternate Prime Numbers

# for num in range(20,2):
#     is_prime = True

#     for i in range(2, int(num**0.5)+ 1):
#         if num%i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not prime")


# prime = []

# for num in range(2,21):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         prime.append(num)

# alt_prime = prime[::2]
# print(alt_prime)


# primes = []

# for num in range(2, 21):
#     # Check if number is prime
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)

# # Print alternate primes
# alternate_primes = primes[::2]
# print(alternate_primes)


# num = 2

# if num>1:
#     for i in range(2,int(num**5) + 1):
#         if (num%i) == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


# num = 5

# # Primes must be greater than 1
# if num > 1:
#     # Use the optimized range we discussed
#     for i in range(2, int(num**0.5) + 1):
#         if (num % i) == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         # This runs if the 'for' loop finished without finding a divisor
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# square = {}
# for i in range(1,11):
#     square[i] = i*i

# print(square)

# Character Replacer (Data Sanitization)

# input = "I love coding in Python"
# s =input.replace(" ", "_")
# print(s)

# Rows = 5

# for i in Rows:
#     for s in range(i-1)

# n=5
# for i in range(1 , n+1):
#     print("*" * i)

# n = 3
# for i in range(1,n+1):
#     print("*" * i)

# n = 5
# for i in range(1,n+1):
#     print(" " * (n-1) + "*" * (2* i-1))

# n = 3
# for i in range(1,n+1):
#     print(" " * (n-1) + "*" * (2*i - 1))

# n = 4
# num = 1

# for i in range(1,n+1):
#     for j in range(i):
#         print(num , end = " ")
#         num += 1
#     print()

# n = 3
# num = 9

# for i in range(1, n+1):
#     for j in range(i):
#         print(num , end = " ")
#         num += 1
#     print()

# rows = 5

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end = " ")
#         # rows +=1
#     print()


# input = "Python"
# contain_digit = False


# for i in input:
#     if i.isdigit():
#         contain_digit = True
#         break

# print(f"The string {input} contain digit: {contain_digit}")


# text = "hello world from python"

# s =text.split()
# empty_list = []

# for i in s:
#     empty_list.append(i.capitalize())

# result = " ".join(empty_list)
# print(result)

# import time

# num = 5
# while num >0:
#     print(num)
#     time.sleep(1)
#     num -=1

# print("Blast off!")


# import time

# count = 5

# while count >0:
#      print(count)
#      time.sleep(2)
#      count -=1

# print("ho gya")

   # Fixed Code
# try:
#     with open('sample.txt', 'r',encoding= 'utf-8') as f:
#         for line in f:
#             print("The file contain",len(line.split()), "words")
# except:
#     print("Eroor: The file'sample.txt was not found")
        
    


# try:
#     with open("sample.txt", "r",encoding='utf-8') as file:
#         data = file.read()
#         words = data.split()
#         word_count = len(words)
#         print(f"The file contains {word_count} words.")
# except FileNotFoundError:
#     print("Error: The file 'sample.txt' was not found.")

# class Car:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

#   def display_info(self):
#     print(f"{self.year} {self.brand} {self.model}")

# car1 = Car("Toyota", "Corolla", 2020)
# car1.display_info()

class car:
   def __init__(self,make,model,year):
      self.make = make
      self.model = model
      self.year = year

   def display_info(self):
      print(f"The {self.year} {self.make} {self.model}'s engine is now running!")
    
Car1 = car("Toyota","Camry",2022)
Car1.display_info()
      
      
