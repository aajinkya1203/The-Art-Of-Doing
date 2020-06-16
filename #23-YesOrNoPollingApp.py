print("Welcome to the Yes or No Polling App!")

# creating a dictionary to keep a record of all the votes and the number of yes / no votes
voters = {

}
yes_votes = 0
no_votes = 0

# variable for storing password for the poll
password = ""

# taking input for the survey
issue = input("What is the issue that people will be voting on today: ")
limit = int(input("What is the maximum no. of people who can vote: "))
password = input("Enter a password to see the poll results at the end: ")

for i in range(limit):
    name = input("Enter your full name: ").title()
    if name in voters.keys():
        print("Sorry, it seems that someone with that name has already voted!")
        continue
    print("\nHere is your issue to vote on:", issue)
    vote = input("What do you think...yes or no: ").lower().strip()
    if vote.startswith('y'):
        yes_votes += 1
        voters[name] = "Yes"
        print("\nThank you {}, your vote of yes has been recorded!".format(name))
    elif vote.startswith('n'):
        no_votes += 1
        voters[name] = "No"
        print("\nThank you {}, your vote of no has been recorded!".format(name))
    else:
        print("That's not a direct yes or neither a direct no!\nWe can't count your vote! :(")

temp_pass = input("Enter your poll password to see the results: ")
if temp_pass == password:
    print("The following {} people voted:".format( len( voters.keys() )) )
    for i in voters.keys():
        print(i)

    print("\n\nOn the issue:",issue)
    if yes_votes < no_votes:
        print("No Wins!\t",no_votes,"to",yes_votes)
    elif no_votes < yes_votes:
        print("Yes Wins!\t",yes_votes,"to",no_votes)
    else:
        print("It's a tie\t",yes_votes,"to",no_votes)
    
    input("Enter any key to see the voting details:")
    for username, votes in voters.items():
        print("Voter: ",username,"\t\tVote: ",votes)
