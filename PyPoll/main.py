import csv

csv_path = r'Starter_Code\PyPoll\Resources\election_data.csv'

with open(csv_path, 'r', newline='', encoding='utf-8') as file:
    datafile = csv.reader(file, delimiter=',')
    header = next(datafile)
    total_votes = 0
    candidatelist = set()

    
    for row in datafile:
        total_votes += 1

        for candidates in candidatelist:
            print(candidates)

      


print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}') 
print('-------------------------')



