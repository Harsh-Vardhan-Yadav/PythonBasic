                  # Dictionary in Python 
# A dictionary is a data structure in Python that stores data in key-value pairs. Dictionary items (key – value pair) are ordered, changeable, and do not allow duplicates. 
# • Key: Must be unique and immutable (strings, numbers, or tuples). 
# • Value: Can be any data type and does not need to be unique.   
student = { 
1: "Class-X", 
"name": "Madhav", 
"age": 20 
} 
print(student)

# Create Dictionary in Python :-

# Method-1: We create a dictionary using curly braces {} and separating keys and values with a colon.
# Syntax 
# my_dict =  {"key1": "value1", "key2": "value2", "key3": "value3", …} 

# Empty dictionary 
empty_dict = {} 

# Dictionary with data 
cohort = { 
"course": "Python", 
"instructor": "Prince Yadav", 
"level": "Advanace" 
}

# Method-2: Using dict() constructor   
# Pass key-value pairs as keyword arguments to dict()

# Method-2: Using dict() constructor   
# Pass key-value pairs as keyword arguments to dict()

person = dict(name="Monika", age=20, city="Naini") 
print(person)   # Output: {'name': 'Monika', 'age’: 20, 'city': 'Naini'} 

# Method-3: Using a List of Tuples :-
# Pass a list of tuples, where each tuple contains a key-value pair.  
student = dict([("name", "Madhav"), ("age", 20), ("grade", "A")]) 
print(student)        # Output: {'name': 'Madhav', 'age’: 20, 'grade': 'A'}

# Access Dictionary Values  :- 
# Access dictionary values by using the key name inside square brackets. 
student = { 
1: "Class-BCA", 
"name": "Aanchal", 
"age": 20 
}  
 # print value based on respective key-names  
print(student["name"])  # Output: Madhav 
print(student["age"])  # Output: 20

# Dictionary Methods :- 
# values, fromkeys, get, items, keys, update, pop, popitem, clear, copy 
# Here are a few useful methods: 
# • .keys(): Returns all keys in the dictionary. 
# • .values(): Returns all values in the dictionary. 
# • .items(): Returns all key-value pairs. 
# • .get(): Returns value for a key (with an optional default if key is missing).

print(student.keys())      # All keys
print(student.values())    # All values
print(student.items())     # All key-value pairs 
print(student.get("name")) # Safe way to access a value

# Dictionary – Add, Modify & Remove Items
# 1. Add or Modify Item: Use assign-operator '=' to add/modify items in a dictionary. 
# Adding a new key-value pair 
student["email"] = "madhav@example.com" 

# Modifying an existing value 
student["age"] = 25 

# 2. Remove Item: Use del or .pop() to remove items from a dictionary. 
# Remove with del 
del student["age"] 

# Remove with pop() and store the removed value 
email = student.pop("email") 
print(email)  # Output: madhav@example.com

# Dictionary Iterations 
# A dictionary can be iterated using for loop. We can loop through dictionaries by keys, values, or both. 

# Loop through keys 
for key in student: 
  print(key) 
# Loop through values 
for value in student: 
  print(student[value]) 
# Loop through values: using values() method 
for value in student.values(): 
  print(value) 
# Loop through both keys and values 
for key, value in student.items(): 
  print(key, value)

# Nested Dictionary  
# Dictionaries can contain other dictionaries, which is useful for storing more complex data.  
# nested dictionaries 
students = { 
"student1": { 
"name": "Monika",  
"age": 20,  
"grade": "A" 
}, 
"student2": { 
"name": "Prince",  
"age": 21,  
"grade": "B" 
} 
} 
print(students["student1"]["name"])  # Output: Monika

# Dictionary Comprehension  
# A dictionary comprehension allows you to create dictionaries in a concise way. 
# Syntax:  new_dict =  {key_expression: value_expression for item in iterable if condition} 

# Example: Creating a dictionary with square numbers 
squares = {x: x * x for x in range(1, 6)} 
print(squares)                    # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

# Dictionary Common Use Cases  
# • User Profiles in Web Applications: Store user details like name, email, etc.  
# • Product Inventory Management: Keep track of stock levels for products in an e
# commerce system. 
# • API Responses: Parse JSON data returned from APIs (e.g., weather data).  
# • Grouping Data: Organize data into categories. Example: grouped = {"fruits": 
# ["apple", "banana"], "veggies": ["carrot"]} 
# • Caching: Store computed results to reuse and improve performance. Example: 
# cache = {"factorial_5": 120} 
# • Switch/Lookup Tables: Simulate switch-case for decision-making.

# actions = {"start": start_fn, "stop": stop_fn} actions["start"]()   


  # -----------------------------------Done--------------------------------