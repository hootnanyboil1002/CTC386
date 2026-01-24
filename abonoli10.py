# A Bonoli
# Lab 10

#This program asks the user to enter their name
#Then the program displays a menu of options
#Option 1 will display a joke
#Option 2 will display the user's name 15 times
#Option 3 will ask a user to enter a numeber, then display a qoute for that number of times
#Option 4 will ask the user to guess a number between 0 and 100
#Option 5 will convert Fahrenheit to Celsius
#Option 6 will display a series of puzzles to solve in an escape room
#The "TWO UV PAIRS" puzzle is from the British Intelligence Agency's 2025 Christmas Puzzler
#The Three Screens Puzzle is based upon a puzzle in the Illustative Mathematics 6th grade curriculum
#The user will select an option and the program will display output based on the user's selection

#IMPORT MODULE(S)
import random

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
    print("OPTION 6: Trapped at CGHQ")
    print()
    print("++++++++++")
    print("\n")

#Define function to display the puzzle exposition
def cryptoIntro():
    print("\n")
    print("You are locked inside the headquarters of British Intelligence...")
    print("There is no one else in the building...")
    print("There is an exit door, but to open it you need to input an alphanumeric code...")
    print("\n")
    print("On the floor, there is a scrap of paper with 0123456789 written on it...")
    print("On the wall, you see the following three signs...")

#Define function to display success message
def successMessage():
    print("\n")
    print("Congratulations, you have retrieved part of the code!...BUT...")
    print("There is more to do...")
    print("\n")

#Define function to display the puzzle menu
def puzzleDisplay():

    #Initialize variables
    unlockMessage = "XXXXXXX"
    alarm = 0
    isLMR = 0
    isL = 0
    isM = 0
    isR = 0

    while (isLMR == 0) and (alarm == 0):
        print("\n")
        print("========================   ++++++++++++++++++   ========================")
        print("=                      =   +                +   =                      =")
        print("=     TWO UV PAIRS     =   +                +   =                      =")
        print("=                      =   +      PLAY      +   =         SOLVE        =")
        print("=   UV + UV + V = VAR  =   + ODDS and EVENS +   =         A            =")
        print("=    R x P x P = AIR   =   +                +   =         RIDDLE       =")
        print("=     SO + SO = VOW    =   +                +   =                      =")
        print("=                      =   +                +   =                      =")
        print("========================   ++++++++++++++++++   ========================")
        print()
        print("          L                        M                        R           ")
        print("\n")
        gamesAfoot=input("Type L, M, or R to assemble the code: ")
        if (gamesAfoot == "L") or (gamesAfoot == "l"):
            unlockMessage = twoPairs()
            if (unlockMessage == "VARIOUS"):
                isL = 1
            else:
                isL = 0
        elif (gamesAfoot == "M") or (gamesAfoot == "m"):
            isM = 1
            alarm = oddsEvens()
        elif (gamesAfoot == "R") or (gamesAfoot == "r"):
            isR = 1
            alarm = logicPuzzle()
        else:
            alarm = 1
            print("INVALID INPUT")
        if (isL == 1) and (isM == 1) and (isR == 1):
            isLMR = 1
        else:
            isLMR = 0

    if (alarm == 0) and (isLMR == 1):       
        unlockCode = input("To unlock the exit door, type LMR: ")
        if (unlockCode == "VARIOUSANDSUNDRY"):
            print("\n")
            print("The exit door is UNLOCKED...You are free to leave")
            print("\n")
        else:
            print("ALARM HAS SOUNDED...SECURITY WILL ARRIVE SHORTLY...GAME OVER")
            print("\n")
    else:
        print("ALARM HAS SOUNDED...SECURITY WILL ARRIVE SHORTLY...GAME OVER")
        print("\n")

#Define the function to display the TWO UV PAIRS puzzle
def twoPairsDisplay():
    print("\n")
    print("Use the information on the left screen to answer the question on the right screen:")
    print("\n")
    print("========================   ========================")
    print("=                      =   =                      =")
    print("=     TWO UV PAIRS     =   =                      =")
    print("=                      =   =                      =")
    print("=   UV + UV + V = VAR  =   =   WHAT IS 1234567    =")
    print("=    R x P x P = AIR   =   =                      =")
    print("=     SO + SO = VOW    =   =                      =")
    print("=                      =   =                      =")
    print("========================   ========================")
    print("\n")

#Define the function to process the TWO UV PAIRS puzzle
def twoPairs():
    #Initialize local variables
    isSolutionReady = 0
    allCapsCode = "XXXXXXX"
    #while loop to display puzzle with hints until player is ready to solve
    while (isSolutionReady == 0):
        twoPairsDisplay()
        twoPairsInput = input("Type C if you are ready to solve the puzzle. Type H if you need a hint: ")
        if (twoPairsInput == "C") or (twoPairsInput == "c"):
            twoPairsCode = input("Type 1234567: ")
            allCapsCode = twoPairsCode.upper()
            isSolutionReady = 1
        elif (twoPairsInput == "H") or (twoPairsInput == "h"):
            print("\n")
            print("You get two hints, and two hints ONLY...")
            print("\n")
            hintInput = int(input("Enter 1 for hint number 1; Enter 2 for hint number 2: "))
            if (hintInput == 1):
                print("Use the scrap of paper with 0123456789 written on it")
                print("\n")
            if (hintInput == 2):
                print("Count the number of letters in TWO UV PAIRS")
                print("\n")
        else:
            isSolutionReady = 1
            print("INVALID INPUT")
            print("\n")
    if (allCapsCode == "VARIOUS"):
        successMessage()
    return allCapsCode

#Define the function to process the results of the logic puzzle
def theRightScreen(integer):
    alarm = 0
    if (integer == 2):
        print("\n")
        print("========================   ++++++++++++++++++   ========================")
        print("=                      =   +                +   =                      =")
        print("=                      =   +                +   =                      =")
        print("=                      =   + The code:      +   =                      =")
        print("=                      =   + SUNDRY         +   =                      =")
        print("=                      =   +                +   =                      =")
        print("=                      =   +                +   =                      =")
        print("=                      =   +                +   =                      =")
        print("========================   ++++++++++++++++++   ========================")
        print("\n")
        pause=input("Type C to Continue or Q to Quit: ")
        if (pause == "C") or (pause == "c"):
            successMessage()
        elif (pause == "Q") or (pause == "q"):
            print("GAME OVER")
            alarm = 1
        else:
            print("Invalid Input...GAME OVER")
            alarm = 1
    else:
        print("\n")
        print("\n")
        print("THE SCREEN HAS RELEASED POISONOUS GAS...You will fall sleep in 3, 2, 1...")
        print("\n")
        alarm = 1
        
    return alarm

#Define function for logic riddle
def logicPuzzle():
    print("\n")
    print("A part of the code is hidden behind one of three screens...")
    print("One of the screens is true; the other two are false")
    print()
    print("Choose carefully...One screen has the code--the other two release poisonous gas")
    print("\n")
    print("========================   ++++++++++++++++++   ========================")
    print("=                      =   +                +   =                      =")
    print("= The code             =   + No code        +   =                      =")
    print("= You seek             =   + Lies behind    +   = The first screen     =")
    print("= Is behind            =   + This screen;   +   = Is FALSE             =")
    print("= This screen...       =   + Look elsewhere +   =                      =")
    print("=                      =   +                +   =                      =")
    print("=                      =   +                +   =                      =")
    print("========================   ++++++++++++++++++   ========================")
    print()
    print("          1                        2                        3           ")
    print("\n")
    userInputRiddle = int(input("Choose the screen that you think reveals the code. Enter 1, 2 or 3: "))
    alarm = theRightScreen(userInputRiddle)

    return alarm


#Define a function to play Odds and Evens
def oddsEvens():
    #Initialize Variables
    sumPoints = 0
    codeList = ["A", "N", "D"]
    alarm = 0
    isEven = -1

    print("\n")
    print("Allow me to explain the rules...")
    print("Before we play, You will play either odd or even.")
    print("Then we will both choose to play either a one or a two.  We will choose at the same time.")
    print("If the sum of the numbers is 2 or 4, even wins; if the sum of the numbers is 3, odd wins")
    print("\n")
    print("We will play three games.")
    print("For every game you win, I will reveal a character of the code in a random order.")
    print("You must then place the characters in the proper order.")
    print("\n")
    print("Let's begin...")
    print("\n")
    for i in range(3):
        userPoint = input("Choose ODD or EVEN...Type D for ODD or E for EVEN: ")
        if (userPoint == "D") or (userPoint == "d"):
            print("OK, you have chosen to play ODD")
            isEven = 0
        elif (userPoint == "E") or (userPoint == "e"):
            print("OK, you have chosen to play EVEN")
            isEven = 1
        else:
            print("Invalid Input.  You lost one chance")
        print()
        if (isEven == 1) or (isEven == 0):    
            print("\n")
            userNumber = int(input("Now, time to play your number...Type 1 or 2: "))
            print("\n")
            computerNumber = random.randrange(1,3)
            print("I played ",computerNumber)
            print("You played ",userNumber)
            print("\n")
            total = userNumber + computerNumber
            if (total == 3) and (isEven == 0):
                sumPoints = sumPoints + 1
                print("You won this round!")
                print("\n")
            elif (total % 2 == 0) and (isEven == 1):
                sumPoints = sumPoints + 1
                print("You won this round!")
                print("\n")
            else:
                print("You lost this round!")
                print("\n")
        else:
            print()
        isEven = -1
    print("You have won ",sumPoints," rounds!...I will reveal ",sumPoints," characters:")
    print("\n")
    if (sumPoints > 0):
            for k in range(1,(sumPoints+1)):
                if (k == 1):
                    print("Character hint = ",codeList[2])
                if (k == 2):
                    print("Character hint = ",codeList[0])
                if (k == 3):
                    print("Character hint = ",codeList[1])
    sumPoints = 0
    print("\n")
    pause=input("Type C to Continue or Q to Quit: ")
    if (pause == "C") or (pause == "c"):
        if (sumPoints > 0):
            successMessage()
        else:
            print()
    elif (pause == "Q") or (pause == "q"):
        print("GAME OVER")
        print("\n")
        alarm = 1
    else:
        print("INVALID INPUT")
        print("\n")
        alarm = 1

    return alarm


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
    if (number == 6):
        cryptoIntro()
        puzzleDisplay()

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

