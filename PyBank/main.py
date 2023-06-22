import csv
import sys


def main():
    # declare an empty list [] to store the csv
    list = []

    # first, open the file to read over
    with open("./Resources/budget_data.csv") as file:
        reader = csv.DictReader(file)
        # TODO Successfully store header row - Why?
        # this append loop will successfully re-write the headers anyway
        # maybe that's all they mean in the instructions?
        header = reader.fieldnames
        # store csv file in list
        for row in reader:
            list.append(row)

    # call function to iterate over list and extract results
    do_stuff(list)


# finds requested data
def do_stuff(data):
    # declare variables
    month_count = 0
    net_profit = 0
    change = 0
    increase = 0
    decrease = 0

    for dict in data:
        # grab values for current row
        # has to be a better way to reference these, by the header value
        monthly_profit = int(list(dict.values())[1])
        date = str(list(dict.values())[0])

        # updates net_profit
        net_profit = net_profit + monthly_profit

        # sets some initial variables
        if month_count == 0:
            last_month = monthly_profit
            total_change = 0
            month_count += 1
        else:
            # computes change in profit between the current_month and the last_month
            current_month = monthly_profit
            change = current_month - last_month
            last_month = monthly_profit
            # updates total_change and month_count
            total_change = total_change + change
            month_count += 1

        # compares change with increase or decrease, updates if a more extreme value is found
        if change > increase:
            increase = change
            increase_date = date
        if change < decrease:
            decrease = change
            decrease_date = date

    # calculates average of changes in profit/losses over time
    # month_count-1, as the first month had no change to add to total_change
    average = total_change / (month_count - 1)

    # call function to print results to terminal
    months = month_count
    total_change = net_profit
    avg_change = f"{average:.2f}"
    increase = f"{increase_date} (${increase})"
    decrease = f"{decrease_date} (${decrease})"
    print_output(months, total_change, avg_change, increase, decrease)

    # export results to text file by diverting terminal std output
    # first save the original stdout
    original_stdout = sys.stdout

    # Open a file for writing
    with open("./analysis/output.txt", "w") as file:
        # Redirect the stdout to the file
        sys.stdout = file
        print_output(months, total_change, avg_change, increase, decrease)

    # Restore the original stdout
    sys.stdout = original_stdout


# prints everything to terminal
def print_output(months, total_change, avg_change, increase, decrease):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_change}")
    print(f"Average Change: ${avg_change}")
    print("Greatest Increase in Profits:", increase)
    print("Greatest Decrease in Profits:", decrease)


main()
