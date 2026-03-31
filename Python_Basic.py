# # num1 = 20
# # num2 = 30

# # def multi(a,b):
# #     multiply=a*b
# #     if multiply <= 1000:
# #         return multiply
# #     else:
# #         return a+b
    
# # result = multi(num1,num2)
# # print("the result is" ,result)

# # result = multi(40,30)
# # print("The result is" , result)

# # print("Printing current and previous number and their sum in a range(10)")
# # previous_num =0
# # # for i in range(1,11):
# # #     x_sum = previous_num + 1
# # #     print("current number", i , "previous number", previous_num,"sum:", x_sum)
# # #     previous_num=1

# # for i in range(11):
# #     x_sum = previous_num + i
# #     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
# #     # modify previous number
# #     # set it to the current number
# #     previous_num = i


# # str = "PYnative"
# # S =(str[0:8:2])
# # for i in S:
# #     print(i)


# # # accept input string from a user
# # word = input('Enter word ')
# # print("Original String:", word)

# # # get the length of a string
# # size = print(len(word))

# # # iterate a each character of a string
# # # start: 0 to start with first character
# # # stop: size-1 because index starts with 0
# # # step: 2 to get the characters present at even index like 0, 2, 4
# # print("Printing only even index chars")
# # for i in range(0, size - 1, 2):
# #     print("index[", i, "]", word[i])

# # word = input("Enter word")
# # print("original str", word)

# # x = list(word)
# # for i in x[0::2]:
# #     print(i)

# # str = "Pynative"
# # u = str.replace("P","n")
# # print(u)


# # numbers_x = [10, 20, 30, 40, 90]

# # x=(numbers_x[0])
# # y=(numbers_x[-1:])

# # def check(x,y):
# #     if x==y:
# #         return True
# #     else:
# #         return False

# # print(check(x,y))

# # def check(lst):
# #     return lst[0] == lst[-1]

# # print(check(numbers_x))


# # list1 = [10, 20, 33, 46, 55]
# # print("Divisible by 5")
# # for i in list1:
# #     if i%5==0:
# #         print(i)

# # str_x = "Emma is good developer. Emma is a writer"

# # print("Emma appeared",str_x.count("Emma"), "times")

# # def count_emma(stat):
# #     print("given string", stat)
# #     count=0
# #     for i in range(len(stat) - 1):
# #         count += stat[i: i+4] == "Emma"
# #     return count

# # count = count_emma("Emma us good developer, emma us es")
# # print("eMMA Appperared" , count , "times")

# # a = 5
# # b = 10

# # print(f"Before swap: a = {a}, b = {b}")

# # a , b = b ,a
# # print(f"after swap: a = {a}, b = {b}")



# # num = 5
# # fact = 1
# # for i in range(1, num+1):
# #     fact = fact * i

# # print(f"The factorial of {num} is {fact}")


# # fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# # fruits.append('fig')
# # fruits.pop(1)

# # print(fruits)

# # S = "Python"
# # G= S[::-1]
# # print(f"original : {S}")
# # print(f"Reversed : {G}")


# # New = "STRING"
# # new1 = New[::-1]
# # print(new1)

# # sentence = "Learning Python is fun!"
# # vowels = "aeiou"
# # count = 0

# # for i in sentence.lower():
# #     if i in vowels:
# #         count += 1

# # print(f"Number of vowels : {count}")



# # for i in sentence.upper():
# #     if i in vowels:
# #         count +=1

# # print(f"the number of upper case vowels{count}")

# # nums = [45, 2, 89, 12, 7]
# # largest = max(nums)
# # smallest = min(nums)

# # print(f"largest : {largest}")

# # data = [1, 2, 2, 3, 4, 4, 4, 5]
# # new_data = list(set(data))
# # print(new_data)

# # numbers_x = [75, 65, 35, 75, 30]

# # numbers_x_new_f = numbers_x[0]
# # numbers_x_new_L = numbers_x[-1]

# # if numbers_x_new_f == numbers_x_new_L:
# #     print(True)
# # else:
# #     print(False)

# # num_list = [10, 20, 33, 46, 55]

# # for i in num_list:
# #     if i%5==0:
# #         print(i)

# # str_x = "Emma is good developer. Emma is a writer"

# # count = str_x.count("Emma")
# # print(f"Emma appeared {count} times")

# # for num in range(1 , 6):
# #     for i in range(num):
# #         print(num , end = " ")

# #     print("\n")

# #     # Outer loop for rows
# # for num in range(1, 6):
# #     # Inner loop for repetition
# #     for i in range(num):
# #         print(num, end=" ") # end=" " keeps it on the same line
# #     # New line after each row
# #     print("\n")

# # number1 = 121
# # number2= 125

# # new_num1 =str(number1)
# # new_num2 =str(number2)

# # s1 = new_num1[::-1]
# # s2= new_num1[::1]

# # s3 = new_num2[::-1]
# # s4 = new_num2[::1]

# # if s1==s2:
# #     print("This is palendrome")
# # else:
# #     print("This is no palindrome")


# # def check_palindrome(number):
# #     print("Original number" , number)

# #     original_str = str(number)
# #     reversed_str = original_str[::-1]

# #     if original_str == reversed_str:
# #         print("This is palindrome")
# #     else:
# #         print("This is not palindrome")

# # check_palindrome(121)
# # check_palindrome(125)



# # list3 = []

# # def merge_list(list1,list2):
# #     result_list = []
    
# #     for i in list1:
# #         if i % 2!= 0:
# #             result_list.append(i)

# #     for i in list2:
# #         if i % 2 == 0:
# #             result_list.append(i)

# #     return result_list


# # list1 = [10, 20, 25, 30, 35]
# # list2 = [40, 45, 60, 75, 90]

# # print("result list: " , merge_list(list1 , list2))


# # def merge_list(list1,list2):
# #     result_list = []

# #     for i in list1:
# #         if i % 2 !=0:
# #             result_list.append(i)

# #     for i in list2:
# #         if i % 2 == 0:
# #             result_list.append(i)
        
# #     return result_list



# # list1 = [20,33,43,23,20,10]
# # list2 =  [20,33,43,23,20,10]

# # print("result list", merge_list(list1, list2))

# # number = 7536
# # print("Given number", number)

# # while number>0:
# #     digit = number % 10

# #     number = number // 10

# #     print(digit ,  end= " ")

# # while number > 0:
# #     # Get the last digit
# #     digit = number % 10
    
# #     # Remove the last digit from number
# #     number = number // 10

# # income = 45000
# # tax_payable = 0
# # print("Given income:" , income)

# # if income <= 10000:
# #     tax_payable = 0
# # elif income <=20000:
# #     tax_payable = (income-10000) * 10/100
# # else:
# #     tax_payable = 0 + (10000 * 10/100)
# #     tax_payable += (income- 20000) * 20/100

# # print("Total income tax to pay is", tax_payable)

# # Nested Loops for Multiplication
# # for i in range(1,11):
# #     for j in range(1,11):
# #         print(i*j, end="\t")
# #     print("\n")

# # Downward Half-Pyramid Pattern
# # for i in range(5,0,-1):
# #     for j in range(0,i):
# #         print("*", end= " ")
# #     print("\n")


# # def exponent(base, exp):
# #     num = exp
# #     result = 1
# #     # Repeat multiplication 'exp' times
# #     while num > 0:
# #         result = result * base
# #         num = num - 1
# #     print(base, "raises to the power of", exp, "is:", result)

# # exponent(2, 5)
# # exponent(5, 4)

# # def check_palindrome(number):
# #     print("Original number" , number)

# #     original_str = str(number)
# #     reversed_str = original_str[::-1]

# #     if original_str == reversed_str:
# #         print("This is palindrome")
# #     else:
# #         print("This is not palindrome")

# # check_palindrome(121)
# # check_palindrome(125)


# # Terms=15
# # num1=0
# # num2=1
# # for i in range(Terms):
# #     print(num1 , end = " ")

# #     res = num1+num2

# #     num1=num2
# #     num2 = res


# # def is_leap(year):

# #     if (year %4 == 0 and year %100 !=0) or (year % 400 ==0):
# #         print(f"{year} is a leap year")
# #     else:
# #         print(f"{year} is not leap year ")

# # is_leap(2020)

# # dict1 = {"name": "Alice", "age": 25}
# # dict2 = {"city": "New York", "job": "Engineer"}


# # merge_dict = dict1 | dict2
# # print(merge_dict)

# # mer = dict1.update(dict2)
# # print(dict1)

# # list_a = [1, 2, 3, 4, 5]
# # list_b = [4, 5, 6, 7, 8]

# # common_element = set(list_a) & set(list_b)
# # print("common element :" ,common_element)

# # numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
# # Evennumbers = []
# # oddnumbers = []
# # for i in numbers:
# #     if i%2==0:
# #         Evennumbers.append(i)
# #     else:
# #         oddnumbers.append(i)
        

# # print("Even number",Evennumbers)
# # print("odd number ", oddnumbers)

# # words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# # for i in words:
# #     print(i ,len(i))

# # from collections import Counter
# # import re
# # text = "apple banana apple cherry banana apple"


# # words = re.findall(r'\b\w+\b', text.lower())
# # word_counts = Counter(words)
# # print(word_counts)

# # text = "apple banana apple cherry banana apple"

# # words = text.split()
# # print(words)
# # frequency = {}

# # for word in words:
# #     if word in frequency:
# #         frequency[word] +=1
# #     else:
# #         frequency[word] = 1

# # print(frequency)

# # Print Alternate Prime Numbers

# # for num in range(20,2):
# #     is_prime = True

# #     for i in range(2, int(num**0.5)+ 1):
# #         if num%i == 0:
# #             is_prime = False
# #             break
    
# #     if is_prime:
# #         print(f"{num} is a prime number")
# #     else:
# #         print(f"{num} is not prime")


# # prime = []

# # for num in range(2,21):
# #     for i in range(2, int(num**0.5) + 1):
# #         if num % i == 0:
# #             break
# #     else:
# #         prime.append(num)

# # alt_prime = prime[::2]
# # print(alt_prime)


# # primes = []

# # for num in range(2, 21):
# #     # Check if number is prime
# #     for i in range(2, int(num**0.5) + 1):
# #         if num % i == 0:
# #             break
# #     else:
# #         primes.append(num)

# # # Print alternate primes
# # alternate_primes = primes[::2]
# # print(alternate_primes)


# # num = 2

# # if num>1:
# #     for i in range(2,int(num**5) + 1):
# #         if (num%i) == 0:
# #             print(f"{num} is not a prime number")
# #             break
# #     else:
# #         print(f"{num} is a prime number")
# # else:
# #     print(f"{num} is not a prime number")


# # num = 5

# # # Primes must be greater than 1
# # if num > 1:
# #     # Use the optimized range we discussed
# #     for i in range(2, int(num**0.5) + 1):
# #         if (num % i) == 0:
# #             print(f"{num} is not a prime number.")
# #             break
# #     else:
# #         # This runs if the 'for' loop finished without finding a divisor
# #         print(f"{num} is a prime number.")
# # else:
# #     print(f"{num} is not a prime number.")

# # square = {}
# # for i in range(1,11):
# #     square[i] = i*i

# # print(square)

# # Character Replacer (Data Sanitization)

# # input = "I love coding in Python"
# # s =input.replace(" ", "_")
# # print(s)

# # Rows = 5

# # for i in Rows:
# #     for s in range(i-1)

# # n=5
# # for i in range(1 , n+1):
# #     print("*" * i)

# # n = 3
# # for i in range(1,n+1):
# #     print("*" * i)

# # n = 5
# # for i in range(1,n+1):
# #     print(" " * (n-1) + "*" * (2* i-1))

# # n = 3
# # for i in range(1,n+1):
# #     print(" " * (n-1) + "*" * (2*i - 1))

# # n = 4
# # num = 1

# # for i in range(1,n+1):
# #     for j in range(i):
# #         print(num , end = " ")
# #         num += 1
# #     print()

# # n = 3
# # num = 9

# # for i in range(1, n+1):
# #     for j in range(i):
# #         print(num , end = " ")
# #         num += 1
# #     print()

# # rows = 5

# # for i in range(5,0,-1):
# #     for j in range(i,0,-1):
# #         print(j, end = " ")
# #         # rows +=1
# #     print()


# # input = "Python"
# # contain_digit = False


# # for i in input:
# #     if i.isdigit():
# #         contain_digit = True
# #         break

# # print(f"The string {input} contain digit: {contain_digit}")


# # text = "hello world from python"

# # s =text.split()
# # empty_list = []

# # for i in s:
# #     empty_list.append(i.capitalize())

# # result = " ".join(empty_list)
# # print(result)

# # import time

# # num = 5
# # while num >0:
# #     print(num)
# #     time.sleep(1)
# #     num -=1

# # print("Blast off!")


# # import time

# # count = 5

# # while count >0:
# #      print(count)
# #      time.sleep(2)
# #      count -=1

# # print("ho gya")

# #    Fixed Code
# # try:
# #     with open('sample.txt', 'r',encoding= 'utf-8') as f:
# #         for line in f:
# #             print("The file contain",len(line.split()), "words")
# # except:
# #     print("Eroor: The file'sample.txt was not found")
        
    


# # try:
# #     with open("sample.txt", "r",encoding='utf-8') as file:
# #         data = file.read()
# #         words = data.split()
# #         word_count = len(words)
# #         print(f"The file contains {word_count} words.")
# # except FileNotFoundError:
# #     print("Error: The file 'sample.txt' was not found.")

# # class Car:
# #   def __init__(self, brand, model, year):
# #     self.brand = brand
# #     self.model = model
# #     self.year = year

# #   def display_info(self):
# #     print(f"{self.year} {self.brand} {self.model}")

# # car1 = Car("Toyota", "Corolla", 2020)
# # car1.display_info()

# # class car:
# #    def __init__(self,make,model,year):
# #       self.make = make
# #       self.model = model
# #       self.year = year

# #    def display_info(self):
# #       print(f"The {self.year} {self.make} {self.model}'s engine is now running!")
    
# # Car1 = car("Toyota","Camry",2022)
# # Car1.display_info()
      
# try:
#     # --- Math and Logic Functions ---
#     num1 = 20
#     num2 = 30

#     def multi(a, b):
#         multiply = a * b
#         return multiply if multiply <= 1000 else a + b
    
#     print("Result 1:", multi(num1, num2))
#     print("Result 2:", multi(40, 30))

#     # --- Range and Sum ---
#     print("\nPrinting current/previous sums:")
#     previous_num = 0
#     for i in range(11):
#         x_sum = previous_num + i
#         print(f"Current: {i}, Previous: {previous_num}, Sum: {x_sum}")
#         previous_num = i

#     # --- String Indexing ---
#     word_str = "PYnative"
#     print("\nEven index chars in PYnative:", word_str[0:8:2])

#     # --- User Input Section (Prone to errors) ---
#     word = input('\nEnter word for indexing: ')
#     size = len(word)
#     print("Even index chars:")
#     for i in range(0, size, 2): # Fixed range logic
#         print(f"index[{i}] {word[i]}")

#     # --- List Comparisons ---
#     numbers_x = [10, 20, 30, 40, 90]
#     def check_first_last(lst):
#         return lst[0] == lst[-1]
#     print("\nFirst and last equal?", check_first_last(numbers_x))

#     # --- String Operations (Count/Replace) ---
#     str_x = "Emma is good developer. Emma is a writer"
#     print(f"Emma appeared {str_x.count('Emma')} times")
#     print("Replace P with n:", "Pynative".replace("P", "n"))

#     # --- Factorial ---
#     num = 5
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(f"Factorial of {num}: {fact}")

#     # --- Palindrome Check ---
#     def check_palindrome(number):
#         original = str(number)
#         if original == original[::-1]:
#             print(f"{number} is a palindrome")
#         else:
#             print(f"{number} is not a palindrome")
    
#     check_palindrome(121)

#     # --- Income Tax ---
#     income = 45000
#     tax = 0
#     if income <= 10000:
#         tax = 0
#     elif income <= 20000:
#         tax = (income - 10000) * 0.1
#     else:
#         tax = (10000 * 0.1) + (income - 20000) * 0.2
#     print(f"Tax for {income}: {tax}")

#     # --- Prime Number List ---
#     primes = []
#     for num in range(2, 21):
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             primes.append(num)
#     print("Primes up to 20:", primes)

# except EOFError:
#     print("\nError: No input received.")
# except ValueError as ve:
#     print(f"\nValue Error: {ve}")
# except TypeError as te:
#     print(f"\nType Error: {te}")
# except Exception as e:
#     print(f"\nAn unexpected error occurred: {e}")
# finally:
#     print("\nExecution complete.")

# new_list = [expression for item in iterable if condition]


# words = ["apple", "bat", "cherry", "dog", "elderberry"]


# fw =[i.upper() for i in words if len(i)>4]
# print(fw)

# words = ["apple", "bat", "cherry", "dog", "elderberry"]

# c = [i.upper() for i in words if len(i)>4]
# print(c)

# d1 = {'a': 10, 'b': 20} 
# d2 = {'b': 5, 'c': 15}

# dict_c = dict_a | dict_b
# print(dict_c)

# dict_c = dict_a.update(dict_b)
# print(dict_c)

# dict_3 = {**dict_a , **dict_b}
# print(dict_3)



# d3 = d1.copy()
# for key, value in d2.items():
#     d3[key] = d3.get(key,0) +value

# print(d3)


# # from collections import Counter
import re
# # text = "apple banana apple cherry banana apple"


# # words = re.findall(r'\b\w+\b', text.lower())
# # word_counts = Counter(words)
# # print(word_counts)

text = "Python Programming"
from collections import Counter

# words = re.findall(r'\b\w+\b', text.lower())

# word_count = Counter(words)
# m = word_count.replace(" ","")
# for i in m:
#     print(i)

# def get_frequency(input_string):
#     clean_text = input_string.lower().replace(" ","")
#     return Counter(clean_text)

# freq = get_frequency(text)
# print(freq)

# word1 = "listen", word2 = "silent"

# def Anagram_checker(word1,word2):
#     for i in word1:
#         for j in word2:
#             if i == j:
#                 print("yes word1 is anagram of word2")
#             else:
#                 print("Word1 is not anagram of word2 ")

# Anagram_checker("listen","silent")

# def Anagram_checker(word1,word2):
#     if sorted(word1) == sorted(word2):
#         print("Yes , they are anagrams")
#     else:
#         print("No, they are not anagrams")

# Anagram_checker("listen","silent")


# def is_anagram(word1, word2):
#     return Counter(word1) == Counter(word2)
        


# s =is_anagram("silent", "listen")
# print(s)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * (factorial(n-1))

# print(factorial(5))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))

# def fibonacci(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(10))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))



# def Flatten(list):

# flattedn = [item for sublist in nested_list for item in sublist]
# print(flattedn)
    
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flattened_list = [item for sublist in nested_list for item in sublist]
# print(flattened_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# import itertools
# flattened_list = list(itertools.chain.from_iterable(nested_list))
# print(flattened_list)

# def flatten_list(nested_list):
#     flattened = []
#     for item in nested_list:
#         if isinstance(item,list):
#             flattened.extend(flatten_list(item))
#         else:
#             flattened.append(item)
#     return flattened

# d_nested_list = [1, [2, 3], [4, [5, 6]], 7]
# f_l = flatten_list(d_nested_list)
# print(f_l)


# string = "Python is awesome"
# # s = string.split()
# # for i in s:
# #     print(i[::-1])

# def reverse(sentance):
#     words = sentance.split()

#     reverse_words = [i[::-1]for i in words]
#     return " ".join(reverse_words)

# print(reverse(string))

# string = "A man, a plan, a canal: Panama"

# # s =string.isalnum()
# # print(s)

# def is_palindrome(sentance):
#     clean_chars = [i.lower() for i in sentance if i.isalnum()]

#     clean_str = "".join(clean_chars)

#     return clean_str == clean_str[::-1]

# print(is_palindrome(string))

# string_list = ["apple", "education", "ice", "ocean", "python", "umbrella"]

# u = [ i for i in string_list if len(i)>5 and i[0].lower() in 'aeiou']
# print(u)



# def remove_duplicate(items):
#     seen = set()
#     result = []

#     for x in items:
#         if x not in seen:
#             result.append(x)
#             seen.add(x)

#     return result

# list = [1, 2, 2, 3, 1, 4, 2]
# print(remove_duplicate(list))\

# def remove_duplicate(items):
#     seen = set()
#     result = []

#     for x in items:
#         if x not in seen:
#             result.append(x)
#             seen.add(x)
#     return result

# list = [1, 2, 2, 3, 1, 4, 2]
# print(remove_duplicate(list))

# Exercise 10: Circular Shift (Rotation)
# List = [1, 2, 3, 4, 5] 
# Shift=  2
# Direction = 'right' 
# def rotate_list(lst,n,direction='right'):
#     if not lst:
#         return lst
    
#     n = n % len(lst)

#     if direction == 'right':
#         return lst[-n:] + lst[:-n]
#     else:
#         return lst[n:] + lst[:n]
    
# data = [1, 2, 3, 4, 5]
# print(f"Right Shift 2: {rotate_list(data, 2, 'right')}")
# print(f"Left Shift 1:  {rotate_list(data, 1, 'left')}")

# from collections import deque

# def rotate_list_deque(lst,n, direction = 'list'):
#     d = deque(lst)

#     if direction == 'left':
#         d.rotate(-n)
#     else:
#         d.rotate(n)

#     return list(d)

# data = [1, 2, 3, 4, 5]
# print(f"Right Shift 2: {rotate_list_deque (data, 2, 'right')}")
# print(f"Left Shift 1:  {rotate_list_deque(data, 1, 'left')}")


# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# # d3 =d1.update(d2)
# # print(d3)

# def merge_and_group(dict1, dict2):
#     combined = {}

#     all_keys = set(dict1.keys()) | set(dict2.keys())

#     for key in all_keys:
#         values = []
#         if key in dict1:
#             values.append(dict1[key])
#         if key in dict2:
#             values.append(dict2[key])
#         combined[key] = values

#     return combined

# print(merge_and_group(d1,d2))



# d3= d1.keys()|d2.keys()
# print(d3)

# def merge_combine(dict1,dict2):
#     combined = {}

#     all_keys = set(dict1.keys()|dict2.dict2.keys)

#     for key in all_keys:
#         value = []

#         if key in dict1:
#             value.append(dict1[key])
#         if key in dict2:
#             value.append(dict2[key])
#         combined[key]= value

#     return combined




# def merge_combined(dict1,dict2):
#     combined = {}

#     all_keys = set(dict1.key()|dict2.key())
    

#     for key in all_keys:
#         values = []

#         if key in dict1:
#             values.append(dict1[key])
#         if key in dict2:
#             values.append(dict2[key])
#         combined[key]=values
    
#     return combined

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# def merge_combine(dict1,dict2):
#     combined = {}

#     all_keys = set(dict1.(key)|dict2(key))

#     for key in all_keys:
#         values = []

#         for key in dict1:


numbers = [2,4,5,34,54,2]

# min_value = numbers[0]
# max_value = numbers[0]

# for num in numbers:
#     if num <min_value:
#         min_value = num
#     if num > max_value:
#         max_value = num


# print("minimum",min_value)
# print("maximum",max_value)

# min_value = numbers[0]

# for i in numbers:
#     if i > min_value:
#         min_value = i

# print("minimum", min_value)

# rev = []

# for i in range(len(numbers)-1,-1,-1):
#     rev.append(numbers[i])

# print(rev)


# num = [12,3,4,5,6,7]

# rev = []

# for i in range(len(num)-1,-1,-1):
#     rev.append(num[i])

# print(rev)


# total = 0

# for i in num:
#     total = total + i

# print(total)

# count_even = 0
# count_odd = 0

# for i in num:
#     if i%2==0:
#         count_even +=1
#     else:
#         count_odd +=1

# print("even:", count_even)
# print("odd", count_odd)

# a = 10
# b = 20
# c = 8

# largest = a

# if b>largest:
#     largest = b

# if c > largest:
#     largest = c

# print(largest)

# num = 121
# temp = num
# rev = 0

# while num>0:
#     digit = num%10
#     rev = rev * 10 + digit
#     num = num // 10

# if temp == rev:
#     print("Palindorme")
# else:
#     print("Not plaindrome")

# num = 5
# for i in range(1,11):
#     print(i*num)

# s = "Python"
# count = 0

# for char in s:
#     count +=1

# print(count)

# num = 5
# fact =1

# for i in range(1,num+1):
#     fact = fact * 1

# print(fact)

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact  = fact *1

# print(fact)

# import math

# num = 5

# # Method 1: Using math.factorial()
# fact = math.factorial(num)
# print("Factorial:", fact)

# # Method 2: Using recursion
# def factorial_recursive(n):
#     return 1 if n <= 1 else n * factorial_recursive(n - 1)

# print("Factorial (Recursive):", factorial_recursive(num))


# num = 7
# count = 0

# for i in range(1,num+1):
#     if num % 1 == 0:
#         count += 1
#     if count == 2:
#         print("prime")
#     else:
#         print("Not prime")

# num = 12345
# count = 0

# while num>0:
#     num = num//10
#     count +=1

# print(count)

# numbers = [1,23,4,3,3,4,4,3,5,6,7]
# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print(unique)

# text = "python is easy" 
# words = text.split()

# print(len(words))


# text = "programming"

# for char in text:
#     if text.count(char) == 2:
#         print(char)
#         break

# for char in text:
#     if text.count(char)> 1:
#         print(char)

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact *= i

# print(fact)

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact *= i

# print(fact)

# num = 7
# count = 0


# for i in range(1,num+1):
#     if num %i==0:
#         count +=1

# if count == 2:
#     print("Prime number")
# else:
#     print("Not prime")
    
# a = 0
# b = 1

# for i in range(10):
#     print(a)
#     c= a+b
#     a = b
#     b = c


# text = "python"

# count = 0

# for i in text:
#     count += 1

# print(count)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# d3 = {}

# for i in d1:
#     d3[i] = [d1[i]]

# for i in  d2:
#     if i in d3:
#         d3[i].append(d2[i])
#     else:
#         d3[i] = [d2[i]]
# print(d3)

# d3 = {}

# for key in d1:
#     d3[key] = [d1[key]]

# for key in d2:
#     if key in  d3:
#         d3[key].append(d2[key])
#     else:
#         d3[key] = [d2[key]]
# print(d3)

d1 = {'x':10,'y':20}
d2 = {'x':30,'z':40}
d3 = {'y':50,'z':60}

result = {}

# for key in d1:
#     result[key] = [d1[key]]
# for key in d2:
#     if key in result:
#         result[key].append(d2[key])
#     else:
#         result[key] = [d2[key]]
# for key in d3:
#     if key in result:
#         result[key].append(d3[key])
#     else:
#         result[key] = [d3[key]]

# print(result)

# dicts = [d1,d2,d3]
# print(dicts)

# for d in dicts:
#     print(d)
#     for key in d:
#         print(key)
#         if key in result:
#             result[key].append(d[key])
#         else:
#             result[key] = d[key]
# print(result)

# d1 = {'x':10,'y':20}
# d2 = {'x':30,'z':40}
# d3 = {'y':50,'z':60}

# result = {}

# dicts = [d1,d2,d3]
# print(dicts)

# for d in dicts:
#     print(d)
#     for key in d:
#         print(key)
#         if key in result:
#             result[key].append(d[key])
#         else:
#             result[key] = [d[key]]

# print(result)

# d1 = {'a':5,'b':10}
# d2 = {'a':3,'b':2,'c':7}

# result = {}

# for i in d1:
#     result[i] = d1[i]
# for i in d2:
#     if i in result:
#         result[i] = result[i]+d2[i]
#     else:
#         result[i] = d2[i]
# print(result)



# data = [
# {'a':1},
# {'a':2},
# {'b':3},
# {'a':4},
# {'b':5}
# ]

# result = {}

# for i in data:
#     for key in i:
#         if key in result:
#             result[key].append(i[key])
#         else:
#             result[key] = [i[key]]

# print(result)

# d1 = {'a':1,'b':2}
# d2 = {'a':1,'b':3}

# result = {}

# for i in d1:
#     result[i]= [d1[i]]

# for i in d2:
#     if i in result:
#         if d2[i] not in result[i]:
#             result[i].append(d2[i])
#         else:
#             result[i]= [d2[i]]
# print(result)


# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# def merge_and_group(dict1,dict2):
#     combined = {}

#     all_keys = set(dict1.keys()) | set(dict2.keys())

#     for key in all_keys:
#         values = []

#         if key in dict1:
#             values.append(dict1[key])
#         if key in dict2:
#             values.append(dict2[key])
#         combined[key] = values
    
#     return combined

# print(merge_and_group(d1,d2))
    
# data = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

# result = {}

# for author in data:
#     books = data[author]

#     for book in books:
#         result[book] = author
    
# print(result)

# employees = [
# {"name": "A", "salary": 50},
# {"name": "B", "salary": 70},
# {"name": "C", "salary": 60}
# ]

# employees.sort(key=lambda x:x["salary"], reverse= True)

# print(employees)

# Set_A =  {1, 2, 3}
# Set_B = {1, 2, 3, 4, 5}

# s = Set_A.issubset(Set_B)
# print(s)

# if s is True:
#     print("Set A is a subset of Set B")
# else:
#     print("set A is not subset of B")


# list1 = [101, 102, 103]
# list2 = [103, 104, 105]

# set1 = set(list1)
# set2 = set(list2)

# set3 = set1^set2
# print(set3)

# def age_calculator(year,month,date):

# from datetime import date


# # Date of birth
# birth_year = 2000
# birth_month = 5
# birth_day = 15

# birth_date = date(birth_year,birth_month,birth_day)
# print(birth_date)

# today = date.today()
# print(today)

# years = today.year - birth_date.year
# months = today.month - birth_date.month
# days = today.day - birth_date.day

# if days <0:
#     months -= 1
#     days += 30

# if months<0:
#     years -= 1
#     months += 12

# print("Age:",years,"years",months,"months",days,"Days")

# from datetime import date

# year = int(input("Enter birth year: "))
# month = int(input("Enter birth month: "))
# day = int(input("Enter birth day: "))

# birth_date = date(year,month,day)
# today = date.today()

# years = today.year - birth_date.year
# months = today.month - birth_date.month
# days = today.day - birth_date.day

# if days < 0:
#     months -= 1
#     days += 30

# if months < 0:
#     years -= 1
#     months +=12

# print("your age: ")
# print(years , "Years", months , "Months", days , "Days")

# from datetime import date , datetime


# def calculate_age():

#     birth_input = input("Enter your birthdate(yyyy-mm-dd): ")

#     birth_date = datetime.strptime(birth_input , "%Y-%m-%d").date()

#     today = date.today()

#     years = today.year - birth_date.year
#     months = today.month - birth_date.month
#     days = today.day - birth_date.day

#     if days <0:
#         months -= 1
#         days += 30
    
#     if months <0:
#         years -= 1
#         months += 12

    
#     print("Your age:",years,"years",months,"months",days,"days")

# calculate_age()

# from datetime import date, datetime

# def calculate_age():
    
#     birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    
#     birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    
#     today = date.today()
    
#     years = today.year - birth_date.year
#     months = today.month - birth_date.month
#     days = today.day - birth_date.day
    
#     if days < 0:
#         months -= 1
#         days += 30
        
#     if months < 0:
#         years -= 1
#         months += 12
        
#     print("Your Age:", years, "Years", months, "Months", days, "Days")

# calculate_age()

# from datetime import datetime
# from deteutil.relativedelta import relativedelta

# import time

# seconds = 5

# while seconds >0:
#     print(seconds)
#     time.sleep(1)
#     seconds -= 1

# print("Time's up!")

# import time

# time_in_seconds = 10

# while time_in_seconds:
#     mins, secs = divmod(time_in_seconds,60)

#     timer = f"{mins:02d}:{secs:02d}"

#     print(timer, end="\r")

#     time.sleep(1)

#     time_in_seconds -= 1

# print("time's up!")

# import time 

# time_in_seconds = 10

# while time_in_seconds:
#     mins , secs = divmod(time_in_seconds,60)

#     timer = f"{mins:02d}:{secs:02d}"

#     print(timer, end="\r")

#     time.sleep(1)

#     time_in_seconds -= 1

# print("times up!")

# import time

# seconds = int(input("Enter time in seconds: "))

# while seconds:
    
#     hrs = seconds // 3600
#     mins = (seconds % 3600) // 60
#     secs = seconds % 60
    
#     print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
    
#     time.sleep(1)
    
#     seconds -= 1

# print("Time's up!")

# from datetime import datetime

# def new_year_countdown():

#     current_date = datetime(2026,3,12)
#     new_year = datetime(2027,1,1)

#     remaining = new_year - current_date

#     days = remaining.days

#     hours = remaining.seconds // 3600

#     minutes = (remaining.seconds % 3600) // 60

#     print("Days:" , days)
#     print("Hours:" , hours)
#     print("Minutes:", minutes)

# new_year_countdown()

from datetime import datetime , timedelta

# def new_year_countdown():

#     now = datetime.now()

#     next_year = now.year + 1

#     new_year = datetime(next_year,1,1)

#     remaining = new_year - now

#     days = remaining.days
#     hours = remaining.seconds // 3600
#     minutes = (remaining.seconds%3600) // 60
#     seconds = remaining.seconds % 60

#     print("Days: ", days)
#     print("Hours: ", hours)
#     print("Minutes: ", minutes)
#     print("seconds: ", seconds)

# new_year_countdown()

# start = datetime(2026,1,1)
# end = datetime(2026,1,10)

# business_days = 0

# current = start

# while current <= end:
#     if current.weekday()<5:
#         business_days +=1
    
#     current += timedelta(days=1)

# print("Business days :", business_days)

# name = input("Enter your name: ")
# profession = input("Enter your profession: ")
# interest = input("Enter your interest: ")

# print("\nYour Stylish Bios:\n")

# print("✨", name, "|", profession)
# print("🚀 Passionate about", interest)
# print("💡 Always learning, always growing")

# print("\n---")

# print("🔥", name)
# print("📊", profession)
# print("⚡ Love:", interest)
# print("🌍 Dream Big")

# print("\n---")

# print("👨‍💻", name, "-", profession)
# print("🐍", interest, "enthusiast")
# print("📈 Future Creator")

# name = input("Name: ")
# profession = input("profession: ")
# interest = input("Interest: ")

# bios = [
#     f" ** {name} | {profession}\n {interest} Lover\n Growth Mindeset",
#     f" ** {name}\n {profession}\n Exploring {interest}",
#     f" ** {name}\n {profession}\n passion for {interest}",
#     f" ** {name}\n  Buildig future\n Learning {interest}"
# ]

# print("\nGenerated Bios:\n")

# for bio in bios:
#     print(bio)
#     print("---------")

# class powerofTwo:

#     def __init__(self,max_exponent):
#         self.max_exponent = max_exponent
#         self.current = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):

#         if self.current <= self.max_exponent:
#             result = 2 ** self.current
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
        
# powers = powerofTwo(5)

# for num in powers:
#     print(num)