# Homework 5
# Task: Write a program that checks if a number is even or odd

# --- #

# getting user number
number = input('Enter a number: ')

# checking if the number is even or odd
if int(number) % 2 == 0:
    print(str(number + ' is a even number.'))
else:
    print(str(number + ' is an odd number.'))