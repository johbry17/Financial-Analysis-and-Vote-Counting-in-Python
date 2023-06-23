import csv


def main():
    # open csv to read, and output file to write to
    data = csv.DictReader(open("./Resources/election_data.csv"))
    results = open("./analysis/analysis.txt", "w")

    # declare variables
    total_votes = 0
    candidates = []
    candidate_votes = []
    percent = []
    most_votes = 0
    winner = 0

    # iterate over row to collect data
    for row in data:
        name = row["Candidate"]

        # collects total votes
        total_votes += 1

        # add new candidate if necessary
        if name not in candidates:
            candidates.append(name)
            candidate_votes.append(int(0))
        if name in candidates:
            # add to vote total for each candidate
            index = candidates.index(name)
            candidate_votes[index] += 1

    # creates a list of each candidate's vote percentage
    for candidate in candidates:
        i = candidates.index(candidate)
        percentage = (candidate_votes[i] / total_votes) * 100
        percent.append(percentage)

    # uses candidate_votes to find winner
    for votes in candidate_votes:
        if votes > most_votes:
            most_votes = votes
            i = candidate_votes.index(votes)
            winner = candidates[i]

    # creates output
    output = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    {candidates[0]}: {percent[0]:.3f}% ({candidate_votes[0]})
    {candidates[1]}: {percent[1]:.3f}% ({candidate_votes[1]})
    {candidates[2]}: {percent[2]:.3f}% ({candidate_votes[2]})
    -------------------------
    Winner: {winner}
    -------------------------
    """

    # print results to terminal
    print(output)

    # writes results and saves to a .txt file
    results.write(output)


main()
