import csv

def main(): 
    data = csv.DictReader(open('./Resources/election_data.csv'))
    my_report = open('./analysis/analysis.txt', 'w')

    # declare variables
    votes = 0

    for row in data:
        votes += 1




    output=f'''
    Election Results
    -------------------------
    Total Votes: {votes}
    -------------------------
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    -------------------------
    Winner: Diana DeGette
    -------------------------
    '''

    print(output)

    my_report.write(output)

# returns results of data processing  

    # return total number of votes
        # simple counter that increases with each row
    # return complete list of candidates
        # use a set? TODO - 
        # or check for a new name every time, then append to a list of {candidate : votes}?
    # percentage of votes each candidate won
        # create a ticker for each candidate using the list of candidates
        # if candidate gets vote
            # {candidate : votes}++
        # {candidate : votes} / total votes
    # total votes each candidate won
        # {candidate : votes}
    # winner of the election
        # iterate over list of candidates
            # winner = 0
            # if {candidate : votes} > winner
                # winner = {candidate : name}

    # print out to terminal
    # save results in text file

if __name__ == "__main__":
    main()
