import csv

def main():

    # declare a csv_list [] to store the csv
    list = []

    # first, open the file to read over
    with open("./Resources/budget_data.csv") as file:
        reader = csv.DictReader(file)
            # TODO Successfully store header row - Why?
            # this append loop will successfully re-write the headers anyway
            # maybe that's all they mean in the instructions?
        header = reader.fieldnames
        for row in reader:
                list.append(row)

    do_stuff(list)


def do_stuff(info):
    
    # declare variables
    month_count = 0
    net_profit = 0
    increase = 0
    decrease = 0
        # last_month_profit
        # current_month_profit
        # change_from_last_month
        # total_change
        # increase
        # decrease
        # increase_date
        # decrease_date

    # For loop to column_length
    for dict in info:
         
         # grab values for current row's cells
         monthly_profit = int(list(dict.values())[1])
         date = str(list(dict.values())[0])

         net_profit = net_profit + monthly_profit
         
         if month_count == 0:
            month_count += 1
         else:
            month_count +=1

         if monthly_profit > increase:
            increase = monthly_profit
            increase_date = date
         if monthly_profit < decrease:
             decrease = monthly_profit
             decrease_date = date
        # date = {"Date" ; value}
        # If month_count != true
            # last_month_profit = profit
            # month_variable = 1
            # net_profit = profit
            # increase = profit
            # decrease = profit
            # increase_date = date
            # decrease_date = date
        # Else
            # month_variable++
            # current_month_profit = profit
            # change_from_last_month = current_month_profit - last_month_profit
            # net_profit = net_profit + profit
            # last_month_profit = profit
            # If profit > increase
                # increase = profit
                # increase_date = date
            # Elif profit < decrease
                # decrease = profit
                # decrease_date = date
    
    # TODO
    # Average change calculation
        # Is this just net_profit/month_count?
        # Or average 

    # pass these values to print_output
    # return average of changes in profit/losses over time
    # return greatest increase in profits (date and amount)
    # return greatest decrease in profits (date and amount)
    print(increase_date)
    print(decrease_date)
    # TODO
    #ensure the variables are passed correctly to print_output
    months = month_count
    total_change = net_profit
    avg_change = "TODO"
    increase = "TODO"
    decrease = "TODO"
    # call function to print results to terminal
    print_output(months, total_change, avg_change, increase, decrease)

    # TODO
    # export results to text file with results
        #open a new file, write results, save to analysis folder

# prints everything to terminal
def print_output(months, total_change, avg_change, increase, decrease):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_change}")
    print("Average Change:", avg_change)
    print("Greatest Increase in Profits:", increase)
    print("Greatest Decrease in Profits:", decrease)


main()