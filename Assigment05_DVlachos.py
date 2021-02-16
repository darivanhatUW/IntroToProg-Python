# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DVlachos,2.9.2021, Added code to open filed and provide data from remainder of the program.
# DVlachos,2.11.2021, Code is now pulling from text file to the remainder of the program.
# DVlachos,2.11.2021, Changed input 4 to open the file to replace the contents of the table into the file.
# DVlachos,2.15.2021, Add user input, comments, headers
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
strFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

objFile = open(strFile, "r") # open txt file
for row in objFile:
    strData = row.split(", ")
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("YOUR TASK LIST: ")
        print("Task | Priority")
        print("---------------")
        for row in lstTable: # Loop to display all the rows in the table in a particular format
            print(row["Task"] + " | " + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        taskInput = input("Which task would you like to add? ") # Ask the user to input a task
        priorityInput = input("What is its priority? (Choose: high, medium, low) ") # Ask the user to input the priority level
        print("\nHERE'S YOUR NEW TASK LIST:") # Displays the task in the table
        print("Task | Priority")
        print("---------------")
        dicRow = {"Task": taskInput, "Priority": priorityInput.strip()} # Adds the user input in the dictionary
        lstTable.append(dicRow) # Appends the new user input to the table
        for row in lstTable: # Loops through the table, per row, to display the data in a particular format
            print(row["Task"] + " | " + row["Priority"])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        lstTable.pop() # Removes the last entry in the table
        print("HERE'S YOUR NEW TASK LIST: ")
        print("Task | Priority")
        print("---------------")
        for row in lstTable: # Displays the items in table in a particular format
            print(row["Task"] + " | " + row["Priority"])
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(strFile, "w") # Opens the "ToDoList.txt" to write into
        print("HERE'S WHAT YOU HAVE SAVED:")
        print("Task | Priority")
        print("---------------")
        for row in lstTable: # Adds items from table to text file
            objFile.write(row["Task"] + ", " + row["Priority"] + "\n")
            print(row["Task"] + " | " + row["Priority"])
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Thank you for using Task List. See you back soon!")
        break  # and Exit the program

objFile.close()