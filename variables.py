# Python 101 - Variables #

# First script!
print("Hello World!")

# --- #

# Variables


# Clear and descriptive variable names make your code easier to understand and maintain.
# 1. Descriptive names
# 2. Use underscores
# 3. Avoid reserved keywords
# 4. Keep it lowercase


# Once a variable is decleared, you can change its value anytime by assigning a new value to it.
age = 10 # age variable is set to 10
age = 20 # age variable is changed to 20

# Example:
# Declare initial variables
user_name = "Mason"
user_age = 26

print(f"User Name: {user_name}")
print(f"User Age: {user_age}")
print()

# Reassigning new values to the variables
user_name = "Olivia"
user_age = 25

print("Updated User Information")
print(f"User Name: {user_name}")
print(f"User Age: {user_age}")
print()


# Example: Storing User Input
user_input = input("Enter your favorite color: ")
print(f"Your favorite color is {user_input}")
print()

# Example: Performing Calculations
num1 = 10
num2 = 5
sum = num1 + num2
print(f"The sum of {num1} and {num2} is equal to {sum}")
print()

# Example: Using Approprate Naming Conventions
book_title = "1984"
author_name = "Gorge Orwell"
publication_year = 1949
price = 19.99

print(f"Title: {book_title}")
print(f"Author: {author_name}")
print(f"Year: {publication_year}")
print(f"Price: ${price}")
print()