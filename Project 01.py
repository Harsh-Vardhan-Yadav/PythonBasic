# Basic Calculator using function, input function and conditinal statment 
def sum(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
def avg(a,b):
  return (a+b)/2
print("Please select a operation:\n " 
      "1. Addition\n" 
      "2. Substraction\n" 
      "3. Multiplication\n" 
      "4. Division\n" 
      "5. Average\n") 
ch = int(input("Enter Choice Based on Operation :"))
n1 = int(input("Enter First Number :"))
n2 = int(input("Enter Second Number :"))
if ch==1:
  s=sum(n1,n2)
  print(f'Sum of {n1} and {n2} is {s}')
elif ch==2:
  sb=sub(n1,n2)
  print(f'Minus of {n1} and {n2} is {sb}')
elif ch==3:
  m=mul(n1,n2)
  print(f'Multiply of {n1} and {n2} is {m}')
elif ch==4:
  d=div(n1,n2)
  print(f'Divied of {n1} and {n2} is {d}')
elif ch==5:
  av=avg(n1,n2)
  print(f'Divied of {n1} and {n2} is {av}')  
else:
  print("Wroung Choice.....")  