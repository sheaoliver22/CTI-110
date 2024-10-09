# Shea Oliver
# 10/9/2024
# P2HW1
# Format output of programs


# Get inputs from user

budget = float(input("Enter your budget: "))
destination = (input("Enter your travel destination: "))
gas = float(input("Estimated gas expenses: "))
lodging = float(input("Estimated accomodation expenses: "))
food = float(input("Estimated food/drink expenses: "))

# Display travel expenses back to user

print("----------Travel Expenses---------")
print(f"{'Location:':<20}{destination:<27}")
print(f"{'Initial Budget:':<20}${budget:<27,.2f}")
print(f"{'Fuel:':<20}${gas:<27,.2f}")
print(f"{'Accomodation:':<20}${lodging:<27,.2f}")
print(f"{'Food:':<20}${food:<27,.2f}")
print("-" * 34)
print()

# Determine remaining balance

remaining_balance = budget - gas - lodging - food

# Display remaining balance to user
print(f"{'Remaining balance:':<20}${remaining_balance:<27,.2f}")
