
import os
import csv


pypoll_file = r"C:\Users\camer\Desktop\3 - PYTHON\HW\PyPoll\Resources\Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"


candidates = []
candidate_votes = []
total_votes = 0


with open(pypoll_file,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    line = next(csvreader,None)


    for line in csvreader:

        total_votes = total_votes + 1

        candidate = line[2]

  
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
       
        else:
            candidates.append(candidate)
            candidate_votes.append(1)


percentages = []
max_votes = candidate_votes[0]
max_index = 0

for count in range(len(candidates)):
    percent_vote = round(candidate_votes[count]/total_votes*100)
    percentages.append(percent_vote)
    if candidate_votes[count] > max_votes:
        max_votes = candidate_votes[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({candidate_votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


write_output = r"C:\Users\camer\Desktop\3 - PYTHON\HW\PyPoll\Analysis\pypoll_results.txt"

filewriter = open(write_output, mode = 'w')

filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {total_votes}\n")
for count in range(len(candidates)):
   filewriter.write(f"{candidates[count]}: {percentages[count]}% ({candidate_votes[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

filewriter.close()
