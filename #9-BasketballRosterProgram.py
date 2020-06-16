import random

print("Welcome to the Basketball Roster Program!\n")

players = []
positions = ["point guard", "shooting guard", "small forward", "power forward", "center"]
# taking inputs for different players at different positions
players.append(input("Who is your {}: ".format(positions[0])).title())
players.append(input("Who is your {}: ".format(positions[1])).title())
players.append(input("Who is your {}: ".format(positions[2])).title())
players.append(input("Who is your {}: ".format(positions[3])).title())
players.append(input("Who is your {}: ".format(positions[4])).title())

# displaying the team
print("\n\tYour starting {} for the upcoming Basketball Season:\n".format(len(players)))
for index, player in enumerate(players):
    print(f"\t\t{positions[index]}:\t\t{player}")

# player injured, replacement needed
injured_index = random.randrange(0, len(players))
injured_player = players.pop(injured_index)
print(f"\nOh no, {injured_player} is injured!")
print("\nYour roster only has {} players now!".format(len(players)))

substitute = input("\nWho will take {}'s position:".format(injured_player)).title()
players.insert(injured_index, substitute)

# displaying the updated roster
for index, player in enumerate(players):
    print(f"\t\t{positions[index]}:\t\t{player}")

print("Good luck "+substitute+" you will do great!")
print("Your roster now has " + str(len(players)) + " players!")
