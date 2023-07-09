#Stocktake app - Documentation

This terminal application is designed to aid in stocktaking smaller operations. designed to be lightweight and compatible with excel programs via the use of CSV.

---

### Getting Started

Before we proceed, please note that the application is dependant on a Unix-like operating system (e.g., Linux, macOS) or a compatible shell environment (e.g., Git Bash on Windows).

A database source file with the following headings: stockcode, description, location, units, costperunit, cyclecode is required. ```database.csv``` has been included in this file package in the src directory as a functional example. 

There is also a number of other dependancies that if you choose to do so can be installed manually prior to the running of shell script ```script.sh```. Otherwise the Shell script will attempt to install these automatically.

Dependancies as follows;

* Python3
* pip3
* virtualenv
* tabulate (only in virtual environment)

For testing an additional dependancy is exists, please install pytest by running the following in the command line if you wish to have this functionality:

```
pip3 install pytest
```

---

### Running the Program

1. Open Terminal.

2. Navigate to the /src directory to find the ```script.sh``` file. 

3. Run the below commands in the terminal session:

```
chmod +x script.sh
./script.sh
```

Note: ```chmod +x script.sh``` command is not needed if the file is already excutionable.

---

### Attribution Sources

The following sources were used to help plan and construct the application.

* ChatGPT
* Coder Academy lessions
* Trello.com

---

### GitHub Source Repository

https://github.com/pipersjames/T1A3

---

### Code Style guide and styling convention

The Project attempts to follow the style of PEP 8. some of the basics of this style include:

* 4 spaces per indentation level

```
def input_counts(selection_data):
    while True: 
```

* Imports first in document and on seperate lines

```
import os
import copy
import time
```

For further information on this style see link below:

[PEP8 style guide](https://peps.python.org/pep-0008/)

---

### Features in Application

**A menu**

A list of functions that can be selected by the user. On completion or termination of a task the user will come back to this menu. The application can be terminated from this menu by user input.

**Select a counting method between cyclic or location to location**

This feature allows the user to select either the location or cyclic code data in the CSV to effectively run their stocktake. It will loop over the selection pulling out items that meet the condition set by the user. It set this data into a variable that can be accessed by the other functions in the app. It then provides feedback to the user and confirms if they wish to continue with the selection.

**Generate count sheets**

Takes the data from the counting method selection and tabulates it in an easy to read way providing only essential data. It stores this data into a text file the user can print out and write on.


**Receives user input with respect to counts made**

Let's the user input the manual counts into the program to be accessed by other functions. Asks the user to verify if they are happy with the result by displaying a table output of the entries onscreen. 

**Generates variance reports**

Takes the data from the user input and creates a variance report. This report provides information on the changes in stock level from before and after. It also provides a breakdown of the cost involved in the transaction. The user is given the option to view these variances onscreen prior to writing the report to file. Saves the file in a subfolder called variance reports with today's date for the auditor.

**Make changes to a database from the user Input**

Takes the input from the user and overwrites the data in the database with these changes. Asks for user confirmation before doing so giving a warning message. Won't commit any changes unless the user confirms.


### Plan of Implementation

1. Create a CSV file housing the database of stock related information.

2. **Count sheet** implementation.
    * read data from database
    * store data into variable
    * modify data to show stockcode,description,location and blank column called count
    * put data into fancy table
    * save table in txt for printing
    * advise the user of file creation
    * error handling for no method selection (after implementation of selection method)


3. **Menu** for selection to be implemented in it's own function. data needs to loop to allow selection of multiple functions.
    * List of options with command to call
    * Loop the menu after each selection is complete
    * User input for option selection
    * Option to exit the program and loop
    * Control warnings if data for function not found

4. **Take user input for counts**
    * Create a copy of the selection data to prevent it's modification
    * Create a loop for the user to input
    * Print out each item line by line asking for user input of the count
    * Store the count of the user for each item
    * Show the user the final counts
    * Get user confirmation or return to beginning of loop for re-input
    * Error handling for later calculations

5. **Location to Location**   
    * Take user input for start location and end location
    * Read the database into a list of dictionaries
    * Filter the dictionaires outside of range defined by user
    * Show selection to the user
    * Ask for confirmation
    * Error handling to manage confirmation case and no data selected.

5. **Variance Report**
    * Create empty list
    * Zip the selection and user inputted counts into a single list
    * Find the difference between the counted units and the original selections units
    * Find the total cost of the difference between units
    * Extract elements needed from that list into the previously empty list
    * Tabulate the data
    * Save the data into a text document for auditors. Title must include the date of completion
    * Ask the user if they would like to view the report before committing to saving it.
    * Error handling for input cases.

6. **Confirm and commit Changes**
    * Read the database
    * Make changes to the read, substituting the counts to overwrite
    * Write those changes back to the database
    * Ask the user if they are sure they want to commit the changes to database.
    * Error handling for cases where the user declines or inputs the wrong thing.

7. **Cycle code setup**
    * Ask for user input of a cycle code
    * Read the database
    * Filter the dictionaries that have the cycle code matching the user input
    * Print the chosen selection onscreen
    * Prompt user for confirmation
    * Error handling for option cases and empty selection

8. Review the code looking to apply some DRY principles and make the user interface more visually appealing.



Implementation of the these steps were tracked through the use of Trello. Please follow the link to the [Trellow workspace](https://trello.com/b/iCG15EOb/t1a3). 

Screenshots below shown in order of actualization.




![first screenshot](./docs/first%20screenshot%20of%20planning.JPG)
![second screenshot of Trello board](./docs/second%20screenshot.JPG)
![third screenshot of Trello board](./docs/third%20screenshot.JPG)
![fourth screenshot of Trello board](./docs/fourth%20screenshot.JPG)
![fifth screenshot of Trello board](./docs/fifth%20screenshot.JPG)
![sixth screenshot of Trello board](./docs/sixth%20screenshot.JPG)
![seventh screenshot of Trello board](./docs/seventh%20screenshot.JPG)
![eighth screenshot of Trello board](./docs/eighth%20screenshot.JPG)
