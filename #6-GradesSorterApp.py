print("Welcome to the Grade Sorter App")

# taking input and appending it into the empty list
numbers = []
numbers.append(int(input("What is your first grade (0-100): ")))
numbers.append(int(input("What is your second grade (0-100): ")))
numbers.append(int(input("What is your third grade (0-100): ")))
numbers.append(int(input("What is your fourth grade (0-100): ")))

print(f"Your grades are {numbers}")

# sorting the list in descending order
numbers.sort(reverse=True)
print("Your grades from highest to lowest are:",numbers)

# Removing the last two smallest grades
print("The lowest two grades will now be dropped.")
print("Removing grade",numbers.pop())
print("Removing grade",numbers.pop())

# Printing remaining grades
print("Your remaining grades are:", numbers)

# Returning the highest number in the list
print("Nice work! Your highest grade is a",numbers[0])