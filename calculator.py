print("CALCULATOR \n")

#operations
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num3):
    return num1 * num2

def div(num1, num2):
    if num2==0:
        return "Error!: Division by zero is not possible."
    
    return num1 / num2 

# Take input from user
num1=float(input("Enter first number:"))

operator=(input("Enter function: + ,-,*,/ :"))

num2=float(input("Enter second number:"))

# operation handeled 

if operator == '+':
    result = add(num1,num2)
elif operator == '-':
    result =sub(num1,num2)
elif operator == '*':
    result = mul(num1,num2)
elif operator =='/':
    result = div(num1,num2)
else:
    result ="invalid operator!"

print("Result=", result)
