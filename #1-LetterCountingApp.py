name = input("Hello, what would your name be: ").title().strip()

print(f"Hello, {name}")
print("I'm a letter counter app and so i'll help you count letters in any message!")

# lower-casing all letters to match the casing of all letters
message = input("Enter a message: ").lower()
letter = input("Enter a letter to count it's occurences: ").lower()

# using the count() method to count the number of letters in a string
letter_count = message.count(letter)
print(f"Your message has {letter_count} {letter}'s in it!")