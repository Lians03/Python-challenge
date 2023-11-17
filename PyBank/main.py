import csv

def average(list_of_nums):
    sum = 0 
    for num in list_of_nums: 
        sum += num 
    return sum / len(list_of_nums)

csv_path = r'Starter_Code\PyBank\Resources\budget_data.csv'
with open(csv_path, 'r', newline='', encoding='utf-8') as file:
    datafile = csv.reader(file, delimiter=',')
    header = next(datafile)
    total_months = 0
    net_total = 0
    last_month = 0
    changes = []
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""

    
    for row in datafile:
        total_months += 1
        date = row[0]
        profit_loss = int(row[1])
        net_total += profit_loss

      
        if total_months > 1:
            change = profit_loss - last_month
            changes.append(change)
            
        if change > max_increase:
                max_increase = change
                max_increase_date = date
        elif change < max_decrease:
                max_decrease = change
                max_decrease_date = date

        last_month = profit_loss
        
total_change = sum(changes)
average_change = average(changes)

output_file_path = r'PyBank\analysis.txt'
with open(output_file_path, 'w') as output_file:
        print('Financial Analysis')
        print('----------------------------')
        print(f'Total Months: {total_months}')
        print(f'Total: ${net_total}')
        print(f'Average Change: ${average_change:.2f}')
        print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
        print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

