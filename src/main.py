import sys
import functions
#menu for function selection












def menu_selection():
    open_message = "Welcome to the Stocktake App, Please choose what you would like to do from the list of options;"
    menu_options = {
        "L": functions.location_to_location,
        "C": functions.cycle_code,
        "P": functions.print_count_sheet,
        "I": functions.input_counts,
        "R": functions.generate_variance_report,
        "F": functions.confirm_and_commit_changes
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
            action = menu_options[choice]
            action()
            while True: 
                choice = input("Do you want to take another action? (Y/N): ")
                if choice.upper() == "Y":
                    break
                elif choice.upper() == "N":
                    print("Thank you for using the Stocktake App. Happy counting!")
                    exit()
                else:
                    print("Invalid input. Please press Y for yes or N for no")
        else:
            print("Invalid choice. Please try again")
            
    print("Thank you for using the Stocktake App. Happy counting!")


menu_selection()

