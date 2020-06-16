import random

# function definition here
def roll_dice():
    # basic info
    sides = int(input("How many sides would you like on your dice: "))
    dices = int(input("How many sides would you like on your dice: "))

    # list of options
    options = list( range( 1, sides+1 ) )

    # rolling dice
    print("\n-----Results are as followed-----")
    sum = 0
    for dice in range(dices):
        dice_face = random.choice( options )
        print( "\t",dice_face )  
        sum += dice_face
    print("\nThe total value of your roll is:",sum)
      

print("Welcome to the The Python Dice App!")

# setting a flag to exit loop
flag = True

while flag:
    roll_dice()
    choice = input("Would you like to roll again (y/n): ").lower()
    if choice.startswith('y'):
        pass
    else:
        flag = False
        print("Thank you for using the Python Dice App.")