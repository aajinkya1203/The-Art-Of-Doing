print("Welcome to Voter Registeration App!")

# taking name and age
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# keeping a track of all the parties as provided by the question
parties = [ 'Republican', 'Democratic', 'Green', 'Independent', 'Libertarian' ]

if age < 18:
    print("You're not old enough to Vote!")
else:
    # showing all the parties
    print("\nHere is a list of political parties to join: ")
    for party in parties:
        print("\t\t-",party.title())
    
    # taking input of user to join a party!
    input_party = input("What part would you like to join: ").title()
    if input_party in parties:
        print("Congratulations {}! You've joined the {} party!".format(name.title(), input_party.title()))
        if input_party.title() == "Republican" or input_party.title() == "Democratic":
            print("This is a Mayor Party!")
        elif input_party == "Independent":
            print("You're an Independent Person!")
        else:
            print("This is not a Mayor Party!")