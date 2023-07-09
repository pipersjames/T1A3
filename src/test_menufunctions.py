from menufunctions import generate_count_sheet
from tabulate import tabulate



#Test if the count sheet is produced in the correct format and fields names
def test_create_count_sheet():
    selection_data = [
        {"stockcode": "ULRR1", "description": "ultra light red rope", "location": "A1", "units": 5, "costperunit": 20, "cyclecode": "A"},
        {"stockcode": "SLRR1", "description": "super light red rope", "location": "A2", "units": 5, "costperunit": 15, "cyclecode": "A"},
        {"stockcode": "RLRR1", "description": "regular light red rope", "location": "A3", "units": 14, "costperunit": 10, "cyclecode": "B"}
    ]
    generate_count_sheet(selection_data)
    expected_output = tabulate([
            {"stockcode": "ULRR1", "description": "ultra light red rope", "location": "A1", "count": " "},
            {"stockcode": "SLRR1", "description": "super light red rope", "location": "A2", "count": " "},
            {"stockcode": "RLRR1", "description": "regular light red rope", "location": "A3", "count": " "}
        ],
        headers="keys",
        tablefmt="grid"
    )
    with open("count_sheet.txt", "r") as file:
        actual_output = file.read()
    assert actual_output.strip() == expected_output.strip()