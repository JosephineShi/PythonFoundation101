# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jia Shi, 8.1.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
newItem = ""
newPriority = ""
exitChoice = ""

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
def menuOption():
    print("Please Choose:")
    print("\t1) Show current data")
    print("\t2) Add a new item")
    print("\t3) Remove an existing item")
    print("\t4) Save Data to File")
    print("\t5) Exit Program")
while (True):
    menuOption()
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The current data is: ")
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("Type a new Task and Priority for your To Do List")
        newTask = str(input("Please enter a new task: "))
        newPriority = str(input("Please enter its priority: "))
        dicRow = {"Task": newTask, "Priority": newPriority}
        lstTable.append(dicRow)
        print(newTask, newPriority, "are Added")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeItem = (input("Type the Task or Priority to remove: "))
        for row in lstTable:
            if row["Task"].lower() == removeItem.lower():
                lstTable.remove(row)
                print(removeItem + " is Removed")
            else: print(removeItem + " is not in the list ")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("The To Do List txt is saved")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        exitChoice = str(input("Do you want to exit? (y or n): "))
        if exitChoice.lower() == "y":
            print("Exited")
            break
        elif exitChoice.lower() == "n":
            print("Continue")
            continue

