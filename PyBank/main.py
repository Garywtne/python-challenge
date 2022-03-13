
import os
import csv

# Path to collect data from the Resources folder

budget_csv = os.path.join('Resources', 'budget_data.csv')
# print(budget_csv)

# declare the variables to track and give them initial values

month_total = 0
month_change = []
PL_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total = 0


# read the csv file and create a list of dictionarys


with open(budget_csv) as PL_data:
    reader = csv.reader(PL_data)

    # Read the header row
    header = next(reader)

    # print(header)

    # Remove the first row from the loop 
    first_row = next(reader)
    month_total += 1
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

#  print the output summary with the correct formatting 

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

