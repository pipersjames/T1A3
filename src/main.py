import sys
import functions


def menu_selection():


    open_message = "Welcome to the Stocktake App, Please choose what you would like to do from the list of options;"

    stocktake_selection = []
    count = []

    menu_options = {
        "L": functions.location_to_location,
        "C": functions.cycle_code,
        "P": functions.print_count_sheet,
        "I": functions.input_counts,
        "R": functions.generate_variance_report,
        "F": functions.confirm_and_commit_changes,
    }

    while True:
        print(f"""
    {open_message}

        1. Select Cycle counting method;
            \u2022 Location to Location (L)
            \u2022 Cycle Code (C)
        2. Print Count Sheet (P)
        3. Input Counts (I)
        4. Generate Variance Report (R)
        5. Confirm and Commit Changes (F)
        6. Exit the Program (E)
    """)
        
        open_message = "What would you like to do now?"
        choice = input(">").upper()

        if choice == "E":
            break

        elif choice in menu_options:
            if choice == "L":
                stocktake_selection = menu_options[choice]()
            elif choice == "I" or choice == "P":
                if stocktake_selection:
                    count = menu_options[choice](stocktake_selection)
                else:
                    print("No stocktake selection available. Please proceed to select a counting method first")
            elif choice == "R":
                menu_options[choice](stocktake_selection,count)
            else:
                menu_options[choice]()
            
    print("Thank you for using the Stocktake App. Happy counting!")


menu_selection()

