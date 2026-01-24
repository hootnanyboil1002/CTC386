# A Bonoli
# CTC-386-151

# This Program Determines the Letter Grade
# From a Numerical Score Input
# The program allows the user to enter numberical grades
# The user enters -1 to quit the program
# The program stores numerical grades in a linked list
# The program then averages the numerical grades
# The program then outputs the average of the numerical grades and the letter grade

# Define function to convert numerical grade to letter grade
def gradeConverter(score):
    if (score >= 90):
        print (score, " is an A letter grade")
    elif (score >= 80) and (score < 90):
        print (score, " is a B letter grade")
    elif (score >= 70) and (score < 80):
        print (score, " is a C letter grade")
    elif (score >= 60) and (score < 70):
        print (score, " is a D letter grade")
    else:
        print (score, " is a F letter grade") 

# Define function to traverse the linked list and sum the grades
def sumGrades(listInstance):
    tempSum = 0
    nodeTotal = 0
    currentNode = listInstance.head
    while currentNode:
        tempSum = tempSum + currentNode.data
        nodeTotal = nodeTotal + 1
        currentNode = currentNode.next
    return nodeTotal, tempSum

# Create instance of Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#intialize Link List and create instance of class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

gradeList = LinkedList()

# Intialize Variables
rawScore = 0
gradeSum = 0
average = 0

print ("\n")

while(rawScore != -1):
    #User inputs numerical data; program will initially accept all data types
    scoreInitial = input("Enter the numerical test score to the nearest tenth (Enter -1 to quit): ")

    #Data validation using the partition function: analyze tuples for numeric data and proper formatting of negatives 
    inputStr = scoreInitial.partition("-")
    
    if (inputStr[0].isnumeric() == True or inputStr[0].isdecimal() == True) and (inputStr[1] == ''):
        rawScore = float(scoreInitial)
    else:
        if (scoreInitial == "-1"):
            rawScore = float(scoreInitial)    
        else:
            while (scoreInitial != "-1") and (inputStr[0].isnumeric() == False and inputStr[0].isdecimal() == False):
                if (scoreInitial == "-1"):
                    rawScore = float(scoreInitial)
                #If the user enters a positive number, then cast input as float and set input to rawScore
                elif (inputStr[0].isnumeric() == True or inputStr[0].isdecimal() == True) and (inputStr[1] == ''):
                    rawScore = float(scoreInitial)
                #If user enters any input other than a positive number or -1, then user must re-enter input
                else:
                    scoreInitial = input("Input error.  Enter -1 to quit, or enter a positive numeric score: ")
                    inputStr = scoreInitial.partition("-")
            #second while loop to catch malformed negative numbers: e.g., 90-90
            while (inputStr[1] == "-") and (inputStr[0] != ''):
                if (scoreInitial == "-1"):
                    rawScore = float(scoreInitial)
                elif (inputStr[0].isnumeric() == True or inputStr[0].isdecimal() == True) and (inputStr[1] == ''):
                    rawScore = float(scoreInitial)
                else:
                    scoreInitial = input("Input error.  Enter -1 to quit, or enter a positive numeric score: ")
                    inputStr = scoreInitial.partition("-")
            if (scoreInitial == "-1") or (inputStr[0].isnumeric() == True) or (inputStr.isdecimal() == True):        
                rawScore = float(scoreInitial)
            else:
                print("You are trying to break the program...Bye")
                rawScore = -1

    # if rawScore is not -1, then create a new Node and point head of list to new Node (LIFO)
    if (rawScore != -1):
        new_node = Node(rawScore)
        new_node.next = gradeList.head
        gradeList.head = new_node

    print("\n")

    if (rawScore >= 0):
        print("You entered the following numerical score: ", rawScore)
        print("\n")

        gradeConverter(rawScore)

        print("\n")

    else:
        print("You have quit the Grade Converter Program. Here is a summary of the data:")
        print("\n")
        print("These are the scores you have entered:")
        temp = gradeList.head
        while temp:
            print(temp.data, end="")
            temp = temp.next
            print()
        print("\n")

        #Claculate sum from linked list data
        nodes, gradeSum = sumGrades(gradeList)

        if (gradeList.head == None):
            print("You did not enter any numerical scores")
            print("\n")
            print("The program cannot determine the letter grade from the input.")
        else:
            average = gradeSum / nodes
            print("The average of all the scores you have enetered = ",average)
            gradeConverter(average)
        print("\n")
        print("Have a nice day!")
        print("\n")
