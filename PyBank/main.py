# Your task is to create a Python script that analyzes the records to calculate each of the following:
    # Start with importing your Modules
import os
import csv

# We need a path to collect from the Resouces folder.
BudgetData = os.path.join("..", "Resources", "budget_data.csv")

# Read CSV to ensure I was able to pull the data.
with open(BudgetData, "r") as cvsfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader =csv.reader(cvsfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

# Must make an empty set to hold the total months and net total of profits/loses.

    num_months = []
    profit_loses = []
   
    # Read each column of data after the header
    for column in csvreader:
        num_months.append(column[0])
        profit_loses.append(int(column[1]))
   
   # I'm printing the first 5 indexes in my list to check to see if it's accurate
    print(num_months[:5])
    print(profit_loses[:5])

# We have to find the changes in "Profit/Losses" over the entire period, then find the average of those changes in the dataset.
    change_in_profit = []

    for i in range(1, len(profit_loses)):
        change_in_profit.append((int(profit_loses[i]) - int(profit_loses[i-1])))


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    print(change_in_profit[:5])
    averageprofit = (sum(change_in_profit) / len(change_in_profit))
    print(averageprofit)

# The total number of months included in the dataset
    total_months = len(num_months)
    print(total_months)

# The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profit_loses)
    

# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profit_loses)
    

# Next step is to match the greatest increase/decrease with their corresponding months.
# We use the plus 1 at the end since month associated with change is the following month.

greatest_increase_month = change_in_profit.index(max(change_in_profit)) + 3
print(num_months[25])

greatest_decrease_month = change_in_profit.index(min(change_in_profit)) + 3 
print(num_months[44])

# check my answers. If correct, then print we must output the results to a text file.

print("Financial Analysis")
print("---------------------------------------------------------------")
print("Total Months:" " " + str(total_months))
print("Total:" " " + str(sum(profit_loses)))
print("Average Change:" " " + str(averageprofit))
print("Greates Increase in Profits:" " " + str(num_months[25]) + " " "$" + str(greatest_increase))
print("Greates Decrease in Profits:" " " + str(num_months[44]) + " " "$" + str(greatest_decrease))

# We will output the Financial Analysiss on a text file. Don't forget to add \n to ensure you move to the next line.
PyBank_Results_File = os.path.join("analysis", "PyBank_Results.txt")

with open(PyBank_Results_File,"w") as file:
    file = open("PyBank_Results_File", "w")
    file.write("Financial Analysis" + "\n")
    file.write("-------------------------------------------------------------" "\n")
    file.write("Total Months:" " " + str(total_months) + "\n")
    file.write("Total:" " " + "$" + str(sum(profit_loses)) + "\n")
    file.write("Average Change:" " " + "$" + str(averageprofit) + "\n")
    file.write("Greatest Increase in Profits:" + str(greatest_increase_month) + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits:" + str(greatest_decrease_month) + " " + "$" + str(greatest_decrease) + "\n")
    file.close()