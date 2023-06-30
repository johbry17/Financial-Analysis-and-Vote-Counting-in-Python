import csv


def main():
    """
    Compare and contrast with PyPoll.
    PyBank's excessive, but was fun to play with.
    PyPoll is sleeker and generally better designed.
    """
    # declare an empty list [] to store the csv
    list = []

    # first, open the file to read over
    with open("./Resources/budget_data.csv") as file:
        reader = csv.DictReader(file)
        # store csv file in list
        for row in reader:
            list.append(row)

    # call function to iterate over list and extract results
    results = do_stuff(list)

    # print output to terminal and save to a file
    print(print_output(*results))
    write_output(print_output(*results))


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
        monthly_profit = int(dict["Profit/Losses"])
        date = dict["Date"]

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
    # month_count-1, accounting for the lack of change during the initial month
    average = total_change / (month_count - 1)

    # call function to print results to terminal
    increase = f"{increase_date} (${increase})"
    decrease = f"{decrease_date} (${decrease})"
    results = [month_count, net_profit, f"{average:.2f}", increase, decrease]
    return results


# prints everything to terminal
def print_output(months, total_change, avg_change, increase, decrease):
    output = f"""Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${total_change}
    Average Change: ${avg_change}
    Greatest Increase in Profits: {increase}
    Greatest Decrease in Profits: {decrease}"""
    return output


# saves print_output function to file
def write_output(output):
    with open("./analysis/output.txt", "w") as file:
        file.write(output)


if __name__ == "__main__":
    main()
