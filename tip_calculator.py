"""This project provides learning of different data types like float and int.

performs addition, multiplication and division and also rounds of decimals without using round function.
"""

total = float(input("Welcome to the Tip calculator.\n What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? %"))
people = int(input("How many people to split the bill? "))

bill = ((total + total * tip_percent/100) / people)

"""Takes floating point value of any length and rounds off to 2 decimal points."""
print("Each person should pay:""{:.2f}".format(bill))