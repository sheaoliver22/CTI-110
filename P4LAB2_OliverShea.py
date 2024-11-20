# Shea Oliver
# 10/30/2024
# P4LAB2
# Write code displaying multiplication table using for and while loop


#Create variable to make program run the first time
run_again = "yes"
# While loop to control entire program
while run_again == "yes":
    #Get input from user
    userNum = int(input("Enter an integer: "))
    #Determine if number is positive
    if userNum >= 0:
        #print multiplication table
        for num in range(1,13):
            print(f"{userNum} * {num} = {userNum*num}")
    else:
        print("program does not handle negative numbers")
    run_again = input("Would you like to run the program again?").lower()

#Loop breaks
print("Exiting program")
