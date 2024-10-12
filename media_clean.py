from datetime import datetime

# Two datetime strings
datetime_str1 = "2023-03-20 12:00:00"
datetime_str2 = "2023-03-21 18:30:00"

# Define the format of the datetime strings
datetime_format = "%Y-%m-%d %H:%M:%S"

# Convert the strings to datetime objects
datetime1 = datetime.strptime(datetime_str1, datetime_format)
datetime2 = datetime.strptime(datetime_str2, datetime_format)

# Compare datetime objects
if datetime1 < datetime2:
    print("Datetime1 is earlier than Datetime2.")
elif datetime1 > datetime2:
    print("Datetime1 is later than Datetime2.")
else:
    print("Datetime1 and Datetime2 are the same.")


# photo clean
selection_method = input("Select file selection method\n(d) Date (t) Datetime (n) Number\n")

datetime_format = "%d/%m/%Y %H:%M"
date_format = "%d/%m/%Y"

def range_finder(input_range_str_1, input_range_str_2):
    if input_range_str_1 > input_range_str_2:
        range_str_1 = input_range_str_2 # range_1 being the smaller value
        range_str_2 = input_range_str_1 # range_2 being the larger value
        return range_str_1, range_str_2
    else:
        range_str_1 = input_range_str_1
        range_str_2 = input_range_str_2
        return range_str_1, range_str_2


if selection_method == 'd':
    date_1 = input("\nEnter date 1 (DD/MM/YYYY):   ")
    date_2 = input("Enter date 2 (DD/MM/YYYY):   ")

    range_str_1 = range_finder(date_1, date_2)[0]
    range_str_2 = range_finder(date_1, date_2)[1]

elif selection_method == 't':
    datetime_1 = input("\nEnter datetime 1 (DD/MM/YYYY HH:MM):   ")
    datetime_2 = input("Enter datetime 2 (DD/MM/YYYY HH:MM):   ")

    range_str_1 = range_finder(datetime_1, datetime_2)[0]
    range_str_2 = range_finder(datetime_1, datetime_2)[1]

elif selection_method == "n":
    number_1 = input("\nEnter number 1: ")
    number_2 = input("Enter number 2:  ")

    range_str_1 = range_finder(number_1, number_2)[0]
    range_str_2 = range_finder(number_1, number_2)[1]

else:
    print("\nInvalid selection, enter again.")

print(f"Range 1: {range_str_1}\nRange 2: {range_str_2}")


file_path = input("\nEnter image file path:    ")

while True:
    action = input("\nProcess Selection \n[r] Rename [d] Delete\nEnter letter for process: ")

    confirmation = True
    while confirmation == True:
        if action != "r" and "d":
            print(f"Invalid selection '{action}'")
        elif action == "r":
            print("ph")
            term = "Rename"
        elif action == "d":
            print("ph")
            term = "Delete"