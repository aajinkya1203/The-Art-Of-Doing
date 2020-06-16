print("Welcome to the Binary/Hexadecimal Converter App!")

# creating two empty lists
hexNo = []
binNo = []

# taking upperbound to create the hex and bin values for
upperBound = int(input("Compute binary and hexadecimal values up to the following decimal number: "))

# generating hex/bin values using list comprehension method!
hexNo = [ hex(num) for num in range(1,upperBound+1) ]
binNo = [ bin(num) for num in range(1,upperBound+1) ]
print("Generating lists....complete!")


# using slicing, show output for only a portion of the list
print("Using slices, we will now show a portion of each list.")
temp_lower = int(input("What decimal number would you like to start at: "))
temp_upper = int(input("What decimal number would you like to stop at: "))

# printing decimal values in that sub-section
print(f"\n\nDecimal values from {temp_lower} to {temp_upper}:")
for i in range(temp_lower, temp_upper+1):
    print(i)

# printing binary values in that sub-section
print(f"\n\nBinary values from {temp_lower} to {temp_upper}:")
for i in binNo[temp_lower:temp_upper+1]:
    print(i)

# printing hex values in that sub-section
print(f"\n\nHexadecimal values from {temp_lower} to {temp_upper}:")
for i in hexNo[temp_lower:temp_upper+1]:
    print(i)

input("Press any key to see all values from 1 to {}".format(upperBound))
print("\n\nDecimal---Binary---Hexadecimal")
print("----------------------------------")

for d, b, h in zip(list(range(1,upperBound+1)), binNo, hexNo):
    print(f"{d}---{b}---{h}")
