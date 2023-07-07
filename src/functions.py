import csv
from tabulate import tabulate

#setup list and stocktake for location to location count
def location_to_location():

    range_value_1 = input("what is the start location: ").upper()
    range_value_2 = input("what is the finish location: ").upper()

    with open("database.csv") as info:
        reader = csv.DictReader(info)
        data = list(reader)



    stocktake_selection = [d for d in data if range_value_1 <= d["location"] <= range_value_2]

    print(f"This is the selection you have chosen: {stocktake_selection}")

    return stocktake_selection



#setup list and stocktake for cycle code count
def cycle_code():
    pass

#generates a count sheet of range of values 
def print_count_sheet(selection_data):

    for i in range(len(selection_data)):
        selection_data[i].pop("units")
        selection_data[i].pop("costperunit")
        selection_data[i].update({"count" : " "}) 

    print(tabulate(selection_data, headers="keys", tablefmt="grid"), file=open("count_sheet.txt", "w"))
    print("-----------------------------------------------------")
    print("The count sheet has been generated as count_sheet.txt")
    print("-----------------------------------------------------")
    

#takes user input for counted items
def input_counts(selection_data):
    count_items = []
    count_input = []
    dict_of_counts = {}

    for row in selection_data:
        count_items.append(row["stockcode"])

    while True:
        count_input.clear()

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
                break
            else:
                print("Invalid selection. Try pressing either Y for yes or N for no")

        if choice.upper() == "Y":
            break

    return dict_of_counts

#creates a variance report saving a copy by the name chosen
def generate_variance_report():
    pass

#confirm variances and updates the database to reflect counts
def confirm_and_commit_changes():
    pass