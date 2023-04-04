# functions

# Allow you to follow DRY (Do not Repeat Yourself)

# def print_something():
#     print("Hello")


def greeting(name):
    print("Hello, my name is " + name)


greeting("Jake")

# return statement

def addition(int1, int2):
    return int1 + int2


print(addition(2, 2))


# Default arguments

def addition(int1=2, int2=2):
    return int1 + int2

print(addition(10, 5)) # this will override the default values assigned at def

# multiple arguments

def multi_args(*multiargs): # * says this is now a tuple - a list that cant be changed
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6)


# type hints

def greeting(name:str): # tells the program that it must be a string
    print("Hello, my name is " + name)


greeting("hello")

def division(denum: int, num: int) -> float: # -> float expects output to be a float
    return denum / num

print(division(12, 4))

def subtraction(int1: int = 5, int2: int = 2) -> int:
    return int1 - int2

print(subtraction())

# functions best practices

# 1. Name your methods using lowercase and _
# 2. All arguments should be clear in their need and where possible their type
# 3. Remember the return statement or your function will return None
# 4. Keep your functions as small as possible and keep them readable
# 5. Use comments within your methods to help explain everything
# 6. Consider using type hints to avoid errors sooner

# make a calculator using functions