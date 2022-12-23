# A Python script that analyzes the votes and calculates each of the following
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

# path to election data
pypoll_csv = os.path.join("Resources","election_data.csv")

# define variables and set intitial values 
candidate_vote_counts = {}
total_votes = 0
winner = ''
max_can_per = 0
candidate_results = ''

# read cvs
with open(pypoll_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    # define a function that calculates votes per candidate
    def add_votes(csvrow):
        candidate = csvrow[2]  
        if candidate in candidate_vote_counts:
            candidate_vote_counts[candidate] += 1
        else :
             candidate_vote_counts[candidate] = 1

    # loop over votes and tally
    for row in csvreader:
        add_votes(row)
        #total votes
        total_votes += 1

    #print(candidate_vote_counts)
    # Format output to print and write to Text file.     
    output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""
    # loop through candidate data and calculate votes per cand
    for candidate_name in candidate_vote_counts:
        percent_per_can = round((candidate_vote_counts[candidate_name] /total_votes) * 100, 2)
        output += f'{candidate_name}: {percent_per_can:.3f}% ({candidate_vote_counts[candidate_name]})\n'

        # if statement that compares voting outcome per canidate a& includes the winner 
        if percent_per_can > max_can_per:
            max_can_per = percent_per_can
            winner = candidate_name
output += f"""-------------------------
Winner: {winner}
-------------------------
"""

# Path to create text file and write output to file.
poll_txt = os.path.join('Analysis', 'election_results.txt') #os.path.join('.','Analysis','election_results.txt')


with open(poll_txt, 'w') as txtfile:
    txtwriter = txtfile.writelines(output)
    
print(output)