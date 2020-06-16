from collections import Counter
import re

print("Welcome to the Frequency Analysis App!")

# taking phrase from the user
phrase = input("Enter a word or phrase to compute the Frequency Analysis of: ").lower()

# cleaning of the phrase so that only the alphabets are present using regex
pattern = "[a-zA-Z]+"
cleaned_phrase = ''.join( re.findall(pattern, phrase) )

# using the Counter to first create an object which returns a dict with the frequency of each letter
result = Counter( cleaned_phrase )

# displaying all the letters with their percentage in an unordered way:
length_of_phrase = len(phrase)
print("Letter\t\tOccurence\t\tPercentage")
for key, value in result.items():
    percentage_value = round( 100 * (value / length_of_phrase), 2)
    print(key,"\t\t",value,"\t\t",percentage_value,"%")

# printing letter in an order of highest -> lowest
ordered_result = result.most_common()
for char in ordered_result:
    print(char[0],end='->',sep='')