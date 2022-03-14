# import dependacies

# os to ensure that the correct operating system is recognised
import os

# csv to enable the reading of csv files
import csv

# Path to collect data from the Resources folder

election_csv = os.path.join("Resources", "election_data.csv")
# print(election_csv)


# declare the variables to track and give them initial values

# declare vote_total to record the total number of votes cast and set the value at zero
vote_total = 0

# Create an empty list for each candidate name to complie a complete list of candidates
candidates = []

# Create an empty tuple to record the votes for each candidate so that the total and % of votes for each candidate can be calculated
candidate_votes = {}

# Create an empty variable for the winning candidate and one for the winner counter set a zero
winner = ""
winner_counter = 0

#  Path to output data from the analysis folder
output_txt = os.path.join("analysis", "election_analysis.txt")

# Read the csv and convert it into a list of dictionaries
with open(election_csv) as election_data:
    reader = csv.reader(election_data)

    # ignore the header row
    header = next(reader)

    
    for row in reader:

        # for each iteration (excluding the header) add 1 to vote counter 
        vote_total = vote_total + 1

        # extract the candidate name from the third column for each row
        name = row[2]

        # If the candidate name is not already in the canditaes list  
        if name not in candidates:

            # Add it to the candidates list
            candidates.append(name)

            # and start counting the votes from zero
            candidate_votes[name] = 0

        # If the candidate name is already in the list of candidates then add 1 to the correct candidate name
        candidate_votes[name] = candidate_votes[name] + 1

# open the output_txt variable as writable "w" using the new variable txt_edit
with open(output_txt, "w") as txt_edit:

    # Create a variable called results holding the formatted output for the total number of votes and print it to the terminal (\n is adding a new line, not required for the final line so that 
    # the candidate list appears straight after the final line of results
    results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"-------------------------")
    
    # print results to the terminal  
    print(results)
    
    # Save this vaiable to the text file
    txt_edit.write(results)

    # choose the winner by looping through the voter counts for each candidate
    for candidate in candidate_votes:

        # Retrieve voter counts and percentage, cast the strings as floats to enable the % calcualtion
        votes = candidate_votes.get(candidate)
        percentage = float(votes) / float(vote_total) * 100

        # find the candidate with the highest number of votes
        if (votes > winner_counter):
            winner_counter = votes
            winner = candidate

        # Create a variable called candidate_result, use it to print each candidate's name, percentage and the numbver of votes
        candidate_result = f"{candidate}: {percentage:.3f}% ({votes})"
        # candidate_result = f"{candidate}: {percentage:.3f}% ({votes})\n"

        # print candidate_result to the terminal, adding end=""    
        print(candidate_result)
        

        # Save each candidates name, percentage and number of votes (candidate_votes) to text file
        txt_edit.write(candidate_result)

    # Create a variable called winning candidate
    winning_candidate = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")

    # print winning candidate to the terminal    
    print(winning_candidate)

    # Save winning candidate to the text file
    txt_edit.write(winning_candidate)

