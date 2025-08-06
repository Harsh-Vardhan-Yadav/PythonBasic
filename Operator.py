# Operators in Python 
# Operators in Python are special symbols or keywords used to perform 
# operations on operands (variables and values).  
# Operators: These are the special symbols/keywords. Eg: + , * , /, etc. 
# Operand: It is the value on which the operator is applied.
# Examples Addition operator '+': a + b  
a=10
b=20
c = a + b
print(c)
#Types of Operators   
# 1. Arithmetic Operators +, -, *, /, %
x=50
y=6
print(x+y)    #Addition
print(x-y)    #Subtraction
print(x*y)    #Multiple
print(x/y)    #Divied
print(x//y)   #Floor Division
print(4**2)   #Exponentiation 

# 2. Comparison (Relational) Operators - It compare to value return true or false
p=10
q=20
print(p==q)     # Equal to
print(p!=q)     # Not equal to
print(p>q)      # Greater than
print(p>=q)     # Greater than equal to
print(p<=q)     # Less than equal to
print(p<q)      # less than

# 3. Assignment Operators 
w=200           #Assignment Value 200 in w variable
print(w)
w+=10     # We can also use combine form in assigment operator with arithmetic op. 
print(w)

# 4. Logical Operators 
print(True and True)        # AND Operator
print(False or True)        # OR Operator
print(not False)            # Not Operator

# 5. Bitwise Operators &, |, ^, ~, <<, >> 
print(10>>2)              #Try to undersatnd this topic self

# 6. Identity Operators :- Identity operators are used to compare the memory locations of two objects, not just equal but if they are the same objects.(is, is not).
d=10
e=20
f=10
print(d is f)
print(d is e)
print(d is not e)
print(id(d))    #id function return the variable address if both variable value same 
print(id(e))    # than id value same that means same obejct share value
print(id(f))

# 7. Membership Operators :- Membership operators checks whether a given value is a member of a sequence (such as strings, lists, and tuples) or not.(in and not in)
print("a" in "Amit")
print("P" in "Python")
print(20 not in [10,20,30,40])

            #Conditional Statements in Python  
n1 = int(input("Enter First Number :")) 
n2 = int(input("Enter Second Number :"))
if n1 > n2:               #After if braket optinal and colon must be use
  print(n1," is greater than ",n2);             
else:
  print(n2," is greater than ",n1)

#   There are 5 types of conditional statements in Python: 
# 1. 'if' Statement :-           Only if condition
# 2. 'if-else' statement :-      If else both block
# 3. 'if-elif-else' statement :- Inside if else write if else 
# 4. Nested 'if else' statement:- Multiple if else PARALLEL 
# 5. Conditional Expressions  (Ternary Operator)

# 3. 'if-elif-else' statement 
# Syntax: 
# if condition1: 
# # Code to execute if condition1 is true 
# elif condition2: 
# # Code to execute if condition2 is true 
# else: 
# # Code to execute if none of the above conditions are true 
score = 85 
if score >= 90: 
  print("Grade - A") 
elif score >= 80: 
  print("Grade - B") 
elif score >= 70: 
  print("Grade - C") 
else: 
  print("Grade - D")

  # 5. Conditional Expressions  (Ternary Operator)
  # Syntax:  value_if_true if condition else value_if_false
age = 16 
status = "Adult" if age >= 18 else "Minor" 
print(status)
# Do more task which topic you learn 