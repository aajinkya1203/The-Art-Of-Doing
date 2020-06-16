import random
print("Welcome to the Rock Paper Scissors App!")

# variables to store sccores for computer and player
player = 0
computer = 0

# making a list of options the computer can pick it's choice from
options = [ 'rock', 'paper', 'scissors' ]

# taking the no of games the user wish to player
games = int(input("How many rounds would you like to play: "))

# temp variable to store the winner of a round to display it!
temp_winner = ""


for i in range(games):
    computers_pick = random.choice(options)
    print("\n\nThe computer has chosen its pick!")
    user_pick = input("Time to pick...rock, paper or scissors: ").lower()
    if user_pick in options:
        print("Player:",player,"\t\tComputer:",computer)
        print("Computer:", computers_pick)
        print("Player:", user_pick)
         
        # masking all possibilites for a rock paper scissors game!
        if user_pick == "rock":
            if computers_pick == "rock":
                temp_winner = ""
            elif computers_pick == "paper":
                computer += 1
                temp_winner = "computer"
                print("Paper covers Rock!")
            elif computers_pick == "scissors":
                player += 1
                temp_winner = "user"
                print("Rock Smashes Scissor\nKaboom!")
        elif user_pick == "paper":
            if computers_pick == "rock":
                player += 1
                temp_winner = "user"
                print("Paper covers Rock!")
            elif computers_pick == "paper":
                temp_winner = ""
            elif computers_pick == "scissors":
                computer += 1
                temp_winner = "computer"
                print("Scissors cut Paper!\nChop chop!")
        else:
            if computers_pick == "rock":
                computer += 1
                temp_winner = "computer"
                print("Rock smashes Scissor!\nKaboom!")
            elif computers_pick == "paper":
                player += 1
                temp_winner = "user"
                print("Scissor cuts Paper!\nChop chop!")
            elif computers_pick == "scissors":
                temp_winner = ""
        
        # after round summary
        if temp_winner == "":
            print("It's a tie, how boring!")
            print("No one gets the point, but the round will be counted!")
        elif temp_winner == "computer":
            print("Computer Wins the Round")
        else:
            print("User Wins the Round!")
    else:
        print("That's an invalid game option!")
        print("Point goes to Computer!")
        computer += 1

print("\n\nFinal Game Results:\n")
print("\tRounds Played:",games)
print("\tPlayer Score:",player)
print("\tComputer Score:", computer)
if computer < player:
    print("\tWinner Player!")
elif player < computer:
    print("\tWinner Computer!")
else:
    print("\tIt's a tie, bummer!\nNo one wins or loses :)")