

# what is higher order fuction
# 1. Take a funtion as argument
# 2. return a function
# 3. Do both

#HOF
# def greet(func):
#   name = func()
#   return "hello " + name


# def get_name():
#   return "Victor"


# print(greet(get_name))

# callinng the function
# Mini calculator
# take a function, and two numbers
# apply the function to the two and return the result

# def add(func, a, b):
#   result = func(a, b)
#   return result

# def operate(num1, num2):
#   return num1 + num2

# print(add(operate, 1, 3))

# FUNCTION THAT RETURNS A FUNCTION
# def outer():
#   def inner():
#     print("this is comming from the inner function")
#   return inner


# inner = outer()
# inner()



# def greet(func):
#   def inner():
#     name = func()
#     print("this is from the inner function")
#     print("this was the result of the function that was passed", name)

#   return inner


# def get_name():
#   return "Natalia"
# inner = greet(get_name)
# inner()




# BUILTING PYTHON HIGER ORDER FUNCTION
# 1. map
# 2. filter



# def square_numbers(nums):
#   squares = []
#   for num in nums:
#     squares.append(num ** 2)
#   return squares

# new_list = square_numbers(nums)
# print(new_list)





# how map works
#square(1)
#square(2)
#square(3)

# Use map() to convert all strings to uppercase
# name = ['Tara', 'Perry', 'Jo', 'Luke']
# print(list(map(uppercase, name)))
# def uppercase(name):
#   return name.upper()

# def square(num):
#   return num ** 2


# nums = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x : x ** 2, nums)))

# name = ['Tara', 'Perry', 'Jo', 'Luke']
# print(list(map(lambda x : x.upper(), name)))



# def even(num):
#   if num % 2 == 0:
#     return True
#   return False

# def even_list_func(nums):
#   even_list = []
#   for num in nums:
#     if even(num):
#       even_list.append(num)
#   return even_list

# print(even_list_func(nums))

# print(list(filter(lambda x : x % 2 == 0, nums)))


# from functools import reduce
# nums = [0, 1, 2, 3, 4, 5, 6]

# def add_two(num1, num2):
#   return num1 + num2

# print(reduce(add_two, nums))


# nums = [1, 2, 3, 4, 5]
# total = reduce(lambda acc, n: acc + n, nums)
# print(total) 


# HOF
# 1. take a function as an argument
# 2. returns a function
# 3. do the both

# closure

# decorator
# def greet(func):
  
#   def lauder():
#     name = func()
#     print("Hello", name.upper())
    
#   return lauder

# def get_name():
#   return "victor"


# func = greet(get_name)
# func()



# inner = modify(add)
# print(inner(1,2))
# from datetime import datetime
# start = datetime.now()

# import time
# def time_taken(func):
#   def wrapper(a, b):
#     start_time = datetime.now()
#     result = func(a, b)
#     end_time = datetime.now()
#     time_taken = end_time - start_time
#     print("time taken is", time_taken)
#     return result
    
#   return wrapper
    


# def power(a, b):
#   return a ** b

# # print(power(2, 3))

# wrapper_inner = time_taken(power)
# #print(wrapper_inner(2, 3))



# def uppercase(func):
#   def wrapper(name):
#     result = func(name).upper()
#     return result
  
#   return wrapper
  
# @uppercase
# def shout(name):
#   return "Hey " + name

# print(shout('Natalia'))

# # inner = uppercase(shout)
# # print(inner('Natalia'))






# def shout(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper


# @shout
# def greet():
#     return "hello"

# print(greet())

# inner = shout(greet)
# print(inner())


# inner = modify(add)
# print(inner(1,2))


# from datetime import datetime

# import time
# def time_taken(func):
#   def wrapper(*args, **kwags):
#     start_time = datetime.now()
#     result = func(*args, **kwags)
#     end_time = datetime.now()
#     time_taken = end_time - start_time
#     print("time taken is", time_taken)
#     return result
    
#   return wrapper

# @time_taken
# def multiply(*args, **kwags):
#   time.sleep(3)
#   num1, num2 = args
#   return num1 * num2
  
# print(multiply(4,5, sum=20))


# def square()
# @time_taken
# def out():
#   time.sleep(2)
#   return 'hello'

# print(out())


# *args

# def variable_arg(*args, **kwargs):
#   num1, num2 = args
#   print("num1", num1)
#   print("num2", num2)


# variable_arg(1, 2, age=10)

# payment
# deposite


# bal = 900
# def logger(func):
#   def wrapper(*args, **kwargs):
#     amount, user_name = args
#     print(f"amount: {amount}, user: {user_name} time: {date}")
#   return wrapper


# @logger
# def deposite(amount, user_name):
#   bal = bal + amount

# @logger
# def withdraw(amount, user_nam):
#   bal = bal - amount


# withdraw(500, 'hj')

#Quesition 1
# Write a function called `apply_twice(func, value)` that applies `func` to
#`value` twice. For example, `apply_twice(double, 3)` should return `12`.


# def apply_twice(func, value):
#   value1 = func(value)
#   value2 = func(value1)
#   print(value2)

# def double(num1):
#   return num1 * 2

# apply_twice(double, 4)


# Write a function `get_operation(op_name)` that accepts a string (`'add'`, `'subtract'`, `'multiply'`, `'divide'`) 
# and returns the corresponding math function. Then use it: `op = get_operation('multiply'); print(op(4, 5))`.

# **Expected Output:** `get_operation('add')(3,4) → 7` | `get_operation('multiply')(4,5) → 20`


# def get_operation(op_name):
#   if op_name == 'add':
#     return lambda x, y : x + y
#   elif op_name == 'subtract':
#     return lambda x, y : x - y
#   elif op_name == 'multiply':
#     return lambda x, y : x * y
#   elif op_name == 'divide':
#     return lambda x, y : x / y
#   else:
#     print('Not an operation')

# op = get_operation("add")
# print(op(2, 4))



# Write a function `build_pipeline(*funcs)` that accepts any number of functions and returns a 
# NEW function. The new function should apply all the input functions in sequence to a given value.
# Example: `pipeline = build_pipeline(double, square, str)` then `pipeline(3)` should 
# compute `str(square(double(3))) = '36'`.

# > **Hint:** Use a loop inside the returned function to apply each `func` in order. 
# Look up `*args` syntax if you haven't seen it yet.
# > 

# **Expected Output:** `build_pipeline(double, square, str)(3) → '36'` | `build_pipeline(abs, double)(-5) → 10`


# def build_pipeline(*funcs):
#   def new_function(value):
#     result = value
#     for func in funcs:
#       result = func(result)
#     return result
#   return new_function
  
# double = lambda x : x * 2
# square = lambda x : x ** 2
# to_str = lambda x : str(x)
# triple = lambda x : x * 3


# new_func = build_pipeline(double, square, triple, to_str)
# print(new_func(1))



# Given a list of Celsius temperatures `[0, 15, 22, 37, 100]`, use `map()` to convert them all to Fahrenheit.
# Formula: `F = (C * 9/5) + 32`
# > **Hint:** Pass a lambda or a named function to `map()`.
# **Expected Output:** `[32.0, 59.0, 71.6, 98.6, 212.0]`


# temp = [0, 15, 22, 37, 100]

# temp_f = list(map(lambda c : c * 9/5 + 32, temp))
# # print(temp_f)

# # values_less_than_50 = list(filter(lambda x : x < 50, temp_f))
# # print(values_less_than_50)

# less_than_50 = list(filter(lambda x : x < 50, map(lambda c : c * 9/5 + 32, temp)))
# # map(lambda c : c * 9/5 + 32, temp)

# print(less_than_50)



### 2.2 (Medium) Word Length Filter & Sort

# Given `words = ['python', 'is', 'a', 'beautiful', 'language', 'hi']`, use `filter()` 
# to keep words longer than 3 characters, then use `sorted()` with a key to sort them by length (shortest first).

# > **Hint:** Chain `filter()`— you can wrap one inside the other.
# > 

# **Expected Output:** `['python', 'beautiful', 'language', 'hi'] → ['python', 'language', 'beautiful']`

words = ['python', 'is', 'a', 'beautiful', 'language', 'hi', "adamuuuuu"]

sorted_words = sorted(list(filter(lambda x : len(x) > 3 , words)), key = len)
print(sorted_words)
