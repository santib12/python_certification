# Python Certification with FreedCodeCamp

# Examples of common data types:

# Integer
my_integer_var = 10
print('Integer:',my_integer_var)

# Float
my_float_var = 4.50
print('Float:', my_float_var)

# Complex
my_complex_var = 3 + 4j
print('complex:', my_complex_var)

#string
my_string_var = 'hello'
print('string:',my_string_var)

# Bollean
my_boolean_var = True
print('boolean:', my_boolean_var)

# Set
my_set_var = {7, 5, 8}
print('set:', my_set_var)

# Dictionary
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)

# Tuple
my_tuple_var = (7, 5, 8)
print('Tuple;', my_tuple_var)

# Range
my_range_var = range(5)
print(my_range_var)

# List
my_list = [22, 'Hello World', 3.14, True]
print(my_list)

# None
my_none_var = None
print('None:', my_none_var)

# Example of string being immutable
greeting = 'hi '
greeting = 'hello '
print(greeting)

greeting[0] = 'H'

# Example of mutable types, for example list and a disctionary
# Example of updatig an element in a list
nums = [1, 2, 3]
nums[0] = 4

print(nums) # [4, 2, 3]

# To get data_type of variable, use type() function
# Example of type() function
my_var_1 = 'Hello World'
my_var_2 = 21

print(type(my_var_1)) #<class 'str'>
print(type(my_var_2)) #<class 'int'>

# Another way to check the type of a variable is to use the buit-in isinstance() function
# isinstance() takes in an object and the type you want to check it against, then return a boolean
# Example of isinstance()
isinstance('Hello World', str)
isinstance(True, bool)
isinstance(42, int)
isinstance('John Doe', int)

# Although python is dynamically typed, you can still add type hints
# Example of type hints
user_name: str = 'John Doe'
user_age: int = 24

# Example of showing hints for function parameters and a return type:
def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}.'

# Combination of the two:
def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}.'

user_name: str = 'John Doe'
user_age: int = 24

print(greet(user_name, user_age))

# Examples of strings, single quotes '', and "" are treated equally
my_str_1 = 'Hello'
my_str_2 = "World"

# If you need multi-line string, you can use tripple or double quotes or single quotes:
my_str_3 = """Multiline
string"""
my_str_4 = '''Another 
multiline
string''' 

# if your strng contains either single or double quotation marks, thn you have two options
# user the opposite kind of quotes. Thats if your string contains single quotes, use double quotes to wrap the string and vise versa
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Escape the single or double quotation mark in the string with a backslash (\).
# With this method, you can use either single or double quotation marks to wrap the string itself:
msg = 'It\'s a sunny day'
quote = "she said, \"Hello!\""

# You can also combine multiple strings together with the plus (+) operator.
# This process is called string concatenation. Here's how to concatenate two strings with the plus operator:
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)

# But note that this only works with strings. If you try to concatenate a string with a number, you'll get a TypeError:
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age)

# This happens bc python does not automatically convert other data types like int nto stings when you concatenate them
name = 'john Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age)

# You can also use the augemented assigment operator for concatenation. this is represented as a pus and equal sing, +=
name = 'Jogn Doe'
age = 26

name_and_age = name
name_and_age += str(age)

print(name_and_age)

# Python also has a category of string called f-strings, which is short for formatted string literals.
# It allows you to handle interpolation and also do some concatenation with a compact and readable syntax.
# F-strings start with f (either lowercase or uppercase) before the quotes,
# and allow you to embed variables or expressions inside replacement fields indicated by curly braces ({}). Here's an example:
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age)

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}')

# To Get the length of a string, you can use the build-in len() function
# Example:
my_str = "Hello World"
print(len(my_str))

# To acess a character by its index, you use square brackets wth the index of the charcter you want to acess inside
# Example
my_str = "Hello World"
print(my_str[0])
print(my_str[6])

# Negative Indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on

my_str = 'Hello World'
print(my_str[-1])
print(my_str[-2])

# string slicing lets you extract a portion  of a string or work with only a specific part of it
# basic syntax
# string[start:stop]

# if you want to extract charcaters froma certain index to another, you just seperate the start and stop indecies with colon.
my_str = "Hello World"
print(my_str[1:4])
 
# Note that the stop index is non_inclusive

# python list data type is a ordered sequence of elements that can be composed of strings, numbers or even other list 
# Example

cities = ['Los Angeles', 'London', 'Tokyo']
# Accessing elemnts in a list: you can refrence its index number in the sequence 
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0]

# accessing elements using negative indexing you can use -1 as the index number for last element

cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1]

# Creating list using list() constructor, the list() constructor is used to convert an iterable into a list 
developer = 'Jessica'
print(list(developer))

# Finding the length of a list you can use len() function to get the length of the list
numbers = [1,2,3,4,5]
len(numbers)

# List Mutability meaning you can update any element in the list as long as you pass in a valid index number 
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

#Index Out of Range Error: If you pass in an index (either positive or negative) that is out of bounds for the list, 
# then you will receive an IndexError:
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
"""

# Removing elements from a list: Elements can be removed from a list using del 
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

# Checking if an Element Exists in a List: The in keyword can be used to check if an element exists in a list:
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

# Nesting list inside other list
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

# To access the nested list, you will need to access it using index 2 since lists are zero-based indexed.
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']

# To further acess the second language from that nested list you will need to acess it using index 1:
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # Rust

#Unpacking values from a list is a technique used to assign values from a list to new variables.
# Here is an example to unpack the developer list into new variables called name, age and job like this:#
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

#Collecting Remaining Items From a List: To collect any remaining elements from a list, you can use the asterisk (*) operator like this:
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

#If the number of variables on the left side of the assignment operator doesn't match the total number of items in the list, then you will receive a ValueError.
# Slicing Lists: Slicing is the concept of accessing a portion of a list by using the slice operator :. To slice a list that starts at index 1 and ends at index 3, you can use the following syntax:
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3] # ['Cookies', 'Ice Cream']

# Step Intervals: It is also possible to specify a step interval which determines how much to increment between the indices.
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]

# append(): Used to add an item to the end of the list. Here is an example of using the append() method to add the number 6 to this numbers list:
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

#Appending lists: The append() method can also be used to add one list at the end of another:
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

