# Shea Oliver
# 10/02/2024
# P2LAB2
# Using Dictionaries

# Create Dictionary
cars = {"Camaro":18.21,"Prius":52.36,"Model S":110,"Silverado":26}
#Print keys
keys = cars.keys()
print(keys)
print()
# Allow user to select vehicle and display mpg
vehicle_choice = input("Enter a vehicle to see its mpg: ")
print()
print(f"The {vehicle_choice} gets {cars[vehicle_choice]} mpg")
print()
# Get mileage input from user
number_miles = float(input(f"How many miles will you drive the {vehicle_choice}? "))
print()
#Calculate fuel requirement
gallons = number_miles / cars[vehicle_choice]
#Display fuel requirement
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle_choice} {number_miles:.1f} miles.")
