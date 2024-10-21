# Shea Oliver
# 10/9/2024
# P2HW2
# Practice with lists

# Get grades from user
grade_list = [float(input("Enter grade for Module 1: ")),float(input("Enter grade for Module 2: ")),float(input("Enter grade for Module 3: ")),float(input("Enter grade for Module 4: ")),float(input("Enter grade for Module 5: ")),float(input("Enter grade for Module 6: "))]

print('-----------Results-----------')

# Print min, max, and sum
print(f"{'Lowest grade:':<18}{min(grade_list):<25}")
print(f"{'Highest grade:':<18}{max(grade_list):<25}")
print(f"{'Sum of grades:':<18}{sum(grade_list):<25}")

# Calculate and print average
print(f"{'Average:':<18}{sum(grade_list)/len(grade_list):<25,.2f}")



print('-' * 29)
