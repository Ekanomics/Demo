def add (a, b):
    return a + b
#сложение

def subtract (a, b):
    return a - b
#вычитание

def multiplication (a, b):
    return a * b
#умножение

def divide (a, b):
    if b == 0:
        return "Impossible, error"
    else:
        return a // b
#деление

print("Welcome, please try my calculator")


def calculate(operation):

    try:
        parts = operation.split()
        if len(parts) != 3:
            raise ValueError("Incorrect format")

        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])

        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            raise ValueError("Numbers should be from 1 to 10")

        if operator not in ('+', '-', '*', '/'):
            raise ValueError("Incorrect operator")

        if operator == '+':
            return str(add(num1, num2))
        elif operator == '-':
            return str(subtract(num1, num2))
        elif operator == '*':
            return str(multiplication(num1, num2))
        elif operator == '/':
            return str(divide(num1, num2))

    except ValueError as e:
        raise e

def main(input_str):
    return calculate(input_str)

if __name__ == "__main__":
    while True:
        try:
            operation = input("Enter operation: ")
            result = main(operation)
            print("Result is:", result)
        except ValueError as e:
            print("throws exception: ", e)
