import csv

def main():
    # dataset of two columns, date and profit/losses

    # declare a csv_list [] to store the csv

    # first, open the file to read over
    # with open("./Resources/budget_data.csv") as file:
        # reader = csv.DictReader(file)
        # or reader = csv.DictReader(file, filednames["header1", "header2"])
            # for row in reader:
                # csv_list.append({"header1": row["header1"], "header2": row["header2"]})

        # TODO
        # Successfully store header row
        
        # iterate over rows to column_length
            # declare
                # month_count
                # net_profit
                # last_month_profit
                # current_month_profit
                # change_from_last_month
                # total_change
                # increase
                # decrease
                # increase_date
                # decrease_date

            # For loop to column_length
                # profit = {"profits/losses" : value}
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
            # total (net_profit)
                # is this just the addition of every column (i.e., net_profit)?
                # or the absolute value of every change?
            # Average change calculation
                # Is this just net_profit/month_count?
                # Or average 

            # pass 
            # return total number of months with month_count++
            # return net total amount in profit/losses over entire time
            # return average of changes in profit/losses over time
            # return greatest increase in profits (date and amount)
            # return greatest decrease in profits (date and amount)

    # TODO
    #ensure the variables are passed correctly to print_output
    months = "TODO"
    total_change = "TODO"
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
    print("Total Months:", months)
    print("Total:", total_change)
    print("Average Change:", avg_change)
    print("Greatest Increase in Profits:", increase)
    print("Greatest Decrease in Profits:", decrease)


main()