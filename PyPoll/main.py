import csv

import os

csvpath = os.path.join('Resources', 'election_data.csv')


total_votes = 0
c_votes = 0
d_votes = 0
r_votes = 0
candidate_dict = {}
candidate_list = []
# open CSV file, read it, but not the header
with open(csvpath) as file:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csv_header = next(csvreader)
    # Loop through each row
    for row in csvreader:
        # print(row)
        total_votes += 1

        if row[2] == "Charles Casper Stockham":
            c_votes += 1
        elif row[2] == "Diana DeGette":
            d_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            r_votes += 1

        per_c = (c_votes/total_votes) * 100
        per_d = (d_votes/total_votes) * 100
        per_r = (r_votes/total_votes) * 100

        availablecandidate_name = row[2]

        if availablecandidate_name not in candidate_list:
            candidate_list.append(availablecandidate_name)
            candidate_dict[availablecandidate_name] = 0
        candidate_dict[availablecandidate_name] += 1

    print("Election Results")


    print("----------------------------") 
    print(f'Total Votes: {total_votes}')

    print("----------------------------")
    print(f'Charles Casper Stockham: {per_c:,3f} ({c_votes})')
    print(f'Diana DeGette: {per_d:,3f} ({d_votes})')
    print(f'Raymon Anthony Doane: {per_r:,3f} ({r_votes})')
    print(candidate_dict)

    print("----------------------------")
winner = max(candidate_dict, key=candidate_dict.get)
result = {key: round(value * 100 / total_votes, 3)
          for key, value in candidate_dict.items()}