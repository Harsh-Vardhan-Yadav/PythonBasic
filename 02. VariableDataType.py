#Variable Syntax - variable_Name = Value
Greet = "Hello World"
print(Greet)
a=10; b=20
print(a+b)
# How to check variable data type in python
print(type(Greet))
print(type(a))
#Data Types in Python Basics
#1. Numeric
p=10            #int interger value only
q=20.34         #float point value only
r=complex(4,5)  #complex Number real and imaginary number combination e.g. 3+6i
print(p)
print(q)
print(r)

#2. String also value lie inside double quotes 
name = "Harsh Vardhan Yadav"
print(name)

#3. Boolean on true false value
t = True          #True or False 
print(t)

#Type casting :- Convert one data type to onther data type
# int(): Converts a value to an integer. 
# float(): Converts a value to a floating-point number. 
# str(): Converts a value to a string. 
# list(), tuple(), set(), dict() and bool()
# Converting String to Integer: 
str_num = "26" 
print(type(str_num))
print(str_num)
int_num = int(str_num)
print(type(int_num)) 
print(int_num)    

# There are two types of type casting in python: 
# • Implicit type casting  :- Automatically by the Python interpreter. 
# • Explicit type casting :- Performed manually by the programmer using
#   built-in functions

# Input Function in Python : It reads the input as a string.
# Syntax variable_name = input("Massage..... ")
name = input("Enter The Name :")
print("Hello ",name)

#Typecate input data by default string
num1 = input("Enter The Number ")
print(type(num1))
print(num1)
num2 = int(input("Enter The Number "))
print(type(num2))
print(num2)

# Home Work – User input 3 subject marks and print result percentage
