# Shea Oliver
# 9/25/2024
# P1HW2
# Determine remaining funds after travel expenses


# Get inputs from user

budget = int(input("Enter your budget: "))
destination = int(input("Enter your travel destination: "))
gas = int(input("Estimated gas expenses: "))
lodging = int(input("Estimated accomodation expenses: "))
food = int(input("Estimated food/drink expenses: "))

# Display travel expenses back to user

print("------Travel Expenses-----")
print("Location:" , destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:" , lodging)
print("Food:", food)
print()

# Determine remaining balance

remaining_balance = budget - destination - gas - lodging - food

# Display remaining balance to user
print("Your remaining balance is:" , remaining_balance)
