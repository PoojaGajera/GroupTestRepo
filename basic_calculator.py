# basic_calculator.py
vedika vedik
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation: +, -, *, /")
    op = input("Enter operation: ")

    if op == '*':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            exit(1)
    else:
        print("Invalid operation.")
        exit(1)

    print(f"Result: {result}")
