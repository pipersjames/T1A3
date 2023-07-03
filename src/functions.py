import csv
from tabulate import tabulate



#setup list and stocktake for location to location count
def location_to_location():
    pass

#setup list and stocktake for cycle code count
def cycle_code():
    pass

#generates a count sheet of range of values 
def print_count_sheet():
    with open("database.csv") as info:
    
        reader = csv.DictReader(info)
        data = list(reader)
        for i in range(len(data)):
            data[i].pop("units")
            data[i].pop("costperunit")
            data[i].update({"count" : " "}) 
        print(tabulate(data, headers="keys", tablefmt="grid"), file=open("count_sheet.txt", "w"))
        print("-----------------------------------------------------")
        print("The count sheet has been generated as count_sheet.txt")
        print("-----------------------------------------------------")

#takes user input for counted items
def input_counts():
    pass

#creates a variance report saving a copy by the name chosen
def generate_variance_report():
    pass

#confirm variances and updates the database to reflect counts
def confirm_and_commit_changes():
    pass