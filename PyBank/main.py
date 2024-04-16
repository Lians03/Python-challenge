import csv
from pathlib import Path

csv_path = Path("PyBank/Resources/budget_data.csv")


dates = []
profits_losses = []
total_net = 0
total_changes = []
net_change = 0
average_change = 0
profit_increase = 0
increase_index = 0
profit_decrease = 0
decrease_index = 0

with open(csv_path) as bankcsv:
    bankreader = csv.reader(bankcsv) 
    header = next(bankreader)

    for row in bankreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

   
    months = len(dates)
    total_net = sum(profits_losses)

   
    for i in range(1, len(profits_losses)):
        total_changes.append(profits_losses[i] - profits_losses[i-1])
        
    net_change = sum(total_changes)
    average_change = round((net_change / len(total_changes)), 2)

    profit_increase = max(total_changes)
    increase_index = total_changes.index(profit_increase) + 1
    
    profit_decrease = min(total_changes)
    decrease_index = total_changes.index(profit_decrease) + 1

analysis = {
    "Total Months": months,
    "Total": f"${total_net}",
    "Average Change": f"${average_change}",
    "Greatest Increase in Profits": f"{dates[increase_index]} (${profit_increase})",
    "Greatest Decrease in Profits": f"{dates[decrease_index]} (${profit_decrease})",
}


print("Financial Analysis\n")
print("-" * 30)

for key, value in analysis.items():
    print(f"{key}: {value} \n")

output_dir = Path("PyBank")
output_dir.mkdir(parents=True, exist_ok=True)

output_filepath = output_dir / "budget_data_analysis.txt"

with open(output_filepath, "w") as writer:
    writer.writelines("Financial Analysis\n")
    writer.writelines("-" * 30 + "\n")
   
    for key, value in analysis.items():
        writer.writelines(f"{key}: {value} \n")
