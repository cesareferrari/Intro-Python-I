
"""
Comments:
Multiline comments
can be included in three quotes: "
"""

# Single line comment


"""
When in the Python repl, we can type help() to get help on a function
like so:

>>> help(range)

This will print out help on the range() function


To show all the methods available on an object, use dir()

>>> dir("") # empty string
"""


print('Hello world')

name = 'Cesare'
print(name)

# Concatenating the strings
print('Hello', name)

# String interpolation, f-string
# available in Python 3
# Python 2 will give an error
print(f'Using string interpolation: Hello, {name}')



# Lists

list_one = ['a', 'b', 'c']
print(list_one) # ['a', 'b', 'c']

# Can be declared with list() which takes an iterable object, like a string
list_two = list("Hello")
print(list_two)  # ['H', 'e', 'l', 'l', 'o']


# Adding to a list

list_one.append('d')
print(list_one) # ['a', 'b', 'c', 'd']


# Iterating on a list
for letter in list_one:
    print(letter)


# Print out the indexes of a list
for index in range(len(list_one)):
    print(index, list_one[index])

# the range() function returns a list of numbers from 0 to one less of list_one
# length

print('Using `enumerate`') 

for (index, element) in enumerate(list_one):
    print(index,element)


for (index) in enumerate(list_one):
    print(f'index: {index}')

# Looks like enumerate returns a tuple?


# Assigning to a list
list_one[0] = 123

print(list_one)



# List comprehension
# works like map

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]
print(squares)

# add if condition at the end
# works like a filter
evens = [num for num in numbers if num % 2 == 0]
print(evens)


names = ['andrea', 'gwen', 'stephanie', 'yanko', 'bill', 'sadie']

s_names = [name.capitalize() for name in names if name.startswith('s')]
print(s_names)


# Strings are similar to lists

print("hello"[0])
print("hello"[0:3])  # slice from index 0 to index 2
print("hello"[1:])  # slice from index 1 to the end


"""
    you can't assign to an element in a string:
    this following expression gives an error

    "hello"[0] = "z" 

    TypeError: 'str' object does not support item assignment
"""


# Dictionaries

# Key, value

my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)

# assign to a dictionary
# my_dict[key] = value
my_dict["d"] = 4
print(my_dict)

# access a key
print(my_dict["a"])

# reassign a key
my_dict["a"] = 3000
print(my_dict)

# iterating through a dictionary
for key in my_dict:
    print(key)

# Print keys and values:
for key in my_dict:
    print(f'{key} is the key and {my_dict[key]} is the value')

# Older syntax, works with Python 2
print("Using different syntax:")
for key in my_dict:
    print("{} is the key and {} is the value".format(key, my_dict[key]))


# check if a key is in the dictionary (returns True or False):
print("a" in my_dict)



# Tuple, is an immutable list

my_tuple = ('a', 1, 2)
print(my_tuple)


# It's possible to change the value of an element in a dictionary
# inside the tuple.

tuple_two = (1, 2, {"a": 1000, "b": 2000})

tuple_two[2]["a"] = 3000

print(tuple_two)  # prints: (1, 2, {'a': 3000, 'b': 2000})


# 11_args.py

# will accept any number of arguments
def f2(*args):  # args can be called anything
    print(args)  # args is a tuple print(type(args)) # class
    return sum(args)



print(f2(*a))

# The star * will unpack a list

a = [1, 2, 3, 4]
print(*a) # will unpack a list


# default arguments

def f3(x, y=1):
    return x + y


# arbitrary number of keyword arguments
def f4(**kwargs):  # double star ** keywordargs (can be anything)
    for key, value in kwargs.items():
        print(key, value)


f4(**d) # similar to spread operator, destructuring dictionary


"""
single star will work on any number of arguments and convert them
to tuple

double star will convert keyword arguments to dictionary
"""




# Value vs ref

def mult(a):
    for idx in range(len(a)):
        a[idx] *= 2

my_list = [1, 2, 3, 4]

mult(my_list) # mutates list in place
print(my_list)



def rename(a):
    a = None

rename(my_list)
print(my_list)  # unchanged


def mult_one(num):
    num *= 2
    return num

x = 5
mult_one(x) # returns 10
print(x) # original variable is unchanged
