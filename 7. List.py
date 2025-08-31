# List in Python :- A list in Python is a collection of items (elements) that are ordered, changeable (mutable), and allow duplicate elements.  
# Lists are one of the most versatile data structures in Python and are used to store 
# multiple items in a single variable. 
fruits = ["apple", "orange", "cherry", "apple"] 
print(fruits) 

# Create List in Python :- You can create lists in Python by placing comma-separated values between square brackets [].  Lists can contain elements of different data types, including other lists. 
# Syntax :- list_name = [element1, element2, element3, ...] 
# List of strings 
colors = ["red", "green", "blue"] 
print(colors)
# List of integers 
numbers = [1, 2, 3, 4, 5]
print(numbers) 
# Mixed data types 
mixed = [1, "hello", 3.14, True]
print(mixed) 
# Nested list 
nested = [1, [2, 3], [4, 5, 6]] 
print(nested)

# Accessing List Elements - Indexing :- You can access elements in a list by referring to their index. Python uses zero-based indexing, meaning the first element has an index of 0.
fruits = ["apple", "orange", "cherry", "apple"] 
print(fruits[1]) 

# List Slicing :- Slicing allows you to access a range of elements in a list. You can specify the start and stop indices, and Python returns a new list containing the specified elements.
# Syntax:  list_name[start:stop:step] 
numbers = [10, 20, 30, 40, 50, 60]
# Slice from index 1 to 3   
print(numbers[1:4])  # Output: [20, 30, 40] 
# Slice from start to index 2  
print(numbers[:3])  # Output: [10, 20, 30] 
# Slice all alternate elements  
print(numbers[0::2])  # Output: [10, 30, 50] 
# Slice with negative indices  
print(numbers[-4:-1])  # Output: [30, 40, 50] 
# Reverse list  
print(numbers[::-1])  # Output: [60,50,40,30,20,10]

# Modifying List :- Lists are mutable, meaning you can change their content after creation. You can add, remove, or change elements in a list.

fruits = ["apple", "banana", "cherry"] 
# Changing an element 
fruits[1] = "blueberry" 
print(fruits)                     # Output: ['apple', 'blueberry', 'cherry'] 
# Adding an element 
fruits.append("mango") 
print(fruits)                    # Output: ['apple', 'blueberry', 'cherry’, 'mango'] 
# Removing an element 
fruits.remove("cherry") 
print(fruits)                   # Output: ['apple', 'blueberry', 'mango']

print(fruits)    
# Output: ['apple', 'blueberry', 'mango']
 
# List Methods :- Python provides several built-in methods to modify and operate on lists. 
# Join Lists :- There are several ways to join, or concatenate, two or more lists in Python. 
list1 = [1, 2]  
list2 = ["a", "b"] 
# One of the easiest ways are by using the + operator 
list3 = list1 + list2 
print(list3)          # Output: [1, 2, 'a', 'b'] 
# using append method 
for x in list2: 
  list1.append(x)   
# appending all the items from list2 into list1, one by one 
print(list1)            # Output: [1, 2, 'a', 'b'] 
# using extend method 
list1.extend(list2)       # add elements from one list to another list 
print(list1)            # Output: [1, 2, 'a', 'b']

# List Comprehensions :- List comprehensions provide a concise way to create lists
# They consist of brackets containing an expression followed by a for clause,
#  and optionally if clauses. 
# Syntax:   
# new_list = [expression for item in iterable if condition] 
# Creating a list of squares: 
squares = [x**2 for x in range(1, 6)] 
print(squares)                                # Output: [1, 4, 9, 16, 25] 
# Filtering even numbers: 
even_numbers = [x for x in range(1, 11) if x % 2 == 0] 
print(even_numbers)                            # Output: [2, 4, 6, 8, 10] 
# Applying a function to each element: 
fruits = ["apple", "banana", "cherry"] 
uppercase_fruits = [fruit.upper() for fruit in fruits] 
print(uppercase_fruits)                        # Output: ['APPLE', 'BANANA', 'CHERRY'] 

#List Comprehensions - Flatten a List Flatten a Nested List - using List Comprehension 
def flatten_list(lst): 
  return [item for sublist in lst for item in sublist]  
nested_list = [[1, 2], [3, 4], [5, 6]] 
flattened = flatten_list(nested_list) 
print(flattened)   
# Output: [1, 2, 3, 4, 5, 6]

#Iterating Over Lists :- Iterating allows you to traverse each element in a list, typically using loops. 
fruits = ["apple", "banana", "cherry"]  
for fruit in fruits: 
  print(fruit) 
# Using while loop   
index = 0 
while index < len(fruits): 
  print(fruits[index]) 
  index += 1

  # -----------------------------------Done--------------------------------