import csv
from csvfunctions import read_data_from_csv, write_data_to_csv
import pytest

def test_read_data_from_csv(tmp_path):
    # Create a temporary CSV file with sample data
    csv_data = [
        {"stockcode": "ULRR1", "description": "ultra light red rope", "location": "A1", "units": "5", "costperunit": "20", "cyclecode": "A"},
        {"stockcode": "SLRR1", "description": "super light red rope", "location": "A2", "units": "5", "costperunit": "15", "cyclecode": "A"},
        {"stockcode": "RLRR1", "description": "regular light red rope", "location": "A3", "units": "14", "costperunit": "10", "cyclecode": "B"}
    ]
    csv_file = tmp_path / "test.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["stockcode", "description", "location", "units", "costperunit", "cyclecode"])
        writer.writeheader()
        writer.writerows(csv_data)

    result = read_data_from_csv(csv_file)
    assert result == csv_data

def test_write_data_to_csv(tmp_path):
    csv_data = [
        {"stockcode": "ULRR1", "description": "ultra light red rope", "location": "A1", "units": "5", "costperunit": "20", "cyclecode": "A"},
        {"stockcode": "SLRR1", "description": "super light red rope", "location": "A2", "units": "5", "costperunit": "15", "cyclecode": "A"},
        {"stockcode": "RLRR1", "description": "regular light red rope", "location": "A3", "units": "14", "costperunit": "10", "cyclecode": "B"}
    ]
    csv_file = tmp_path / "test.csv"
    fieldnames = ["stockcode", "description", "location", "units", "costperunit", "cyclecode"]

    # Call the function
    write_data_to_csv(csv_file, csv_data, fieldnames)

    # Read the written data from the file and assert its content
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        result = list(reader)
    assert result == csv_data