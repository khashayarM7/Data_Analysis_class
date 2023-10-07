import pandas as pd
from persiantools.jdatetime import JalaliDate

# read csv file via pandas
BTC = pd.read_csv("/Users/khashayar/Desktop/Data Analysis/DA 03/BTC-USD.csv")

# turn date column from object to datetime style via pandas
BTC["Date"] = pd.to_datetime(BTC["Date"])

# make new column and put days number in that
BTC["PersianWeekDay"] = BTC["Date"].apply(lambda d: JalaliDate(d).isoweekday())

print("Note: BTC-USD time from 2020-01-01 to 2023-09-30\n ")

try:
    # Get a number between 1 and 7 from the user
    day = int(input("Enter a number between 1 and 7: "))

    # Check if the user input is within the desired range
    assert 1 <= day <= 7

    # Filter the DataFrame based on the user's input
    days = BTC[BTC["PersianWeekDay"] == day]

    # Display the matching row(s)
    print(days if not days.empty else "No matching row found for the given number.")

# print this error with wrong number or input str
except (ValueError, AssertionError):
    print("Please enter a valid number between 1 and 7.")
