#PyCleaner
#Simple Data Cleaning Tool in PY
# Dev - Ahmed Shaikh
# https://github.com/AhmedShaikh0

from colorama import Fore
import pandas as pd

file = input("Enter your File name: ")
data = pd.read_csv(file)

while True:
    print(Fore.YELLOW,"Options:")
    print("1. Read Data from file")
    print("2. Remove Duplicate Records")
    print("3. Modify Records")
    print("4. Read Top 5 Rows")
    print("5. Read Last 5 Rows")
    print("6. Read Particular Row")
    print("7. Modify Particular Record")
    print("8. Export Cleaned CSV File")
    print("9. Exit Program")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

    if choice == "1":
        data.info()

    elif choice == "2":
        data.drop_duplicates(inplace=True)
        print("Duplicate Records removed Successfully.")

    elif choice == "3":
        column = input("Enter Column name: ")
        incorrect = input("Enter Incorrect Word: ")
        correct = input("Enter Correct Word: ")
        data[column].replace(incorrect, correct, inplace=True)
        print("Data Modified Successfully.")

    elif choice == "4":
        print(data.head())
    
    elif choice == "5":
        print(data.tail())

    elif choice == '6':
        row_num_u = int(input("Enter Row number to Read: "))
        row = data.iloc[row_num_u]
        print(row)
    
    elif choice == '7':

        row_index = int(input("Enter Row number: "))  
        column_name = cn = input("Enter column name: ")  
        new_value = input("Set New Value: ")
        
        data.at[row_index, column_name] = new_value

        print(data)

    elif choice == "8":
        exp_file = input("Enter File Name to Export (Must Include .csv) in End: ")
        data.to_csv(exp_file, index=False)
        print(Fore.YELLOW, exp_file," Successfully Exported.")

    elif choice == '9':
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8/9).")
