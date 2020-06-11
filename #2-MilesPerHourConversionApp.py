print("Welcome to the Miles Per Hour Conversion Calculator:")

# taking input in floating point
inputValue = float(input("Enter the speed in miles per hours: "))

# Converting on the fact that 1mph = 0.4474mps
convertedValue = round(inputValue*0.4474, 2)

# displaying the result
print("Your speed in Miles Per hours:",inputValue)
print("Your speed in Metres Per Seconds:",convertedValue)