# Learning to use user-defined functions

# Define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)

# Define an addition function
def add(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)

def returnNum():
    userInput = input("Give me a big number: ")
    while not userInput.isnumeric():
        print("Value must be a number")
        userInput = input("Give me a big number: ")
    return int(userInput)

def getName(lastName):
    name = input("Enter your name: ")
    fullname = "******************" + name + "******************" + lastName
    return fullname

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

    bigNum = returnNum()

    print(bigNum * 5)

    print(getName("Oliver"))

#Call the main function
if __name__ == "__main__":
     main()