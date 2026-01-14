import os

def Print_Title():
    print("=" * 30)
    print("Log File Analyser")
    print("=" * 30)

def Display_Menu():
    print("\n1. Load log file")
    print("2. Show total log entries")
    print("3. Show log level breakdown")
    print("4. Exit")

def Get_Option(min_option, max_option):
    while True:
        choice = input(f"\nEnter an option ({min_option}-{max_option}): ").strip()
        if not choice:
            print(f"Please enter a number between {min_option} and {max_option}.")
            continue

        try:
            option = int(choice)
        except ValueError:
            print(f"Invalid input. Enter a number between {min_option} and {max_option}.")
            continue

        if option < min_option or option > max_option:
            print(f"Invalid option. Choose a number between {min_option} and {max_option}.")
            continue

        return option

def Load_Log_File():
    fileFound = False
    while not fileFound:
        path = input("\nEnter file path: ")
        if not path:
            print("Path connot be empty")
        elif not os.path.isfile(path):
            print("File not found")
        else:
            print("File loaded")
            fileFound = True

running = True
while running:
    Print_Title()
    Display_Menu()
    option = Get_Option(1, 4)
    if option == 1:
        Load_Log_File()
    elif option == 2:
        print("Feature not yet implemented")
    elif option == 3:
        print("Feature not yet implemented")
    else:
        running = False