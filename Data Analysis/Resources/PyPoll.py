#add our dependencies
import csv
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "12032020-election_results_DS.csv")

#Initialize a total vote counter.
total_votes = 0

#Candidate options and candidate votes
candidate_options=[]
candidate_votes={}

#Track the winning candidate, vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)
    
    #Print the header row
    headers = next(csvreader)
    print(headers)

    #Print the file object.
    for row in csvreader:
   
        #Add the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name=row[2]

        #Get distinct candidate names
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Track candidate's vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)