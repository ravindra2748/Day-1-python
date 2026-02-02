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


numbers_x = [10, 20, 30, 40, 90]

x=(numbers_x[0])
y=(numbers_x[-1:])

def check(x,y):
    if x==y:
        return True
    else:
        return False

print(check(x,y))

def check(lst):
    return lst[0] == lst[-1]

print(check(numbers_x))


