# Your task is to create a Python script that would help a small, rural town modernize its vote counting process.
    # The total number of votes cast

    # A complete list of candidates who received votes

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote.

# Start with importing your Modules
import os
import csv

# We need a path to collect from the Resouces folder.
ElectionData = os.path.join("Resources", "election_data.csv")

# We must define Candidate as a empty set and Votes as an empty set.

candidates = []
votes = []

# Read CSV to ensure I was able to pull the data.
with open(ElectionData, "r") as cvsfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader =csv.reader(cvsfile, delimiter=",")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Now we will iterate through each row
    for column in csvreader:
        candidates.append(column[2])
        votes.append(column[0])

    # Now we find the total number of votes
    Total_Votes = (len(votes))

    # Check to see if the total votes were calculates
    print("Total Votes:" + str(Total_Votes))

    # Count Candidate Correy votes and Correy's percentage.
    Correy = int(candidates.count("Correy"))
    Correy_P = round((Correy / Total_Votes) * 100)
    Correy_P_Rounded = round(int(Correy_P))

    # Count Candidate Khan votes Khan's percentage.
    Khan = int(candidates.count("Khan"))
    Khan_P = round((Khan / Total_Votes) * 100)
    Khan_P_Rounded = round(int(Khan_P))

     # Count Candidate Li votes Li's percentage.
    Li = int(candidates.count("Li"))
    Li_P = round((Li / Total_Votes) * 100)
    Li_P_Rounded = round(int(Li_P))

     # Count Candidate O'Tooley votes O'Tooley's percentage.
    OTooley = int(candidates.count("O'Tooley"))
    OTooley_P = round((OTooley / Total_Votes) * 100)
    OTooley_P_Rounded = round(int(OTooley_P))

    # Check to see if we get back the votes for each candidates and their percentages
    print(str(Correy))
    print(str(Correy_P_Rounded))
    print(str(Khan))
    print(str(Khan_P_Rounded))
    print(str(Li))
    print(str(Li_P_Rounded))
    print(str(OTooley))
    print(str(OTooley_P_Rounded))

    # We have to figure out the winner of the election.

    if Correy > Khan > Li > OTooley:
        Winner = "Correy"
    elif Khan > Correy > Li > OTooley:
        Winner = "Khan"
    elif Li > Correy > Khan > OTooley:
        Winner = "Li"
    elif OTooley > Correy > Khan > Li:
        Winner = "O'Tooley"
    
    # heck to see who is the winner. Accordind to the pre checks from earlier calculations, the answer should be Khan.
    print(str(Winner))

# Now we can write a text file with the election results. Don't forget to add \n to ensure you move to the next line.
# output_file = Path("python-challenge", "PyPoll", "analysis", "Election_Results_Summary.txt")

# with open(output_file,"w") as file:
    # file = open("output.text", "w")
    # file.write("Election Results" + "\n")
    # file.write("-------------------------------------------------------------" "\n")
    # file.write("Total Votes:" " " + str(Total_Votes) + "\n")
    # file.write("-------------------------------------------------------------" "\n")
    # file.write("Correy:" " " + str(Correy_P_Rounded) + "%" + str(Correy) + "\n")
    # file.write("Khan:" " " + str(Khan_P_Rounded) + "%" + str(Khan) + "\n")
    # file.write("Li:" " " + str(Li_P_Rounded) + "%" + str(Li) + "\n")
    # file.write("O'Tooley:" " " + str(OTooley_P_Rounded) + "%" + str(OTooley) + "\n")
    # file.write("-------------------------------------------------------------" "\n")
    # file.write("Winner:" " " + str(Winner) + "\n")
    # file.write("-------------------------------------------------------------" "\n")
    # file.close()