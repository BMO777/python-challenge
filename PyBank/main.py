import csv

import os

csvpath = os.path.join('Resources', 'budget_data.csv')

#define months, and change variables we will need to loop to make lists
months = []

incomechange = []

change = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

# set initial variables for month count, total, greatest increase& decrease
    month_count = 0
    total = 0
    g_inc = 0
    g_dec = 0
    # use 'for' function to loop though values in csv file
    for row in csvreader:

     #calclate sum of total months   
        month_count += 1

    #calculate total
        total = total + int(row[1])

        months.append(row[0])

        incomechange.append(int(row[1]))

    #something I tried that didnt work:
    #from itertools import pairwise
    #for pair in pairwise(months):           
       
       #loop though column values containing income data

    for i in range(len(incomechange) -1):
        
        #subtract or add one value following another starting from the top and append/wrap values in list called change
        change.append(incomechange[i+1] - incomechange[i])  

    #statistics to calculate mean
    import statistics 
    avg_change = statistics.mean(change)

    #pull greatest increase&decrease by using max&min values looping though list named change
    g_inc = max(change)
    g_dec = min(change)

    #pull greatest increase&decrease months by pairing an index from lists named months&change, though +1 needs to be added to match the data because it takes the 1st value of the pair
    inc_date = months[change.index(g_inc) + 1]
    dec_date = months[change.index(g_dec) + 1]


    # print values required to match assignment

    print("Financial Analysis")


    print("----------------------------")    
    print(f'Total Months: {month_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${int(avg_change)}')
    print(f'Greatest Increase in Profits: {inc_date} (${g_inc})')
    print(f'Greatest Decrease in Profits: {dec_date} (${g_dec})')

   

# Store the file path associated with the file (note the backslash may be OS specific)
file = os.path.join('analysis', 'results.txt')

# # Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

#     # This stores a reference to a file stream
    print(text)

#     # Store all of the text printed to the terminal inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)


