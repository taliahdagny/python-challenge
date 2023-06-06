import csv
import os

# input_path = "Resources/election_data.csv"
input_path = os.path.join("Resources", "election_data.csv")
output_path = "Analysis/election_analysis.txt"

numbervotes = 0
candidates = []
candidate_list = []
percentagevoteswon = 0
totalvoteswon = {}
winner = [""]

with open (input_path) as file: 
    reader = csv.DictReader(file)
    
    header = next(reader)
    firstrow = next(reader)
    numbervotes += 1
    
    for row in reader:
        numbervotes = number_votes + 1
        candidate_list = row[2]
        if candidates not in candidate_list:
            candidate_list.append(candidates)
            percentagevoteswon[candidates] = 0
       
    percentagevoteswon[candidates] = percentagevoteswon[candidates] + 1
    
    
    


with open(out_path,"w") as txt: 
    output = f"""
Election Results
-------------------------
Total Votes: {numbervotes}
-------------------------
{candidates}: {percentagevoteswon}% ({totalvoteswon})
{candidates}: {percentagevoteswon}% ({totalvoteswon})
{candidates}: {percentagevoteswon}% ({totalvoteswon})
-------------------------
Winner: {winner}
-------------------------
"""
    print(output)
    txt.write(output)