# Python 101 - Applied Variable Manipulation #

# Scenario 1
# TASK: Calculate the total cost of a shopping list.
def scenario_one():
    apple_price = 0.50 * 10
    banana_price = 0.30 * 5
    orange_price = 0.80 * 8
    total = apple_price + banana_price + orange_price
    print(total) # Output: 1.6
    print()
scenario_one()


# Scenario 2
# TASK: Combine first and last names into a single string to display the full name.
def scenario_two():
    get_first_name = input("Enter first name: ")
    get_last_name = input("Enter last name: ")
    full_name = get_first_name + " " + get_last_name
    print(f"Hello, {full_name}!")
scenario_two()


# Scenario 3
# TASK: Transfer the water so that each container has an equal amount.
container1 = 12
container2 = 7
container3 = 0

# Equal distribution formula
total_water = container1 + container2 + container3
equal_amount = total_water / 3

# Adjusting the containers
container1 = equal_amount
container2 = equal_amount
container3 = equal_amount

# Output
print(f"Contanier 1: {container1} liters")
print(f"Contanier 2: {container2} liters")
print(f"Contanier 3: {container3} liters")
