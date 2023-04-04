
def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 + num2


def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 - num2


def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 * num2


def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 / num2


print("Select which operator you wish to use: 1 = add, 2 = subtract, 3 = multiply, 4 = divide: ")

i = input()
if i == "1":
    print("Result: ", add())

if i == "2":
    print("Result: ", subtract())

if i == "3":
    print("Result: ", multiply())

if i == "4":
    print("Result: ", divide())