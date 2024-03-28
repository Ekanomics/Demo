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


def main():
    print("Welcome, please try my calculator")

    operation = input("Enter operation: ")

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
        print("Result is:", add(num1, num2))
    elif operator == '-':
        print("Result is:", subtract(num1, num2))
    elif operator == '*':
        print("Result is:", multiplication(num1, num2))
    elif operator == '/':
        print("Result is:", divide(num1, num2))


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print ("Error:", e)
