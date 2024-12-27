# Python 101 - Arithmatic and String Operations #

# Addition
def addition():
    x = 5
    y = 3
    result = x + y
    print(f"For addition, the output is: {result}") # Output: 8
    print()
addition()


# Subtraction
def subtraction():
    x = 5
    y = 3
    result = x - y
    print(f"For subtraction, the output is: {result}") # Output: 2
    print()
subtraction()


# Multiplication
def multiplication():
    x = 5
    y = 3
    result = x * y
    print(f"For multiplication, the output is: {result}") # Output: 15
    print()
multiplication()


# Division
def division():
    x = 5
    y = 3
    result = x / y
    print(f"For division, the output is: {result}") # Output: 1.66
    print()
division()


# --- #


# Manipulating Strings
# String Concatenation: To concatenate strings, use the + operator.
# Example:
greeting = "Hello"
name = "Mason"
message = greeting + ", " + name + "!"
print(message) # Output: Hello, Mason!
# NOTE: This is handy when you need to build dynamic text outputs.


# Gathering user input with the input() fuction.
# Example:
user_name = input("Enter your username: ")
print(f"Hello, {user_name}")
print()
