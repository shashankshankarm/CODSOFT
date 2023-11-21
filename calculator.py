def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

# Take user input for the values of a and b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Take user input for the operation to be performed (+, -, *, /)
c = input("Enter the operation {+,-,*,/}: ")

# Create a dictionary to map operations to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Check if the operation requested by the user exists in the dictionary
if c in operations:
    result = operations[c](a, b)  # Perform the operation using the mapped function
    print(result)  # Print the result
else:
    print("Invalid input")  # If the operation input is not one of '+', '-', '*', '/', print an error message
