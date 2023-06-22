# csv of "Voter ID", "County", "Candidate"

# open with csv DictReader, read it into a list for working on
    # TODO will i run into a memory problem, reading the entire csv into a list?

# read through list

# return total number of votes
    # simple counter that increases with each row
# return complete list of candidates
    # use a set? TODO
    # or check for a new name every time, then append to a list of {candidate : votes}?
# percentage of votes each candidate won
    # create a ticker for each candidate using the set or list of candidates
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