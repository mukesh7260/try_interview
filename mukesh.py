l = lambda : [i for i in range(10) if i % 2 == 0] 
print(l()) 

l = lambda a , b : a * b
print(l(2,3))


l = lambda : print('hello') 
print(l()) 


# Syntax of a lambda function:
# lambda arguments: expression
# example of lambda function  
# No arguments: 

l = lambda : [i for i in range(10) if i % 2 == 0]
print(l())  # ➜ [0, 2, 4, 6, 8]

# With arguments: 

l = lambda a, b: a * b # here a , b is the argument of lamda function 
print(l(2, 3))  # ➜ 6

# ❗ Why : is required
# Because Python's lambda is an expression, not a block like a normal function, you need a clear delimiter between:
# Arguments: what goes into the lambda
# Expression body: the single expression that gets evaluated and returned
# The : does that.


# ✅ With no arguments:
say_hello = lambda: "Hello"
print(say_hello())  # ➜ Hello

# ✅ With one argument: 

square = lambda x: x ** 2
print(square(4))  # ➜ 16 

# ✅ With a conditional expression:/

max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # ➜ 20 

# ✅ When to Use Lambda
# When you need a small, throwaway function
# When passing a function as an argument (e.g. sorted, map, filter)
# For one-liners 
# ❌ When not to use lambda:
# When the function logic is complex
# When you need multiple lines
# When readability matters more



# 1. map() + lambda
# 🔹 Purpose: Apply a function to each item in a list.

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares) 

# ✅ 2. filter() + lambda
# 🔹 Purpose: Filter a list based on a condition. 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens) 


# ✅ 3. sorted() + lambda
# 🔹 Purpose: Sort a list of items by a custom key. 

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)


# output : - 

[
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Charlie', 'age': 35}
] 


# ✅ Bonus: lambda in reduce() (needs functools)
# 🔹 Purpose: Reduce a list to a single value


from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)