import csv
from collections import defaultdict

# Input and output file paths
input_file = "C:\\Users\\8saks\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv"
output_file = "C:\\Users\\8saks\\Documents\\GitHub\\python-challenge\\PyPoll\\Analysis\\Analysis.txt"

# Initialize variables
total_votes = 0
candidates = defaultdict(int)

# Read the input file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidates[row[2]] += 1

# Calculate percentages and find the winner
winner = max(candidates, key=candidates.get)
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Print and save the results
with open(output_file, 'w') as outfile:
    output = f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"
    print(output)
    outfile.write(output)

    for candidate, percentage in percentages.items():
        output = f"{candidate}: {percentage:.3f}% ({candidates[candidate]})\n"
        print(output)
        outfile.write(output)

    output = f"-------------------------\nWinner: {winner}\n-------------------------"
    print(output)
    outfile.write(output)
