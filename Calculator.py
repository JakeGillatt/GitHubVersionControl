# def calculator():
#     str_calc_welcome = "Welcome to Jake's  Calculator"
#     str_enter_num1 = "Enter the first number:"
#     str_select_op = "Enter a math operator (+, *, -, /)"
#     str_enter_num2 = "Enter the second number"
#     str_error_msg = "Please enter a valid math operator (+, *, -, /)"
#     str_equals: str = "= "
#     calc_result = ""
#
#     # Initialisation
#     print(str_calc_welcome)
#     print(str_enter_num1)
#
#     # User input
#     input_num1 = input()
#     print(str_select_op)
#     input_operator = input()
#     print(str_enter_num2)
#     input_num2 = input()
#
#     # Here is the 'Add' part of the calculator
#     if input_operator == "+":
#         calc_result = float(input_num1) + float(input_num2)
#         print(str_equals + str(calc_result))
#
#     # Here is the 'Multiply' part of the calculator
#     elif input_operator == "*":
#         calc_result = float(input_num1) * float(input_num2)
#         print(str_equals + str(calc_result))
#
#     # Here is the 'Minus' part of the calculator
#     elif input_operator == "-":
#         calc_result = float(input_num1) - float(input_num2)
#         print(str_equals + str(calc_result))
#
#     # Here is the 'Divide' part of the calculator
#     elif input_operator == "/":
#         calc_result = float(input_num1) / float(input_num2)
#         print(str_equals + str(calc_result))
#
#     else:
#         print(str_error_msg)
#
# calculator()

#
# def add(num1, num2):
#     return num1 + num2
#
#
# def subtract(num1, num2):
#     return num1 - num2
#
#
# def multiply(num1, num2):
#     return num1 * num2
#
#
# def divide(num1, num2):
#     return num1 / num2
#
#
# print(add(2, 2))
# print(subtract(2, 2))
# print(multiply(2, 2))
# print(divide(2, 2))

# # calculator with input


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

# def add(num1, num2):
#     return num1, num2
#
#
# def minus(num1, num2):
#     return num1, num2
#
#
# def multiply(num1, num2):
#     return num1, num2
#
#
# def divide(num1, num2):
#     return num1, num2
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#     # Take input from the user
#     choice = input("Enter choice(1/2/3/4): ")
#
#     # Check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         break
#     else:
#         print("Invalid Input")
