import menufunctions
import time


def menu_selection():


    open_message = "\033[1;95mWelcome to the Stocktake App, Please choose what you would like to do from the list of options;\033[0m"

    stocktake_selection = []
    count = []

    menu_options = {
        "L": menufunctions.location_to_location,
        "C": menufunctions.cycle_code,
        "S": menufunctions.generate_count_sheet,
        "I": menufunctions.input_counts,
        "R": menufunctions.generate_variance_report,
        "F": menufunctions.confirm_and_commit_changes,
    }

    while True:
        print(f"""
{open_message}

    1. Select stocktaking method and define range;
        \u2022 Location to Location (L)
        \u2022 Cycle Code (C)
    2. Generate Count Sheet (S)
    3. Input Counts (I)
    4. Generate Variance Report (R)
    5. Confirm and Commit Changes (F)
    6. Exit the Program (E)
    """)
        
        open_message = "\033[1;95mWhat would you like to do now?\033[0m"
        choice = input("\033[1mPlease enter the letter corresponding to your menu choice: \033[0m").upper()

        if choice == "E":
            break

        elif choice in menu_options:
            if choice == "L" or choice == "C":
                stocktake_selection = menu_options[choice]()               
            elif choice == "S" or choice == "I":
                if stocktake_selection:
                    count = menu_options[choice](stocktake_selection)
                else:
                    print()
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("No stocktake selection available. Please select a stocktaking method and define a range of values before continuing...")
                    print("----------------------------------------------------------------------------------------------------------------------")
                    time.sleep(1)
            elif choice == "R":
                if count:
                    menu_options[choice](stocktake_selection,count)
                else:
                    print()
                    print("------------------------------------------------------------------------------")
                    print("No user counts have been entered. Please input the counts before continuing...")
                    print("------------------------------------------------------------------------------")
                    time.sleep(1)
            elif choice == "F":
                menu_options[choice](count)
        else:
            open_message = "\033[1;95mPlease choose from the menu below\033[0m"
            print()
            print("----------------------------------")
            print("Invalid Input. Please try again...")
            print("----------------------------------")
            time.sleep(1)

    print()        
    print("\033[1;95mThank you for using the Stocktake App. Happy counting!\033[0m")


menu_selection()

