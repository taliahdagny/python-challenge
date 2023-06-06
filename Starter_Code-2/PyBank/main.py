import csv

input_path = "Resources/budget_data.csv"
out_path = "Analysis/budget_analysis.txt"

monthcount = 0
nettotal = 0
monthchange = []
netchange = []
greatestincrease = ["", 0]
greatestdecrease = ["", 9999999999]

with open (input_path) as file: 
    reader = csv.reader(file)

    header = next(reader)
    firstrow = next(reader)
    monthcount += 1
    nettotal += int(firstrow[1])
    previous = int(firstrow[1])

    for line in reader: 
        monthcount += 1
        nettotal += int(line[1])
        netchangenumber = int(line[1])-previous
        netchange.append(netchangenumber)
        previous = int(line[1])
        monthchange.append(line[0])
        if netchangenumber>greatestincrease[1]:
            greatestincrease[1]=netchangenumber
            greatestincrease[0]=line[0]
        if netchangenumber<greatestdecrease[1]:
            greatestdecrease[1]=netchangenumber
            greatestdecrease[0]=line[0]
averagemonthlychange = sum(netchange)/len(netchange)


with open(out_path,"w") as txt: 
    output = f"""
Financial Analysis
----------------------------
Total Months: {monthcount}
Total: ${nettotal}
Average Change: ${averagemonthlychange:.2f}
Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})
Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})
    """
    print(output)
    txt.write(output)