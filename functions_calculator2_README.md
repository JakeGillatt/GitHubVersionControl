# Create a calculator using functions and enable user input

create the 4 operator functions, allow for 2 user inputs, calculate the user inputs and return the value.
```
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
```

give the user a list of operators to choose from.
```
print("Select which operator you wish to use: 1 = add, 2 = subtract, 3 = multiply, 4 = divide: ")
```

allow the user to input their choice and assign it to the variable 'i'
```
i = input()
```
create if and elseif statements to determine the user selection and act accordingly. print the selected functions return value.
```
if i == "1":
    print("Result: ", add())

elif i == "2":
    print("Result: ", subtract())

elif i == "3":
    print("Result: ", multiply())

elif i == "4":
    print("Result: ", divide())
```