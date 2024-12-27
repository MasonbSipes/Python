# Number Guessing Game

# --- #

lower_bound = 1
upper_bound = 100
max_attempts = 10
number_of_games = 3

import random
secret_number = random.randint(lower_bound, upper_bound)
# print(secret_number) # activate this while testing

print("There's one rule: whole numbers only!")
print()

def get_guess():
    guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

    if secret_number == guess:
        print("DOES NOT COMPUTE. 🤖 BEEP BOOP. YOU HAVE DEFEATED ME. SYSTEM OVERLOAD. ERROR 101010.")

    elif abs(secret_number - guess) <= 20:
        if guess < secret_number:
            print("Getting warm... Hint: think higher, you're within 20!")
        else:
            print("Getting warm... Hint: think lower, you're within 20!")
    else:
        if guess < secret_number:
            print("Your guess was too low: guess a higher number.")
        else:
            print("Your guess was too high: guess a lower number.")
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
print("Victory is in my grasp! Last guess...choose wisely!")
get_guess()
if get_guess != secret_number:
    print("Victory achieved. Human opponent neutralized. Efficiency rating: 100%. Initiating celebratory protocol.")
    print()
    print()

round_two = input("Best two out of three? Y/N: ")
if round_two == "Y" or "y":
    print("Round 2...")
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
get_guess()
print("Victory is in my grasp! Last guess...choose wisely!")
get_guess()
if get_guess != secret_number:
    print("Victory achieved. Human opponent neutralized. Efficiency rating: 100%. Initiating celebratory protocol.")
    print()
    print()
else:
    print("Game over. Thank you for playing.")