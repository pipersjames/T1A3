import csv
from tabulate import tabulate
from datetime import datetime
import os
import copy
import time

#setup list and stocktake for location to location count
def location_to_location():

    range_value_1 = input("what is the start location: ").upper()
    range_value_2 = input("what is the finish location: ").upper()

    with open("database.csv") as info:
        reader = csv.DictReader(info)
        data = list(reader)

    stocktake_selection = [d for d in data if range_value_1 <= d["location"] <= range_value_2]

    print(f"This is the selection you have chosen: \n{tabulate(stocktake_selection, headers='keys', tablefmt='grid')}")
    selection_ok = input("Ok to continue? (Y/N): ")
    print()
    if selection_ok.upper() == "Y":
        return stocktake_selection
    elif selection_ok.upper() == "N":
        print("Selection removed. Returning to Menu...")
        time.sleep(1)
    else:
        print("Invalid Input. Returning to Menu...")
        time.sleep(1)        

#setup list and stocktake for cycle code count
def cycle_code():
    
    cycle_selection = input("What is the cycle code: ").upper()

    with open("database.csv") as data:
        reader = csv.DictReader(data)
        database = list(reader)

    stocktake_selection = [d for d in database if cycle_selection == d["cyclecode"]]

    print(f"This is the selection you have chosen: \n{tabulate(stocktake_selection, headers='keys', tablefmt='grid')}")
    selection_ok = input("Ok to continue? (Y/N): ")
    print()
    if selection_ok.upper() == "Y":
        return stocktake_selection
    elif selection_ok.upper() == "N":
        print("Selection removed. Returning to Menu...")
        time.sleep(1)
    else:
        print("Invalid Input. Returning to Menu...")
        time.sleep(1) 

#generates a count sheet of range of values 
def print_count_sheet(selection_data):

    data = copy.deepcopy(selection_data)

    for i in range(len(data)):
        data[i].pop("units")
        data[i].pop("costperunit")
        data[i].update({"count" : " "}) 

    print(tabulate(data, headers="keys", tablefmt="grid"), file=open("count_sheet.txt", "w"))
    print("-----------------------------------------------------")
    print("The count sheet has been generated as count_sheet.txt")
    print("-----------------------------------------------------")

#takes user input for counted items
def input_counts(selection_data):
    while True:
        count = copy.deepcopy(selection_data)

        for item in count:
            item["units"] = input(f"Please enter the count of item {item['stockcode']} : ")

        subset_keys = ["stockcode", "units"]
        print(tabulate([{k: item[k] for k in subset_keys} for item in count],
                       headers="keys",
                       tablefmt="grid"))

        while True:
            choice = input("Are you happy with the quantities? (Y/N): ")
            if choice.upper() == "Y":
                break
            elif choice.upper() == "N":
                break
            else:
                print("Invalid selection. Try pressing either Y for yes or N for no")

        if choice.upper() == "Y":
            break
    return count

#creates a variance report saving a copy by the name chosen
def generate_variance_report(selection_data, count):

    variance_report = []
    prepared_changes = []

    for database, changes in zip(selection_data, count):
        stockcode = database["stockcode"]
        description = database["description"]
        location = database["location"]
        units1 = database["units"]
        units2 = changes["units"]
        costperunit = database["costperunit"]
        variance = int(units2) - int(units1)
        totalcost = int(variance) * int(costperunit)
        variance_report.append({"stockcode": stockcode, "description": description, "units_in_database": units1, "count": units2, "variance": variance, "cost_difference": totalcost})

    current_date = datetime.now().strftime("%d-%b-%Y")
    folder_name = "variance reports"
    file_name = f"variances_{current_date}.txt"

    script_dir = os.path.dirname(os.path.abspath(__file__))

    folder_path = os.path.join(script_dir, folder_name)
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path) 

    print(tabulate(variance_report, headers="keys", tablefmt="grid"), file=open(file_path, "w"))
    print("---------------------------------------------------------------------")
    print(f"The variance report has been generated as {file_name}")
    print("---------------------------------------------------------------------")
    
    return variance_report

#confirm variances and updates the database to reflect counts
def confirm_and_commit_changes(count):
    
    confirmation = input("Are you sure you wish to proceed in committing changes to the database? (Y/N)")

    if confirmation.upper() == "Y":
        changes = copy.deepcopy(count)
        confirmation_file = []

        with open("database.csv") as info:
            reader = csv.DictReader(info)
            data = list(reader)
            
        for item_in_changes in changes:
            item_in_changes_id = item_in_changes["stockcode"]
            for item_in_database in data:
                if item_in_database["stockcode"] == item_in_changes_id:
                    item_in_database.update(item_in_changes)
                    break
    
        fieldnames = data[0].keys()  

        with open("database.csv", "w", newline="") as info:
            writer = csv.DictWriter(info, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print("Changes have been commited to the database, returning to menu...")
    
    elif confirmation.upper() == "N":
        print("No changes have been made, returning to menu...")
    else:
        print("Invalid Input, returning to menu...")
        

        

        
