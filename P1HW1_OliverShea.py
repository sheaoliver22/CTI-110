# Shea Oliver
# 09/16/2024
# P1HW1
# Using math expressions with user input

print("-----Calculating Exponents-----")
print()
print()


#Get input from user and convert to integer
base_value = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent: '))
print()

#Calculate math result
exponent_solution= str(base_value ** exponent)


#Display math result to user
print(base_value, 'raised to the power of', exponent, 'is', exponent_solution + '!!!')
print()
print()


print("-----Addition and Subtraction-----")
print()
print()

#get input from user
start_num = int(input('Enter a starting integer: '))
add_num = int(input('Enter an integer to add: '))
sub_num = int(input('Enter an integer to subtract: '))

print()
print()

#calculate solution
arithmetic_solution = start_num + add_num - sub_num

#calculate & display solution
print(start_num, '+', add_num, '-', sub_num, 'is equal to', arithmetic_solution)
