# Simple Calculator in Python

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Main program
print("Simple Calculator")
try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    result = calculate(number1, number2, op)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")