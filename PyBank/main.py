# import dependacies

# os to ensure that the correct operating system is recognised
import os

# csv to enable the reading of csv files
import csv

# Path to collect data from the Resources folder, check by using print(budget_csv)

budget_csv = os.path.join('Resources', 'budget_data.csv')

# declare the variables to track and give them initial values

# total_months initially set to zero then added to as looping through the data to provide the 'Total Months'
month_total = 0

# the total value starts at zero and will be added to when looping through the data to provide the 'Total'
total = 0

# we calulate the 'Average Change' by dividing the Total sum(PL_change) by the number of changes len(PL_change)

# prev_PL to facilitate calculation of the change in profit/loss each month
prev_PL = 0

# This list starts empty and then as we loop through the data it is appened with the month_change
month_change = []

# This list also starts empty and then as we loop through the data it is appened PL_change associated with the month_change
PL_change = []

# This array has two elements, the first captures the month_change (currenty empty) and the secound the PL_change (set at zero) which enables us to calculate which month_change has the greatest increase 
greatest_increase = ["", 0]

# This array also has two elements, the first captures the month_change (currenty empty) and the secound the PL_change (set at a number greater than the maximum PL_change) 
# checked by print(max(PL_change)) subsequently removed, this enables us to calculate which month_change has the greatest decrease

greatest_decrease = ["", 2000000]

# read the csv file and create a list of dictionarys

with open(budget_csv) as PL_data:
    reader = csv.reader(PL_data)

    # Read the header row, store as variable called header. use print(header) to check
    header = next(reader)

    # Remove the first row from the loop 
    first_row = next(reader)

    # add 1 to month_total
    month_total += 1

    # cast as intergers
    total += int(first_row[1])
    prev_PL = int(first_row[1])



    for row in reader:

#       record the total profit/loss for each row        
        month_total += 1
        total += int(row[1])


#       record the change in profit/loss for each row compared to the perevious row
        net_change = int(row[1]) - prev_PL
        prev_PL = int(row[1])
        PL_change += [net_change]
        month_change += [row[0]]

#       calculate the greatest increase in profit/loss 
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

#       calculate the greatest decrease in profit/loss 
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#  calculate the average change in profit/loss by dividing the total change by the number of changes
average_change = sum(PL_change) / len(PL_change)

# print the output summary as individual lines to check output whilst building the code with the correct formatting then..

# print("Financial Analysis")
# print("-------------------------")
# print(f'Total: {month_total}')
# print(f'Total: ${total}')
# print(f'Average Change: ${average_change:.2f}')
# print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
# print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

#  create a variable for the output adding \n to create a new line

summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(summary) 

# Path to output data to the analysis folder
output_txt = os.path.join("analysis", "PyBank_analysis.txt")

#  export the output to csv

with open(output_txt, "w") as txt_file:
    txt_file.write(summary)

