import csv

def read_data_from_csv(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def write_data_to_csv(file_path, data, fieldnames):
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)