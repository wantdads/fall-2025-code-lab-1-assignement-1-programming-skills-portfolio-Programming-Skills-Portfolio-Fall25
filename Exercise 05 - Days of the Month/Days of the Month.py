# program to tell how many days are in a month

# dictionary for months and days
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# ask user for month number
month = int(input("Enter month number (1-12): "))

# check if month is valid
if month in days_in_month:
    # check for leap year if month is February
    if month == 2:
        leap = input("Is it a leap year? (yes or no): ")
        if leap.lower() == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print("This month has", days_in_month[month], "days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
