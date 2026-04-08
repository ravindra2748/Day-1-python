import pickle

# 1. वह डेटा (Object) जिसे हमें सेव करना है
user_data = {
    "name": "Rahul",
    "age": 25,
    "skills": ["Python", "Data Science"]
}

# --- PICKLING (डेटा को फाइल में सेव करना) ---
# 'wb' का मतलब है Write Binary
with open("data.pkl", "wb") as file:
    pickle.dump(user_data, file)
    print("Data सफलतापूर्वक Pickle कर दिया गया है।")

# --- UNPICKLING (फाइल से डेटा वापस पढ़ना) ---
# 'rb' का मतलब है Read Binary
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print("\nUnpickled डेटा:")
    print(loaded_data)

# जाँच करें कि क्या यह वही Object है
print(f"\nType: {type(loaded_data)}")



# def fib(n):
#    p, q = 0, 1
#    while(p < n):
#        yield p
#        p, q = q, p + q
# x = fib(10)    # create generator object

# x.__next__()    # output => 0
# x.__next__()    # output => 1
# x.__next__()    # output => 1
# x.__next__()    # output => 2
# x.__next__()    # output => 3
# x.__next__()    # output => 5
# x.__next__()    # output => 8
# x.__next__()    # error
 
# for i in fib(10):
#     print(i)


# my_list = [[10,20,30],[40,50,60],[70,80,90]]
# flat = [x for temp in my_list for x in temp]
# print(flat)

# class Arraylist:
#     def __init__(self,number_list):
#         self.numbers = number_list
#     def __iter__(self):
#         self.pos = 0
#         return self
#     def __next__(self):
#         if(self.pos <len(self.numbers)):
#             self.pos +=1
#             return self.numbers[self.pos - 1]
#         else:
#             raise StopIteration
# array_obj = Arraylist([1,2,3])
# it = iter(array_obj)
# print(next(it))
# print(next(it))
# print(next(it))
    

# string = "This is a string"

# string_list = string.split(' ')
# print(string_list)
# print(' '.join(string_list))

# class employee:
#     def __init__(self,emp_name):
#         self.emp_name = emp_name

# emp_1 = employee("rvn")
# print(emp_1.emp_name)

# class employee:
#     def __init__(self,emp_name):
#         self.emp_name = emp_name
    
#     def introduce(self):
#         print(f"Hello, I am {self.emp_name}")

# class parentclass:
#     def par_func(self):
#         print("I am parent class function")

# class childclass(parentclass):
#     def child_func(self):
#         print("i AM CHILD class f")
    
# obj1 = childclass()
# obj1.par_func()
# obj1.child_func()

# a = 5
# b = 10

# temp = a
# a = b
# b = temp

# print(a,b)

# a,b = b,a
# print(a,b)

# a = 10
# b = 25
# c = 15

# if a>b and a >c :
#     print("largest:", a)
# elif b>c:
#     print("largest:",b)
# else:
#     print("largest:",c)

# num = 8
# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")

# n = 6
# a = 0
# b = 1

# for i in range(n):
#     print(a, end = "  ")
#     c = a+b
#     a = b
#     b = c

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i

# print("fsct",fact)

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact = fact *i

# print("factorial", fact)

# num = 1234
# rev = 0

# while num>0:
#     digit = num %10
#     rev = rev* 10 +digit
#     num = num // 10

# print(rev)

# num = 121
# rev = 0
# temp = num

# while num>0:
#     digit = num%10
#     rev = rev*10 +digit
#     num = num //10

# if temp == rev:
#     print("palindrome")
# else:
#     print("Not palindorme")



# num = 12345
# count = 0

# while num>0:
#     num = num // 10
#     count +=1

# print(count)

# num = 12345
# sum = 0

# while num>0:
#     digit = num%10
#     sum +=digit
#     num = num //10

# print(sum)


# num = 153

# temp = num
# sum = 0

# while num>0:
#     digit = num % 10
#     sum += digit**3
#     num = num //10

# if sum == temp :
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# a = 12
# b = 18

# while b!=0:
#     a,b = b, a%b

# print(a)

# a = 12
# b = 18

# temp_a = a
# temp_b = b

# while b!=0:
#     a,b = b,a%b

# gcd = a
# lcm = (temp_a*temp_b)//a
# print(lcm)

print("Hello")