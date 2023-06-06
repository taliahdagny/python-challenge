import csv
import os

input_path = "Resources/election_data.csv"
output_path = "Analysis/election_analysis.txt"

numbervotes = 0
candidates = []
candidate_list = []
percentagevoteswon = 0
totalvoteswon = {}
winner = [""]

with open (input_path) as file: 
    reader = csv.reader(file)
    
    header = next(reader)
    firstrow = next(reader)
    numbervotes = 1
    
    for row in reader:
        numbervotes = numbervotes + 1
        candidatelist2 = str(row[2])
        #print(row[2])
        if candidatelist2 not in candidate_list:
            candidate_list.append(candidates)
       # print(candidate_list)  
    percentagevoteswon[candidates] = percentagevoteswon[candidates] + 1
    
    print(totalvoteswon)
    


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