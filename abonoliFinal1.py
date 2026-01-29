#A Abonoli
# Final Qeustion 1

#Display menu
print("\n")
print("OPTION MENU")
print()
print("OPTION 1")
print("OPTION 2")
print("OPTION 3")
print("\n")

userInput = int(input("Enter 1,2, or 3 to select from the Option Menu: "))

#Conditionals to handle option slection
if (userInput == 1):
    print("\n")
    userName = input("Enter your name: ")
    print("\n")
    print("Why did ", userName," cross the road?...")
    print("To get to the other side!")
    print("HAHAHAHAHAHAHAHAHAHAHAHA!")
    print("\n")
elif (userInput == 2):
    for i in range(20):
        print("Gelato")
elif (userInput == 3):
    usernumber = 1.0
    userNumber = float(input("Enter a Number: "))
    while (userNumber != 0):
        userNumber = float(input("Warning: That was not the number I was looking for!  Enter another number: "))
    displayNumber = int(userNumber)
    print("Congratulations! ", displayNumber," is correct number!")
else:
    print("Invalid Input.  Good-bye.")

