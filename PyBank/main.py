import os
import csv

csv_path = r"C:\Users\8saks\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"
output_path = r"C:\Users\8saks\Documents\GitHub\python-challenge\PyBank\Analysis\Analysis.txt"

total_months = 0
net_total = 0
previous_month_profit = None
monthly_changes = []
max_profit_increase = ["", 0]
max_profit_decrease = ["", 0]

with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        current_month_profit = int(row[1])
        net_total += current_month_profit

        if previous_month_profit is not None:
            monthly_change = current_month_profit - previous_month_profit
            monthly_changes.append(monthly_change)

            if monthly_change > max_profit_increase[1]:
                max_profit_increase = [row[0], monthly_change]

            if monthly_change < max_profit_decrease[1]:
                max_profit_decrease = [row[0], monthly_change]

        previous_month_profit = current_month_profit

average_change = sum(monthly_changes) / len(monthly_changes)

results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_profit_increase[0]} (${max_profit_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_profit_decrease[0]} (${max_profit_decrease[1]})\n"
)

print(results)

with open(output_path, "w") as output_file:
    output_file.write(results)
