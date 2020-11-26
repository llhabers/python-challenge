# Your task is to create a Python script that analyzes the records to calculate each of the following:
    # Start with importing your Modules
import os
import csv

# We need a path to collect from the Resouces folder.
BudgetData = os.path.join("..", "Resources", "budget_data.csv")

# Read CSV to ensure I was able to pull the data.
with open(BudgetData, "r") as cvsfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader =csv.reader(cvsfile, delimiter=",")

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Must make an empty set to hold the total months and net total of profits/loses.

    num_months = []
    profit_loses = []
   
    # Read each row of data after the header
    for row in csvreader:
        num_months.append(row[0])
        profit_loses.append(float(row[1]))

# We have to find the changes in "Profit/Losses" over the entire period, then find the average of those changes in the dataset.
    change_in_profit = []

    for i in range(1, len(profit_loses)):
        change_in_profit.append(float(profit_loses[i]) - float(profit_loses[i-1]))

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    averageprofit = (sum(change_in_profit) / len(change_in_profit))

# The total number of months included in the dataset
    total_months = len(num_months)

# The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(averageprofit)

# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(averageprofit)

# Next step is to match the greatest increase/decrease with their corresponding months.
# We use the plus 1 at the end since month associated with change is the following month.

greatest_increase_month = change_in_profit.index(max(change_in_profit)) + 1

greatest_decrease_month = change_in_profit.index(min(change_in_profit)) + 1 

# check my answers

print("Financial Analysis")
print("---------------------------------------------------------------")
print(total_months)
print(str(sum(profit_loses)))
print(averageprofit)
print(greatest_decrease)
print(greatest_increase)
print("Greates Increase in Profits:" + str(greatest_increase_month) + " " "$" + str(greatest_increase))
print("Greates Decrease in Profits:" + str(greatest_decrease_month) + " " "$" + str(greatest_decrease))