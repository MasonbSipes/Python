# Homework 9
# Task: Create a function named 'greet' that takes a name as an argument and prints "Hello, [name]!"

# --- #

greet = input('What is your name?: ')
print ('Hello ' + greet)

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Mason")  # "Mason" is an argument
