# A Bonoli
# GitHub Test Comment--Lab 9

#This program aks the user to enter their name
#Then the program displays a menu of options
#Option 1 will display a joke
#Option 2 will display the user's name 15 times
#Option 3 will ask a user to enter a numeber, then display a qoute for that number of times
#Option 4 will ask the user to guess a number between 0 and 100
#Option 5 will convert Fahrenheit to Celsius
#The user will select an option and the program will display output based on the user's selection

#Define funtion to Display Options
def displayOptions():
    print("\n")
    print("GAME MENU")
    print()
    print("++++++++++")
    print()
    print("OPTION 1")
    print("OPTION 2")
    print("OPTION 3")
    print("OPTION 4")
    print("OPTION 5")
    print()
    print("++++++++++")
    print("\n")

#Define function to ask user to play a guessing game and validate whether or not input falls within a set range
def guessingGame(mystery):
    print("\n")
    inputNum = int(input("Guess a whole number between 0 and 100 to win: "))
    print("\n")
    while (inputNum != mystery):
        if (inputNum != mystery) and (inputNum >= 0 and inputNum <= 100):
            if (inputNum > mystery):
                print(inputNum," is greater than the winning number.")
            if (inputNum < mystery):
                print(inputNum," is less than the winning number.")
            inputNum = int(input("Guess another whole number between 0 and 100 to win: "))
            print("\n")
        while (inputNum < 0) or (inputNum > 100):
            inputNum = int(input("Input not in range. Guess a whole number between 0 and 100 to win: "))
            print("\n")
    print("Hurrah!  You guessed the mystery number!")
    print("You escaped the While Loop of Oblivion!...")  
    print("To escape is to win!")
    print("\n")

#Define function to convert Fahrenheit to Celsius
def FahrenheitToCelsius(degreesF):
    degreesC = 5/9*(degreesF - 32)
    return degreesC

#Define function to handle Option slection
def playOption(number):
    if (number == 1):
        print("\n")
        print("Knock, knock..")
        print("Who's there?")
        print("Cash")
        print("Cash who?")
        print("No, thank you. I like almonds.")
        print("\n")
    if (number == 2):
        print("\n")
        for i in range(15):
            print(userName)
        print("\n")
    if (number == 3):
        print("\n")
        iteration = int(input("Enter a number and you will get a surprise: "))
        print("\n")
        for k in range(iteration):
            print("Wherever you go, there you are...")
        print("\n")
    if (number == 4):
        guessingGame(mysteryNum)
    if (number == 5):
        print("\n")
        tempInput = float(input("Enter the temperature in degrees Fahrenheit: "))
        celsius = FahrenheitToCelsius(tempInput)
        print("\n")
        print(tempInput," degrees Fahrenheit is ",celsius," degrees Celsius.")
        print("\n")

#MAIN PROGRAM
#Initialize Variables
isGameOn = 1
mysteryNum = 68

#Input user's name
userName = input("Enter your name: ")

userInput = input("Would you like to play a game? (Type Y or N): ")

if (userInput == "N") or (userInput == "n"):
    isGameOn = 0
else:
    isGameOn = 1
    print()
    print("Hi",userName,". Welcome to the Game!")

#Display menu and allow user to select a menu option--user enters N or n to quit
while (isGameOn == 1):
    displayOptions()
    optionNumber = int(input("Select an option number from the menu: "))
    playOption(optionNumber)
    userInput = input("Would you like to play again? (Type Y or N): ")
    if (userInput == "N") or (userInput == "n"):
        isGameOn = 0
    else:
        isGameOn = 1
print("\n")
print("Thank you,",userName,". See you next time.")
print("\n")

