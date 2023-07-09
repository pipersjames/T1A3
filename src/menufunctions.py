import os
import copy
import time
from csvfunctions import read_data_from_csv, write_data_to_csv
from tabulate import tabulate
from datetime import datetime


database_file = "database.csv"
count_sheet_file = "count_sheet.txt"
variance_report_folder = "variance reports"

#Performs a location-to-location selection prompt for stocktake setup
def location_to_location():
    print()
    range_value_1 = input("what is the start location: ").upper()
    print()
    range_value_2 = input("what is the finish location: ").upper()
    database = read_data_from_csv(database_file)
    stocktake_selection = [d for d in database if range_value_1 <= d["location"] <= range_value_2]
    if stocktake_selection:
        print()
        print(f"This is the selection you have chosen: \n{tabulate(stocktake_selection, headers='keys', tablefmt='grid')}")
        print()
        selection_ok = input("\033[1mOk to continue with the selection? (Y/N): \033[0m")
        print()
        if selection_ok.upper() == "Y":
            return stocktake_selection
        elif selection_ok.upper() == "N":
            print("Selection removed. Returning to Menu...")
            time.sleep(1)
        else:
            print("Invalid Input. Returning to Menu...")
            time.sleep(1)    
    else:
        print()
        print("No data range selected. Returning to Menu...")
        time.sleep(1)    

#Performs a cycle code selection prompt for stocktake setup
def cycle_code():
    print()
    cycle_selection = input("What is the cycle code: ").upper()
    database = read_data_from_csv(database_file)
    stocktake_selection = [d for d in database if cycle_selection == d["cyclecode"]]
    if stocktake_selection:
        print()
        print(f"This is the selection you have chosen: \n{tabulate(stocktake_selection, headers='keys', tablefmt='grid')}")
        print()
        selection_ok = input("\033[1mOk to continue with the selection? (Y/N): \033[0m").upper()
        print()
        if selection_ok == "Y":
            return stocktake_selection
        elif selection_ok == "N":
            print("Selection removed. Returning to Menu...")
            time.sleep(1)
        else:
            print("Invalid Input. Returning to Menu...")
            time.sleep(1) 
    else:
        print()
        print("No data range selected. Returning to Menu...")
        time.sleep(1) 


#generates a count sheet of range of values 
def generate_count_sheet(selection_data):
    data = copy.deepcopy(selection_data)
    for i in range(len(data)):
        data[i].pop("units")
        data[i].pop("costperunit")
        data[i].pop("cyclecode")
        data[i].update({"count" : " "}) 
    print(tabulate(data, headers="keys", tablefmt="grid"), file=open(count_sheet_file, "w"))
    print()
    print("-----------------------------------------------------")
    print(f"The count sheet has been generated as {count_sheet_file}")
    print("-----------------------------------------------------")
    time.sleep(1)

#takes user input for counted items
def input_counts(selection_data):
    while True:
        count = copy.deepcopy(selection_data)
        for item in count:
            print()
            while True:
                try:
                    item["units"] = int(input(f"Please enter the count of item {item['stockcode']} : "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer value.")
        subset_keys = ["stockcode", "units"]
        print()
        print(tabulate([{k: item[k] for k in subset_keys} for item in count], headers="keys", tablefmt="grid"))
        while True:
            print()
            choice = input("\033[1mAre you happy with the quantities shown on screen? (Y/N): \033[0m")
            if choice.upper() == "Y":
                break
            elif choice.upper() == "N":
                break
            else:
                print("\033[1mInvalid selection. Try pressing either Y for yes or N for no\033[0m")
        if choice.upper() == "Y":
            break
    return count

#generates a variance report saving a copy in the variance reports folder
def generate_variance_report(selection_data, count):
    variance_report = []
    for database, changes in zip(selection_data, count):
        stockcode = database["stockcode"]
        description = database["description"]
        units1 = database["units"]
        units2 = changes["units"]
        costperunit = database["costperunit"]
        variance = int(units2) - int(units1)
        totalcost = int(variance) * int(costperunit)
        variance_report.append({"stockcode": stockcode, "description": description, "units_in_database": units1, "count": units2, "variance": variance, "cost_variance": totalcost})
        print()
    show_report = input("\033[1mWould you like to view the report onscreen? (Y/N): \033[0m").upper()
    if show_report == "Y":
        print()
        print(tabulate(variance_report, headers="keys", tablefmt="grid"))
        proceed_next_step = input("Continue? (Y/N): ").upper()
        if proceed_next_step == "N":
            print()
            print("Report generation cancelled, returning to menu...")
            time.sleep(1)
            return
        elif proceed_next_step == "Y":
            pass
        else:
            print()
            print("Invalid input. Report generation cancelled, returning to menu...")
            time.sleep(1)
            return
    elif show_report == "N":
        pass
    else:
        print()
        print("Invalid selection. Report generation cancelled, returing to menu...")
        return
    current_date = datetime.now().strftime("%d-%b-%Y")
    folder_name = variance_report_folder
    file_name = f"variances_{current_date}.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, folder_name)
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path) 
    print()
    print(tabulate(variance_report, headers="keys", tablefmt="grid"), file=open(file_path, "w"))
    print("---------------------------------------------------------------------")
    print(f"The variance report has been generated as {file_name}")
    print("---------------------------------------------------------------------")
    time.sleep(1)
    return variance_report

#confirm variances and updates the database to reflect counts
def confirm_and_commit_changes(count):
    print()
    confirmation = input("\033[1;31mWarning!\033[0m Are you sure you wish to proceed in committing changes to the database? (Y/N): ")
    if confirmation.upper() == "Y":
        changes = copy.deepcopy(count)
        confirmation_file = []
        database = read_data_from_csv(database_file)   
        for item_in_changes in changes:
            item_in_changes_id = item_in_changes["stockcode"]
            for item_in_database in database:
                if item_in_database["stockcode"] == item_in_changes_id:
                    item_in_database.update(item_in_changes)
                    break
        fieldnames = database[0].keys()
        write_data_to_csv(database_file, database, fieldnames)
        print()
        print("----------------------------------------------------------------")
        print("Changes have been commited to the database, returning to menu...")
        print("----------------------------------------------------------------")
        time.sleep(1)
    elif confirmation.upper() == "N":
        print()
        print("No changes have been made, returning to menu...")
        time.sleep(1)
    else:
        print()
        print("Invalid Input. No changes have been made, returning to menu...")
        time.sleep(1)
        

        

        
