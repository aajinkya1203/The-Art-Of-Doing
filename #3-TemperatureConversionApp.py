print("Welcome to the Temperature Conversion App!")

# taking input in floating point
farenhiet = float(input("What is the given temperature in degrees Fahrenheit:"))

# converting farenhiet -> celsius
celsius = round((5/9)*(farenhiet-32), 4)
# converting celsius -> kelvin
kelvin = round((celsius + 273), 4)

# displaying the result
print(f"Degrees Fahrenheit:\t{farenhiet}\n")
print(f"Degrees Celsius:\t{celsius}\n")
print(f"Degrees Kelvin:\t{kelvin}\n")