import csv
from pathlib import Path

csv_path = Path("PyPoll/Resources/election_data.csv")

ballot_ids = []
counties = []
candidates = []

with open(csv_path) as pollcsv:
    pollreader = csv.reader(pollcsv) 
    header = next(pollreader)

    for row in pollreader:
        ballot_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

    total_votes = len(ballot_ids)
    
    candidate_list = list(set(candidates))
    votes = [candidates.count(candidate) for candidate in candidate_list]
    percent_votes = [(votes[i] / total_votes) * 100 for i in range(len(candidate_list))]
    candidate_results = sorted(zip(candidate_list, votes, percent_votes), key=lambda x: x[1], reverse=True)

    winner = candidate_results[0][0]

# Printing Analysis 
print("Election Results \n")
print("-" * 30 + "\n")
print(f"Total Votes: {total_votes} \n")
print("-" * 30 + "\n")
for candidate, vote_count, percent_vote in candidate_results:
    print(f"{candidate}: {percent_vote:.3f}% ({vote_count})")
print("-" * 30 + "\n")
print(f"Winner: {winner} \n")
print("-" * 30 + "\n")

output_dir = Path("PyPoll")
output_dir.mkdir(parents=True, exist_ok=True)

output_filepath = output_dir / "election_data_analysis.txt"

with open(output_filepath, "w") as writer:
    writer.writelines("Election Results \n")
    writer.writelines("-" * 30 + "\n")
    writer.writelines(f"Total Votes: {total_votes} \n")
    writer.writelines("-" * 30 + "\n")
    for candidate, vote_count, percent_vote in candidate_results:
        writer.writelines(f"{candidate}: {percent_vote:.3f}% ({vote_count})\n")
    writer.writelines("-" * 30 + "\n")
    writer.writelines(f"Winner: {winner} \n")
    writer.writelines("-" * 30 + "\n")
