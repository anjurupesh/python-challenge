import os
import csv
pybank_csv = os.path.join("..","Resources", "/Users/owner/Desktop/GWDataBootCamp/python-challenge/PyPoll/Resources/election_data.csv")
pathout = os.path.join("Resources", "budget_data_analysis.txt")
sum_of_votes = []
num_of_voter = 0

with open(pybank_csv, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for votes in reader:
        num_of_voter = (num_of_voter + 1 )
        
print("Election Results")
print(".................................")
print(f"Total Votes: {num_of_voter}")

unique_list = []

with open(pybank_csv, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for candids in reader:
        if candids[2] not in unique_list:
            unique_list.append(candids[2])


num_of_Khan = 0
num_of_Correy = 0
num_of_Li = 0
num_of_Tooley = 0

with open(pybank_csv, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for candidatename in reader:
        if candidatename[2] == "Khan":
            num_of_Khan = (num_of_Khan + 1)
        elif candidatename[2] == "Correy":
            num_of_Correy = (num_of_Correy + 1)
        elif candidatename[2] == "Li":
            num_of_Li = (num_of_Li + 1)
        elif candidatename[2] == "O'Tooley":
            num_of_Tooley = (num_of_Tooley + 1)
 
perc_khan = round((num_of_Khan/num_of_voter)*100,3)
perc_correy = round((num_of_Correy/num_of_voter)*100,3)
perc_li = round((num_of_Li/num_of_voter)*100,3)
perc_tooley = round((num_of_Tooley/num_of_voter)*100,3)

print(f"Khan: {perc_khan}%({num_of_Khan}), \nCorrey: {perc_correy}% ({num_of_Correy}), \nLi:{perc_li}% ({num_of_Li}),\nO'Tooley: {perc_tooley}%, ({num_of_Tooley})")

perc_votes = []

perc_votes.append(perc_khan)
perc_votes.append(perc_correy)
perc_votes.append(perc_li)
perc_votes.append(perc_tooley)

grouped_list = list(zip(unique_list,perc_votes))

for winner in grouped_list:
    if winner[1] == max(perc_votes):
        print(f"Election winner: {winner[0]}")


with open(pathout, "w") as txt_file:
    
    txt_file.write("Election Results\n")
    txt_file.write(".................................\n")
    txt_file.write(f"Total Votes: {num_of_voter}\n")
    txt_file.write(f"Khan: {perc_khan}%({num_of_Khan}), \nCorrey: {perc_correy}% ({num_of_Correy}), \nLi:{perc_li}% ({num_of_Li}),\nO'Tooley: {perc_tooley}%, ({num_of_Tooley})\n")
    txt_file.write(f"Election winner: {winner[0]}")