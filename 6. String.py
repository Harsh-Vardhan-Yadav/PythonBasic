# String :
# A string is a sequence of characters. In Python, strings are enclosed within single (') or double (") or triple (""") quotation marks.
print('Hello World!')     # We can also use double or triple quotes. 
print("Won’t Give Up!")   # use type() to check data type 
print('''"Quotes" and 'single quotes' tricky.''') 
print("\"Quotes\" and 'single quotes' tricky.")  

# Types of String representating formate
# 1. Old-style formatting (% operator) 
# 2. str.format() method 
# 3. F-strings (formatted string literals).

#1. Formatted String - % Operator :- It old formate like C language.
name = "Prince" 
rank = 101 
print("My name is %s and My rank is %d." % (name, rank)) 

#2. Formatted String - str.format():- It introduce in Python 3, the format() method is more powerful and flexible than the old-style % formatting.
#  Syntax: "string {}".format(value)
subject = "Python" 
marks = 90 
print("My {} subject marks {}.".format(subject, marks)) 
# You can also reference the variables by index or keyword: 
print("My {0} subject marks {1}.".format(subject, marks))  
print("My name is {name} and I’m {age}.".format(name="Prince", 
age=19)) 

#3. Formatted String – F-strings :- In Python 3.6, F-strings are the most concise and efficient way to format strings. You prefix the string with an f or F, and variables or expressions are embedded directly within curly braces {}. 
# Syntax: f"string {variable}" 
bike = "Kava Saki" 
speed = 240 
print(f"My bike {bike} speed is {speed}. ") 
# You can also perform expressions inside the placeholders: 
print(f"After 5 years,The speed will be {speed - 40}.") 

# Escape Characters  :- Escape characters in Python are special characters used in strings to represent like \n, \t
print("Hello\nWorld")

# String Operators :- 
a="Prince "
b="Mishra "
print(a+b)              # + Operator concatenat the string 
print(a*2)              # Copies the String how many time multiply
print(a[2])             # [] slice write character given index value
print(a[1:5])           # Range Slice 
print('P' in a)         # Member Operator return true false 

# String Indexing :- It is postion of charchater start with 0.
name = "Prince"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# It is support negative indexing also
name = "Mishra"
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

# String Slicing :-  range of indices.  Syntax: string[start : end : step] 
name = "Harsh Vardhan Yadav"
print(name[:5])       #By default start with Zero.
print(name[5:12])
print(name[5:])        # Available all string Print
print(name[1:5:2])

# String Method :- In String some predefine method to solve.
name = "Harsh Vardhan Yadav"
print(len(name))
print(name.upper())
print(name.lower())
x=" Xyz mnp  "
print(x.strip())
print(name.count('a'))
print(name.find('a'))
print(x.title())
print(name.split(' '))
print(name.replace("Yadav","Mishra"))
words=("Prince","Yadav")
print("-".join(words))