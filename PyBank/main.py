import csv

import os

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []

incomechange = []

change = []




with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


    month_count = 0
    total = 0
    g_inc = 0
    g_dec = 0
    
    for row in csvreader:

        month_count += 1
        total = total + int(row[1])

        months.append(row[0])

        incomechange.append(int(row[1]))

    from itertools import pairwise
    for pair in pairwise(months):
            
       

        for i in range(len(incomechange) -1):
            
            
            change.append(incomechange[i+1] - incomechange[i])  
            import statistics 
        avg_change = statistics.mean(change)
        g_inc = max(change)
        g_dec = min(change)

    print("Financial Analysis")


    print("----------------------------")    
    print(f'Total Months: {month_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${int(avg_change)}')
    print(f'Greatest Increase in Profits: (${g_inc})')
    print(f'Greatest Decrease in Profits: (${g_dec})')

   

# Store the file path associated with the file (note the backslash may be OS specific)
file = os.path.join('analysis', 'results.txt')

# # Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

#     # This stores a reference to a file stream
    print(text)

#     # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)


