
#make sure os capability to find csv file is as good as possible:
import csv

import os

csvpath = os.path.join('Resources', 'election_data.csv')



#set initial variables for total votes, Charles,Diana,and Raymon votes, also set proper backets for dictionary&list
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
    # Loop through each row and store candidate votes and sum of total votes
    for row in csvreader:
        # print(row)
        #sum of votes
        total_votes += 1
        #looping though to store candidate votes in based on how often name is listed 
        if row[2] == "Charles Casper Stockham":
            c_votes += 1
        elif row[2] == "Diana DeGette":
            d_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            r_votes += 1

        #calculate percentage of votes
        per_c = (c_votes/total_votes) * 100
        per_d = (d_votes/total_votes) * 100
        per_r = (r_votes/total_votes) * 100


        #start process of calculating max by aking list of whole row with candidates in it
        candidate_names = row[2]
        #loops though candidate names to count the occurence 
        if candidate_names not in candidate_list:
            candidate_list.append(candidate_names)
            
            candidate_dict[candidate_names] = 0
            
            #if same candidate name encountered, add one to the counter next to proper index in dictionary created above
        candidate_dict[candidate_names] += 1

 
#print accoding to the pattern required
    print("Election Results")


    print("----------------------------") 
    print(f'Total Votes: {total_votes}')


    #use round function to truncate percentage numbers by three decimals
    print("----------------------------")
    print(f'Charles Casper Stockham: {round(per_c, 3)}% ({c_votes})')
    print(f'Diana DeGette: {round(per_d, 3)}% ({d_votes})')
    print(f'Raymon Anthony Doane: {round(per_r, 3)}% ({r_votes})')


    print("----------------------------")
    #calculate winner using max function comparing all three value next to their names in the dictionary created above
    winner = max(candidate_dict, key=candidate_dict.get)

    print(f'Winner: {winner}')
    print("----------------------------")      

file = os.path.join('analysis', 'results.txt')

# # Open the file in "write" mode ('w') 
with open(file, 'w') as text:

#    

    import io
    import contextlib

     # This captures the output to terminal

    captured_output = io.StringIO()

    with contextlib.redirect_stdout(captured_output):
        
        #print accoding to the pattern required
        print("Election Results")


        print("----------------------------") 
        print(f'Total Votes: {total_votes}')


        #use round function to truncate percentage numbers by three decimals
        print("----------------------------")
        print(f'Charles Casper Stockham: {round(per_c, 3)}% ({c_votes})')
        print(f'Diana DeGette: {round(per_d, 3)}% ({d_votes})')
        print(f'Raymon Anthony Doane: {round(per_r, 3)}% ({r_votes})')
    

        print("----------------------------")
        #calculate winner using max function comparing all three value next to their names in the dictionary created above
        winner = max(candidate_dict, key=candidate_dict.get)

        print(f'Winner: {winner}')
        print("----------------------------")


    # sets variable from output
    captured_string = captured_output.getvalue()

    #writes captures output to file
    text.write(captured_string)

