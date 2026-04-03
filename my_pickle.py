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

class employee:
    def __init__(self,emp_name):
        self.emp_name = emp_name

emp_1 = employee("rvn")
print(emp_1.emp_name)

class employee:
    def __init__(self,emp_name):
        self.emp_name = emp_name
    
    def introduce(self):
        print(f"Hello, I am {self.emp_name}")