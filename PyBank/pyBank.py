import os
import csv
pybank_csv = os.path.join("..","Resources", "/Users/owner/Bootcamp/GWU-ARL-DATA-PT-12-2019-U-C/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
pathout = os.path.join("Resources", "budget_data_analysis.txt")
months= []
revenue= []
with open(pybank_csv, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    csv_header = next(csvfile)
    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))
total_months = len(months)
greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0
total_revenue_change= 0
for r in range(len(revenue)):
    total_revenue += revenue[r]
    revenue_change = int(revenue[r]) - int(revenue[r-1])
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue_change
        month_greatest_increase= months[r]
    if revenue[r] <= greatest_decrease:
        greatest_decrease = revenue_change
        month_greatest_decrease = months[r]
for r in range(len(revenue)):
    total_revenue_change += int(revenue[r]) - int(revenue[r- 1])
first_loop = (int(revenue[0]) - int(revenue[-1]))
total_revenue_change_adj = total_revenue_change - first_loop
average_revenue_change = round((total_revenue_change_adj)/(total_months-1),2)
output = (f"Financial analysis\n"
f".................................\n"
f"total_months:{total_months}\n"
f"total_Revenue:{total_revenue}\n"
f'greatest_increase: {greatest_increase}\n'
f'month_great_increase: {month_greatest_increase}\n'
f'greatest_decrease: {greatest_decrease}\n'
f"month_greatest_decrease:{month_greatest_decrease}\n"
f'average_revenue_change:{average_revenue_change}')
print (output)
with open(pathout, "w") as txt_file:
    txt_file.write(output)