import csv
data = csv.DictReader(open('Resources/budget_data.csv'))
my_report = open('analysis/my_report.txt','w')

months = 0
total = 0
total_ch = 0
prev_rev = 0
inc = [0,'']
dec = [0,'']

for row in data:
    months += 1
    rev = int(row['Profit/Losses'])

    change = rev - prev_rev

    if prev_rev == 0:
        change = 0
    
    total += rev
    total_ch += change

    if change > inc[0]:
        inc[0] = change
        inc[1] = row['Date']

    if change < dec[0]:
        dec[0] = change
        dec[1] = row['Date']

    prev_rev = rev
output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[1]} (${inc[0]:,})
Greatest Decrease in Profits: {dec[1]} (${dec[0]:,})
'''

print(output)
my_report.write(output)