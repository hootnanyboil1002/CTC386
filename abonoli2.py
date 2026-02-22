# A Bonoli
# Lab 2
# This program converts binary into decimal and decimal into binary


# Define function to convert user input into a list with integer elements
def convertToList(inputString):
    binaryList = []
    binaryList.extend(inputString)
    listLength = len(binaryList)
    for i in range(listLength):
        binaryList[i] = int(binaryList[i])
    return binaryList


# Define function to convert binary digits into a decimal integer
def binaryToDecimal(inputList):
    length = len(inputList)
    total = 0
    for n in range(length):
        placeValue = inputList[n]*2**(length - (n+1))
        total = total + placeValue
    return total

# Define function to convert a decimal number to binary digits
def decimalToBinary(userInput):
    digitList = []
    quotient = userInput
    if (quotient == 0):
        binaryString = "00000000000000000000000000000000"
    else:
        while quotient != 0:
            quotient, remainder = divmod(quotient, 2)
            digitList.insert(0, remainder)
        binaryString = ''.join(str(element) for element in digitList)
    return binaryString


#MAIN PROGRAM

userInput = input("Enter a binary number with any number of binary digits: " )

binaryIntList = convertToList(userInput)

print("The binary number you entered is: ", userInput)
print("The decimal number is: ", binaryToDecimal(binaryIntList))

print("\n")

decimalInput = int(input("Enter a base-10 integer: "))
print("The binary number is: ", decimalToBinary(decimalInput))

