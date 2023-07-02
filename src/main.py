import sys
import csv
from tabulate import tabulate
#menu for function selection



#generates a count sheet of range of values
def print_list_of_items():
    with open("database.csv") as info:
    
        reader = csv.DictReader(info)
        data = list(reader)
        for i in range(len(data)):
            data[i].pop("units")
            data[i].pop("costperunit")
            data[i].update({"count" : " "}) 
        print(tabulate(data, headers="keys", tablefmt="grid"), file=open("count_sheet.txt", "a"))

    


print_list_of_items()
