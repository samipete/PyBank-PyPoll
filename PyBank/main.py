# A Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

# Path to collect data from the resources folder
pyBank_csv = os.path.join("Resources", "budget_data.csv")

# lists to store data from budget csv
dates = []
profits_losses = []

# set total profits/losses, monthly changes, and increase/descrease to zero initially
p_l_total = 0
p_l_changes = 0
max_increase = 0
max_decrease = 0

# set variables;total monthly change current month as str and current and previous profit loss month variables; set to zero
current_month_pl = 0
previous_month_pl = 0
current_date = ""
total_monthly_changes = 0

# Read budget csv file
with open (pyBank_csv, newline = '') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # start the loop for reading and calculating csv data 
    for row in csvreader:
        
        #add dates and profits/losses
        dates.append(row[0]) 
        profits_losses.append(row[1]) 

        # find the total amount of profits/losses
        p_l_total += int(row[1]) 
     
        # create a conditional statement which calculates profit losses
        if len(profits_losses) > 1: 
            current_month_pl = int(profits_losses[len(profits_losses) - 1]) 
            previous_month_pl = int(profits_losses[len(profits_losses) - 2]) 
            current_date = dates[len(dates) - 1]

            # calculate pl change and monthly change
            monthly_change = int(current_month_pl - previous_month_pl) 

            # calculate total monthly changes
            total_monthly_changes += monthly_change

            # Find max increase/decrease using another if statement
            if  (monthly_change < max_decrease):
                max_decrease = monthly_change
                max_decrease_month = current_date
            elif (monthly_change > max_increase):
                 max_increase = monthly_change
                 max_increase_month = current_date

    #find the total number of months included in the data set (from 2010- beginning of 2017)
    months_total = len(dates) 
    # find the average change in profits/losses
    avg_pl_change = round(total_monthly_changes / (months_total - 1), 2)

    
# Format summary for print and output
output = f"""Financial Analysis 
----------------------------------
Total months: {months_total}
Total: ${p_l_total}
Average Change: ${avg_pl_change}
Greatest Increase in Profits: {max_increase_month} (${max_increase})
Greatest Decrease in Profits:  {max_decrease_month} (${max_decrease})
 """    

# path for output
budget_txt = os.path.join('Analysis','pybank_results.txt')
with open(budget_txt, 'w') as txtfile:
    txtwriter = txtfile.writelines(output)

print(output)

