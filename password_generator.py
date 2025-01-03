# Password Generator #

# ========== #
#
# Notes:
# 1. 
#
# ========== #

# Importing random and string libraries
import random, string

# Defining different variables to make the password
lowercase = string.ascii_lowercase * 2
uppercase = string.ascii_uppercase * 2
numbers = string.digits * 2
special = string.punctuation * 2
none_ambiguous_special = "!$&@"

# Get length of password
print()
print("How long do you want the password to be?")
print("NOTE: your password can be up to 128 characters long.")
get_length = int(input())

# Check if password is too long
while True:
    if get_length > 128:
        print("Password is too long. Please try again.")
        get_length = int(input())
    else:
        break

# Check is user needs to avoid ambiguous characters
print("Need to avoid any ambiguous characters like '%^*()'?")
avoid_ambiguous_characters = input()


if avoid_ambiguous_characters in ["Y", "Yes", "y", "yes"]:
    make_password_none_ambiguous = lowercase + uppercase + numbers + none_ambiguous_special
    length = get_length
    temp = random.sample(make_password_none_ambiguous, length)
    password = "".join(temp)
    print(f"Your password is: {password}")
    quit()

elif avoid_ambiguous_characters in ["N", "No", "n", "no"]:
    make_password_ambiguous = lowercase + uppercase + numbers + special
    length = get_length
    temp = random.sample(make_password_ambiguous, length)
    password = "".join(temp)
    print(f"Your password is: {password}")
    quit()
