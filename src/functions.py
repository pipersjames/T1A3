import csv
from tabulate import tabulate

dict_of_counts = {}

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
    count_items = []
    count_input = []

    with open("database.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            count_items.append(row["stockcode"])
    
    global dict_of_counts

    while True:
        for i in range(len(count_items)):
            count = input(f"Please enter the count of item {count_items[i]} : ")
            count_input.append(count)

        dict_of_counts = dict(zip(count_items, count_input))
        print(tabulate(dict_of_counts, headers="keys", tablefmt="grid"))

        while True:
            choice = input("Are you happy with the quantities? (Y/N): ")
            if choice.upper() == "Y":
                break
            elif choice.upper() == "N":
                count_input.clear()
                input_counts()
            else:
                print("Invalid selection. Try pressing either Y for yes or N for N")
    
        return dict_of_counts
    
def print_counts():
    print(dict_of_counts)

#creates a variance report saving a copy by the name chosen
def generate_variance_report():
    pass

#confirm variances and updates the database to reflect counts
def confirm_and_commit_changes():
    pass