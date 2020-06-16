import random
print("Welcome to Guess My Number App!")

# taking name of the user along with an introductory message!
name = input("Hello! What is your name: ").title()

# a bool value to check if the user has guessed the answer or not
guessed = False

# program will pick a number randomly between 1-20!
randomNumber = random.randrange(1, 21)
print("Well {}, I am thinking of a number between 1 and 20!".format(name))
print("\nYou have five chances to guess the number! Good luck!")

# guess starts with 5 chances
for i in range(5):
    temp = int(input("Take a guess: "))
    if temp == randomNumber:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, i+1))
        guessed = True
        break
    elif temp < randomNumber:
        print("Too Low!")
    else:
        print("Too High!")

if guessed == False:
    print("Game Over!\nI was thinking of the number", randomNumber)