import csv

def main():
    # dataset of two columns, date and profit/losses
    # first, open the file to read over
    '''
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file, filednames["header1", "header2"])
            {"header1": value, "header2": value}
            for row in reader:
                do stuff, like:
    '''
        # with open("*.csv") as file:
            #store headers?
            # for line in file:
                # date, profit_or_loss = line.rstrip().split(",")

        # find and declare variable column_length - maybe unnecessary?
        # iterate over rows to column_length
            # month variable++ that returns total number of months
            # return change in profit/losses over entire time
            # return average of changes in profit/losses over time
            # greatest increase in profits (date and amount)
            # greatest decrease in profits (date and amount)

    # print all to terminal
    print_output()
    # export results to text file with results
        #open a new file, write results, save to analysis folder


# prints everything to terminal
#TODO
# add add input for months, total_change, avg_change, increase, decrease
def print_output():
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:")
    print("Total:")
    print("Average Change:")
    print("Greatest Increase in Profits:")
    print("Greatest Decrease in Profits:")


main()