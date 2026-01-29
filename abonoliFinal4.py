#A Bonoli
#Final Question 4

#Define a function that accepts an integer
#The function will then print "Happy New Year!"
#The number of times as the integer argument

#Define function
def happyNewYear(integer):
    for k in range(integer):
        print("Happy New Year!")
    print("\n")

#MAIN PROGRAM
print("\n")
userInput = int(input("Enter a number between 1 and 10: "))
while (userInput < 1) or (userInput > 10):
    userInput = int(input("Input out of range.  Enter a number between 1 and 10: "))
print("\n")
happyNewYear(userInput)
