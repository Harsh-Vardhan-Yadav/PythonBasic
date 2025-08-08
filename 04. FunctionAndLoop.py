#Function :- A function is a block of code that performs a specific task.
#Benefits of Using Function:  Increases code Readability & Reusability. 
# Basic Concepts: 
# • Create function: Use the def keyword to define a function. 
# • Call function: Use the function's name followed by () to run it.  
# • Parameter: The variable listed inside parentheses in function definition. 
# • Argument: The actual value you pass to function when you call it.Types of Functions  
# Below are the two types of functions in Python: 
# 1. Built-in library function:  
# • These are Standard functions in Python that are available to use. 
# • Examples: print(), input(), type(), sum(), max(), etc 
# 2. User-defined function:  
# • We can create our own functions based on our requirements. 
# • Examples:  create your own function :)

def show():
  print("Hello, I am Function. ")
show()

# Add two Number Using Function
def sum(a,b):
  print(f'Sum of {a} and {b} is {a+b}')
n1 = int(input("Enter First Number :"))
n2 = int(input("Enter Second Number :"))
sum(n1,n2)

# Add two Number Using Function with return type
def sum(a,b):
  s=a+b
  return s
n3 = int(input("Enter First Number :"))
n4 = int(input("Enter Second Number :"))
s=sum(n3,n4)
print(f'Sum of {n3} and {n4} is {s}')

# Types of Function Arguments
# 1. Required arguments (Single/Multiple arguments) 
# 2. Default argument 
# 3. Keyword arguments (named arguments) 
# 4. Arbitrary arguments (variable-length arguments *args and **kwargs)

# 1. Required arguments (Single/Multiple arguments) 
# It is same as other language above example is this type.

# 2. Default argument 
def greetings(name = "World"):   # default value 
  print("Hello, " + name + "!") 
greetings()              # No argument passed  Output: Hello, World! 
greetings("Madhav")     # Madhav as argument | Output: Hello, Madhav! 

# 3. Keyword arguments (named arguments) 
def divide(a, b):                # a,b are 2 parameters 
  return a / b 
result = divide(b=10, a=20)     # with keyword arguments 
print(result)                   # Output: 2
result = divide(10, 20)    
print(result)                   # positional arguments | Output: 0.5 

# 4. Arbitrary arguments (variable-length arguments *args and **kwargs)
# i) Arbitrary Positional Arguments (*args)  
# If you're unsure how many arguments will be passed, use *args to accept any number of positional arguments.   
# Purpose: Allows you to pass a variable number of positional arguments. 
# Type: The arguments are stored as a tuple. 
# Usage: Use when you want to pass multiple values that are accessed by position.  
# Example 1: 
def add_numbers(*args): 
  return sum(args)                  # Any number of arguments 
result = add_numbers(1, 2, 3, 4) 
print(result)                       # Output: 10 
# Note: Here, *args collects all the passed arguments into a tuple, & sum() function adds them. Example : 
def greetings(*names): 
  for name in names: 
    print(f"Hello, {name}!") 
greetings("Madhav", "Rishabh", "Visakha") 
# Output: Hello, Madhav! Hello, Rishabh! Hello, Visakha! 
# Arbitrary Keyword Arguments (**kwargs)  
# If you want to pass a variable number of keyword arguments, use **kwargs. 
# Purpose: Allows you to pass a variable number of keyword arguments (arguments with 
# names). 
# Type: The arguments are stored as a dictionary. 
# Usage: Use when you want to pass multiple values that are accessed by name.
#It is same *args with keyword argument 
  
# Loops in Python : Loops enable you to perform repetitive tasks efficiently without writing redundant code.
# Types of Loops in Python 
# 1. While loop 
# 2. For loop 
# 3. Nested loop

# 1. While Loop :- 
# Syntax:  
# while condition: 
#     Code block to execute 

# Print numbers from 0 to 5 
count = 0 
while count < 6:   
  print(count) 
  count += 1 

# 2. For Loop :- 
# Syntax:  
# for variable in sequence: 
#      Code block to execute 
language = "Python" 
for x in language: 
  print(x)  

# Using range() Function 
# Syntax:         By default start with zero and increment by 1
# range(stop)              (optional)
# range(start, stop)       (exclusive)
# range(start, stop, step) (optional)

# Output: 0  1  2  3  4
for i in range(5): 
  print(i)

# Output: 1  3  5  7  9 
for i in range(1, 10, 2): 
  print(i) 
  
# Loop Control Statements : oop control statements allow you to alter the normal flow of a loop.
# • pass statement :  The pass statement is used as a placeholder (it does nothing)
for i in range(5):
  pass

# break Statement-The break statement terminates the loop entirely, exiting from it 
# immediately.
for i in range(5): 
  if i == 3: 
    break 
  print(i)  
# Output: 0  1  2

# continue Statement : The continue statement skips the current iteration and moves 
# to the next one.   
for i in range(5): 
   if i == 3: 
      continue 
   print(i) 

   #Prince Yadav Done
