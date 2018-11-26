import os
import csv
import collections

#enjoins the CSV file
election_csv = os.path.join('..', 'PyPoll', 'election_data.csv')

#opens the CSV file in "READ" mode delimiting each line with " "
with open(election_csv, "r", newline="") as csvfile:

    # Return a reader object 'election CSV' and will iterate over lines in csvfile
    csvreader = csv.reader(csvfile, delimiter=",")

    # skips header
    next(csvreader)

    total_votes = 0
    all_candidates = []

    for row in csvreader:
        #add one to every row after header
        total_votes += 1
        #append the entire candidate column into a list
        all_candidates.append(row[2])
    #remove duplicate names to find the true total number of candidates
    filtered_candidates = set(all_candidates)
    # create an empty list for percentages
    vote_percentage_list = []
    # calculates the percentage of votes for each candidate
    # tallies up totals for each candidate
    vote_count_by_candidate = collections.Counter(all_candidates)
    for x in vote_count_by_candidate:
        vote_int = int(vote_count_by_candidate[x])
        vote_percentage = round(vote_int / total_votes * 100,2)
        vote_percentage_list.append(vote_percentage)

    #extracts the candidate name and their respective vote counts into two separate lists
    vote_count_val = []
    vote_candidate_name = []
    for x,y in vote_count_by_candidate.items():
        vote_candidate_name.append(x)
        vote_count_val.append(y)

    #determines the highest vote count, identifies the index of that vote count, and matches that vote count to the list "vote_candidate_name" to find the name of the winner
    max_vote = max(vote_count_val)
    max_vote_index = vote_count_val.index(max_vote)
    winner = str(vote_candidate_name[max_vote_index])

    #prints the candidates in order alongside their vote percentages and vote counts
    def candidate_summary():
        file = open("PyPoll_main_Eric Lieu.txt", "w")
        print(f"Election Results\n----------------------------\nTotal Votes: {total_votes}\n----------------------------")
        file.write(f"Election Results\n----------------------------\nTotal Votes: {total_votes}\n----------------------------\n")
        file.close()
        file = open("PyPoll_main_Eric Lieu.txt", "a")
        for x in range(0, len(filtered_candidates)):
            print(f"{vote_candidate_name[x]}: {vote_percentage_list[x]}% ({vote_count_val[x]})")
            file.write(f"{vote_candidate_name[x]}: {vote_percentage_list[x]}% ({vote_count_val[x]})\n")
        print(f"----------------------------\nWinner: {winner}\n----------------------------")
        file.write(f"----------------------------\nWinner: {winner}\n----------------------------")
    candidate_summary()





