import random
print("Welcome to the Thesaurus App!")

# hard-coding the values in a dictionary
words = {
    "hot" : ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold" : ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy" : ['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad" : ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
}

print("Choose a word from the Thesauras and I'll give you it's synonyms!")

# displaying all the words in the thesauras to pick from
for word in words.keys():
    print("\t-", word)

# taking user input
user_word = input("What word would you like a synonym for: ").lower()

# giving a random synonym from a list of synonyms
random_syn = random.choice( words[user_word] )
print("A synonym for {} is {}".format( user_word, random_syn ))

# showing whole thesauras or not
choice = input("Would you like to see the whole thesauras (yes/no): ").lower()
if choice.startswith('y'):
    for word, syns in words.items():
        print(word,"synonyms are:")
        for syn in syns:
            print("\t-",syn)
else:
    print('I hope you enjoyed the program. Thank you!')