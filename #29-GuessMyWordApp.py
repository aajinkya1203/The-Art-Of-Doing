import random
import re

print("Welcome to the Guess My Word App!")

# creating a dict that contains categories and its corresponding choice of answers!
words = {
    "sports": [ 'cricket', 'soccer', 'football', 'volleyball', 'golf', 'swimming', 'cycling' ],
    "fruits": [ 'mango', 'pear', 'kiwi', 'avacado', 'blueberry', 'grapes', 'pomegranate' ],
    "colors": [ 'grey', 'maroon', 'cyan', 'gold', 'silver', 'teal', 'violet' ],
    "artists": [ 'drake', '6ix9ine', 'eminem', 'kendrick', 'kanye', 'ariana', 'logic', 'travis', 'MJ', 'frank' ],
}

# setting a flag if the user wants to play again
again = True

# setting a list to contain all the hidden index of the word to be guesses
indexes = []

# setting a variable to keep a track if the user has guessed it or not
win = False

# setting a variable to store the word dashes and the letters
blank = ''

# game starts
while again:
    # randomly selecting a topic
    categories = [ word for word, values in words.items() ]
    topic = random.choice( categories )

    # randomly selecting a word from that topic
    word = random.choice( words[topic] )
    # storing the length of this word
    length = len(word)

    # giving the user the details of the word to guess:
    print("Guess a {} letter word from the catergory: {}\n\tWord: ".format( length, topic.title() ), end="")
    for i in range( length ):
        blank += '_'
    print(blank, end='')
    indexes = list(range(0, length))

    # guessing starts
    for chance in range( length ):
        guess = input("\nEnter your guess: ").lower()
        if guess == word:
            print("Correct! You guessed the word in {} guesses".format( chance+1 ))
            again = False
            win = True
            break
        print("\nThat is not correct! Let us reveal a letter to help you!")

        # giving the user a random letter to help him/her guess
        r_letter = random.choice(indexes)
        indexes.remove(r_letter)
        blank = list(blank)
        blank[r_letter] = word[r_letter]
        blank = ''.join(blank)
        print("\tWord:",blank,"\n")

    if win == False:
        print("\nUh-oh! You couldn't guess the word!\nThe word I was thinking of was:",word)
        
    # resetting all variables
    blank = ''
    again = False
    indexes = []
    win = False

    # asking for a re-game
    choice =  input("Would you like to go again (y/n): ")
    if choice.startswith('n'):
        again = False
        print("\nThanks for playing!\n")