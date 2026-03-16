# '''
# 1. Print all prime numbers between two numbers

# Input: 10, 20
# Output: [11, 13, 17, 19]
# '''
# # CODE Answer 1st method
# start = 10
# end = 20

# for num in range(start, end+1):
#     if num >1:
#         for i in range(2,num):
#             if num % i ==0:
#                 break
#         else:
#             print(num)

# print("code answer 2nd method")

# start = 10
# end = 20

# for num in range(start, end+1):
#     count= 0

#     for i in range(1,num+1):
#         if num% i == 0:
#             count +=1
#     if count ==2:
#             print(num)

# # 2. Pyramid Pattern using *
# #     *
# #    ***
# #   *****
# #  *******
# # *********

# # Code answer
# print("Pyramid Pattern using")

# rows = 5

# for i in range(rows):
#     print(" "* (rows-i-1)+ "*"*(2*i+1))


# for i in range(rows):
#     print(" "*(rows-i-1),end="")
#     print("*"*(2*i+1))

# # 3. Merge Two Dictionaries
# # Input

# # {'a':1}, {'b':2}

# # Output

# # {'a':1, 'b':2}
# print("Merge Two Dictionaries")

# dict1 = {'a':1}
# dict2  = {'b':2}

# result = {**dict1, **dict2}
# print(result)

# dict3 = dict1 | dict2
# print(dict3)

# # 4. Count Uppercase and Lowercase Letters
# # Input

# # "Hello World"

# # Output

# # {'upper': 2, 'lower': 8}
# print("Count Uppercase and Lowercase Letters")

# text = "Hello World"

# lower = 0
# upper = 0

# for ch  in text:
#     if ch.isupper():
#         upper += 1
#     if ch.islower():
#         lower +=1

# print({'upper': upper, 'lower':lower})

# #5. Extract All Numbers From a String

# # Input

# # abc123xyz45

# # Output

# # [123, 45]

# print("Extract All Numbers From a String")

# text = "abc123xyz45"

# numbers = []
# current_num = ""

# for ch in text:
#     if ch.isdigit():
#         current_num = current_num +ch
#     else:
#         if current_num != "":
#             numbers.append(int(current_num))
#             current_num = ""
# if current_num != "":
#     numbers.append(int(current_num))

# print(numbers)


# # 1

# # Write a Python program to find factorial of a number

# # Example
# # Input: 5
# # Output: 120

# input = "Data Science"

# vowel = "aeiou"
# count_vowel = 0

# for ch in input.lower():
#     if ch in vowel:
#         count_vowel +=1
# print(count_vowel)


# _list = [10, 45, 23, 67, 12]

# max_num = _list[0]

# for num in _list:
#     if num>max_num:
#         max_num = num

# print(max_num)

# s = "swiss"

# for c in s:
#     if s.count(c)==1:
#         print(c)
#         break

# count = {}

# for c in s:
#     if c in count:
#         count[c] +=1
#     else:
#         count[c] = 1

# for c in s:
#     if count[c]==1:
#         print(c)
#         break

# s1 = "listen"
# s2 = "silent"

# if sorted(s1)==sorted(s2):
#     print("Anagram")
# else:
#     print("Not anagram")

# _list = [1,2,2,3,1]

# result = []

# for i in _list:
#     if i not in result:
#         result.append(i)

# print(result)


# a = 12
# b = 15

# gcd = 1

# for i in range(1,min(a,b)+ 1):
#     if a% i ==0 and b% i ==0:
#         gcd = i

# lcm = (a*b)//gcd
# print("GCD",gcd)
# print("lcm",lcm)

# matrix = [[1,2,3],
#  [4,5,6]]

# # print(list((zip(*matrix))))

# rows= len(matrix)
# cols = len(matrix[0])

# trnaspose = []

# for i in range(cols):
#     new_row = []
#     for j in range(rows):
#         new_row.append(matrix[j][i])
#     trnaspose.append(new_row)

# print(trnaspose)

# A = [[1,2],
#      [3,4]]

# B = [[5,6],
#      [7,8]]


# result = [[0,0],[0,0]]

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             result[i][j] += A[i][k] * B[k][j]
        
# print(result)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


n = len(matrix)

for i in range(n):
    for j in range(i,n):
        matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()
    
print(matrix)