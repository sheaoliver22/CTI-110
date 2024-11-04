#



#Get the number of scores from user
userNum = int(input("Number of scores: "))

print()

#Create score list
validScores = []

#Loop to allow user to enter scores
for scores in range(0, userNum):
    userInput = float(input(f"Enter score #{scores + 1}: "))
    # Use loop to ensure score is between 0 and 100
    while userInput > 100 or userInput < 0:
        print("Score must be between 0 and 100.")
        userInput = float(input(f"Enter score #{scores + 1}: "))
    # add valid inputs to a list
    validScores.append(userInput)


# Done adding grades
print()
print("---" * 10)
print("results:")
print()

#Determine lowest and avg scores
lowestScore = min(validScores)
avgScore = sum(validScores) / len(validScores)
#Print lowest score
print(f"Lowest Score: {lowestScore}")
#Remove lowest score from list then print the list
validScores.remove(lowestScore)
print(f"Modified List: {validScores}")
#Print avg score
print(f"Scores Average: {avgScore}")
#Determine and print letter grade
if avgScore >= 90:
    print("Grade: A")
elif avgScore >= 80:
    print("Grade: B")
elif avgScore >= 70:
    print("Grade: C")
elif avgScore >= 60:
    print("Grade: D")
else:
    print("Grade: F")
