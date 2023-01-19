import csv

import os

csvpath = os.path.join('Resources', 'election_data.csv')


total_votes = 0
candidate_dict = {}
candidate_list = []
# open CSV file, read it, but not the header
with open(csvpath) as input_file:
    content = csv.reader(input_file)
    next(content)
    # Loop through and check each row
    for row in content:
        # print(row)
        total_votes += 1
        availablecandidate_name = row[2]
        if availablecandidate_name not in candidate_list:
            candidate_list.append(availablecandidate_name)
            candidate_dict[availablecandidate_name] = 0
        candidate_dict[availablecandidate_name] += 1

    print("Election Results")


    print("----------------------------") 
    print(f'Total Votes: {total_votes}')

    print("----------------------------")

    print(candidate_dict)

    print("----------------------------")
winner = max(candidate_dict, key=candidate_dict.get)
result = {key: round(value * 100 / total_votes, 3)
          for key, value in candidate_dict.items()}