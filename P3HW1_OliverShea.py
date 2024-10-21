# Shea Oliver
# 10/21/2024
# P3HW1
# Correct errors and use if statements


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [ mod_1, mod_2, mod_3, mod_4, mod_5, mod_6 ]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg = float(sum_grades/len(grades))

# determine letter grade for average

print('-----------Results-----------')

# Print min, max, and sum
print(f"{'Lowest grade:':<18}{min(grades):<25}")
print(f"{'Highest grade:':<18}{max(grades):<25}")
print(f"{'Sum of grades:':<18}{sum(grades):<25}")

# Calculate and print average
print(f"{'Average:':<18}{avg:<25,.2f}")

print('-----------------------')

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') 





