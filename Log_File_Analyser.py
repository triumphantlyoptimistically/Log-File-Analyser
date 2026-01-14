import filecmp
from logging import info
import os
from pydoc import text

def Print_Title():
    print("=" * 30)
    print("Log File Analyser")
    print("=" * 30)

def Display_Menu():
    print("\n1. Load log file")
    print("2. Show total log entries")
    print("3. Exit")

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
            print("\nFile loaded\n")
            return path


def Read_Log_File(path):
    valid_entries = 0
    info_entries = 0
    warning_entries = 0
    error_entries = 0
    fatal_entries = 0

    with open(path, "r", encoding="utf-8") as text_file:
        for line in text_file:
            line = line.strip()
            if not line:
                continue
            entryData = line.split(" ")
            if len(entryData) < 4:
                continue
            level = entryData[3]
            match level:
                case "[INFO]":
                    valid_entries = valid_entries + 1
                    info_entries = info_entries + 1
                case "[WARN]":
                    valid_entries = valid_entries + 1
                    warning_entries = warning_entries + 1
                case "[ERROR]":
                    valid_entries = valid_entries + 1
                    error_entries = error_entries + 1
                case "[FATAL]":
                    valid_entries = valid_entries + 1
                    fatal_entries = fatal_entries + 1
    overallData = [valid_entries, info_entries, warning_entries, error_entries, fatal_entries]
    return overallData


def Display_Entry_Data(data):
    print(f"\nTotal lines processed: {data[0]}")
    print(f"Info entries: {data[1]}")
    print(f"Warning entries: {data[2]}")
    print(f"Error entries: {data[3]}")
    print(f"Fatal entries: {data[4]}\n")


running = True
while running:
    Print_Title()
    Display_Menu()
    option = Get_Option(1, 3)
    if option == 1:
        path = Load_Log_File()
    elif option == 2:
        entryData = Read_Log_File(path)
        Display_Entry_Data(entryData)
    else:
        running = False