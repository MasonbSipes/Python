# Password Generator #

# ========== #
#
# Notes:
# 1. What happens when someone enters a wrong number or letter/word?
#
# ========== #

# Importing random and string libraries
import random
import string

# Defining different variables to make the password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
ups_special = "!$&"

# Print different levels of severity
print("------------------------------------")
print("| Different severity levels:       |")
print("| 1. Minor (12 characters)         |")
print("| 2. Intermediate (16 characters)  |")
print("| 3. Major (32 characters)         |")
print("------------------------------------")
print()

# Geth input from user for severity level
choose_severity_level = int(input("Choose a severity level: "))
print()

# Get input from user for type of password
is_ups_pw = input("Will this be used as a UPS password?: ")
print()

# ==================================================================================================== #

# Definition for option one
def option_one():
    if choose_severity_level == 1 and is_ups_pw in ["no", "No", "n", "N"]:
        severity_one = lowercase + uppercase + numbers + special # combine the data
        length = int(12)
        temp = random.sample(severity_one, length) # use random
        password_one = "".join(temp) # create the password
        print(f"Your password is: {password_one}") # print the password

    elif choose_severity_level == 1 and is_ups_pw in ["yes",  "Yes",  "y",  "Y"]:
        severity_one = lowercase + uppercase + numbers + ups_special # combine the data
        length = int(12)
        temp = random.sample(severity_one, length) # use random
        password_one = "".join(temp) # create the password
        print(f"Your password is: {password_one}") # print the password
option_one()

# ==================================================================================================== #

# Definition for option two
def option_two():
    if choose_severity_level == 2 and is_ups_pw in ["no", "No", "n", "N"]:
        severity_two = lowercase + uppercase + numbers + special # combine the data
        length = int(16)
        temp = random.sample(severity_two, length) # use random
        password_two = "".join(temp) # create the password
        print(f"Your password is: {password_two}") # print the password

    elif choose_severity_level == 2 and is_ups_pw in ["yes",  "Yes",  "y",  "Y"]:
        severity_two = lowercase + uppercase + numbers + ups_special # combine the data
        length = int(16)
        temp = random.sample(severity_two, length) # use random
        password_two = "".join(temp) # create the password
        print(f"Your password is: {password_two}") # print the password
option_two()

# ==================================================================================================== #

# Definition for option three
def option_three():
    if choose_severity_level == 3 and is_ups_pw in ["no", "No", "n", "N"]:
        severity_three = lowercase + uppercase + numbers + special # combine the data
        length = int(32)
        temp = random.sample(severity_three, length) # use random
        password_three = "".join(temp) # create the password
        print(f"Your password is: {password_three}") # print the password

    elif choose_severity_level == 3 and is_ups_pw in ["yes",  "Yes",  "y",  "Y"]:
        severity_three = lowercase + uppercase + numbers + ups_special # combine the data
        length = int(32)
        temp = random.sample(severity_three, length) # use random
        password_three = "".join(temp) # create the password
        print(f"Your password is: {password_three}") # print the password
option_three()
