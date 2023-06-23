import csv

def main(): 
    data = csv.DictReader(open('./Resources/election_data.csv'))
    my_report = open('./analysis/analysis.txt', 'w')

    # declare variables
    votes = 0
    candidates = []
    candidate_votes = []

    for row in data:
        name = row['Candidate']

        # collects total votes
        votes += 1

        # add new candidate if necessary
        if name not in candidates:
            candidates.append(name)
            candidate_votes.append(int(0))
        if name in candidates:
            # add to vote total for each candidate
            index = candidates.index(name)
            candidate_votes[index] += 1
    
    print(candidates)
    print(candidate_votes)

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
