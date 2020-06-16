import random

print("Welcome to the Coin Toss App!")

# setting variables for keeping a track of heads and tails
heads = 0
tails = 0

# setting a list which indicates 0 as heads and 1 as tails
option = [ 0, 1 ]

# taking number of flips from user and if they wish to see the details of the flips
print("\nI will flip a coin a set number of times.")
flips = int(input("How many times would you like me to flip the coin: "))
show_details = input("Would you like to see the result of each flip (y/n): ").lower()

# flip process starts here

if show_details.startswith('y'):
    print("\nFlipping...\n")
    for i in range(1, flips+1):
        # passing option list in the random.choice() to select a value randomly from the list
        temp = random.choice(option)
        if temp == 0:
            # heads condition met
            heads += 1
            print("\nGot a HEADS at flip-{}!".format(i))
        else:
            # tails condition met
            tails += 1
            print("\nGot a TAILS at flip-{}!".format(i))
        # small description which is shown when the heads == tails
        if heads == tails:
            print(f"At {i} flips, the number of heads and tails were equal at {heads} each")
else:
    print("\nFlipping...\n")
    for i in range(1, flips+1):
        # passing option list in the random.choice() to select a value randomly from the list
        temp = random.choice(option)
        if temp == 0:
            # heads condition met
            heads += 1
        else:
            # tails condition met
            tails += 1

        # small description which is shown when the heads == tails
        if heads == tails:
            print(f"At {i} flips, the number of heads and tails were equal at {heads} each")
    

# shwoing the summary
print("\n\nResults of Flipping a coin {} times".format(flips))

print("\nSide\t\tCount\t\tPercentage")
heads_percentage = round((heads / flips) * 100, 2)
tails_percentage = round((tails / flips) * 100, 2)
print("\nHeads\t\t{}/{}\t\t{}".format( heads, flips, heads_percentage))
print("\nTails\t\t{}/{}\t\t{}".format( tails, flips, tails_percentage))

