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

running = True
while running:
    Print_Title()
    Display_Menu()
    if Get_Option(1, 4) == 4:
        running = False