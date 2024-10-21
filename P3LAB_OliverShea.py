# Shea Oliver
# 10/21/2024
# P3LAB
# Determine change from dollar input

#get input from user
money = float(input('Enter the amount of money as a float: $'))

# convert money to integer and round
money = int(round(money*100))
#Determine cents
change = money % 100

if money == 0:
    print("No change")
#Display amount of dollars
elif money // 100 == 1:
    print(money // 100, "Dollar")
elif money // 100 > 1:
    print(money // 100, "Dollars")
#Display amount of quarters 
if change // 25 == 1:
    print(change // 25, "Quarter")
elif change // 25 > 1:
    print(change // 25, "Quarters")
# Subtract quarters from remaining change then display dimes
change = change - ((change // 25)*25)
if change // 10 == 1:
    print(change // 10, "Dime")
elif change // 10 > 1:
    print(change // 10, "Dimes")
#Subtract dimes from remaining change then display nickels
change = change - ((change // 10)*10)
if change // 5 == 1:
    print(change // 5, "Nickel")
elif change // 5 > 1:
    print(change // 5, "Nickels")
#Subtract nickels from remaining change then display pennies
change = change - ((change // 5)*5)
if change == 1:
    print(change, "Penny")
elif change > 1:
    print(change, "Pennies")
