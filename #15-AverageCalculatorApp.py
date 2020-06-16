import math
print("Welcome to the Average Calculator App!")

name = input("What is your name: ").title()
noOfGrades = int(input("How many grades would you like to enter: "))

# entering grades into the list
grades = []
for i in range(noOfGrades):
    grades.append(int(input("Enter grade: ")))

# sorting the grades highest -> lowest
print("\n\nGrades highest to lowest are:")
grades.sort(reverse=True)
for i in grades:
    print(i)

# Showing summary of the person
print("\n\n{}'s grade summary:\n".format(name) )
print("\tTotal number of grades:", len(grades) )
print("\tHighest grade:", max(grades) )
print("\tLowest grade:", min(grades) )
avg = sum(grades) / len(grades)
print("\tAverage:", round(avg, 2) )

# desired average calculation and how to achieve it
desiredAvg = int(input("\nWhat is your desired average: "))
required_grade = (desiredAvg * (len(grades)+1)) - sum(grades)
print("You need to get a",required_grade,"on your next assignment to earn an average of",desiredAvg)

# predicting the average change if the scores were different
print("\n\nLets see what your average could have been if you did better/worse on an assignment.")
to_remove = int(input("What grade would you like to remove: "))
new_value = int(input("What grade would you like to change "+ str(to_remove) + " to: "))

# copying list grades into a new list
original_grades = grades[:]

# printing the new grades in descending order
grades.remove(to_remove)
grades.append(new_value)
print("\n\nNew Grades Highest to Lowest\n")
grades.sort(reverse=True)
for i in grades:
    print(i)

# Showing summary of the person
print("\n\n{}'s grade summary:\n".format(name) )
print("\tTotal number of grades:", len(grades) )
print("\tHighest grade:", max(grades) )
print("\tLowest grade:", min(grades) )
new_avg = sum(grades) / len(grades)
print("\tAverage:", round(avg, 2) )

print(f"\nYour new average would have been {new_avg} compared to your real average of {avg}!")
print("That is a change of {} points!".format( round(new_avg - avg), 2))

print("\n\nToo bad your original grades are still the same!\n",grades)
print("You should go ask for extra credit!")