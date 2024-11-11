# Learning to use user-defined functions

# Define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)

# Define an addition function
def add(num1, num2, num3):
    result = num1 * num2 * num3
    print(result)

# Define the main function
def main():
    # Get input from user
    first_num = int(input("Enter a number: "))
    second_num = int(input("Enter a number: "))
    third_num = int(input("Enter a number: "))
    # Call the multiply function
    multiply(first_num,second_num,third_num)
    # Call the add function
    add(first_num,second_num,third_num)

#Call the main function
if __name__ == "__main__":
     main()