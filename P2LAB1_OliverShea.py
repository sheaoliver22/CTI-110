# Shea Oliver
# 09/30/2024
# P2LAB1
# Using imported library, math, and f-string


# import math module
import math

# Get radius from user

radius = float(input("What is the radius of the circle? "))
print()

# Calculate and display diameter
diameter = 2*radius
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calculate and display circumference
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {circumference:.2f}\n")

#Calculate and display area
area = (radius**2)*math.pi
print(f"The area of the circle is {area:.3f}")
