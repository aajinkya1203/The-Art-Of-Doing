print("Welcome to the Multiplication/Exponent Table App!")

# taking user's name
name = input("What would your name be:")
num = float(input("What number would you like to work with:"))

print("\n\nMultiplication Table for",num)

for i in range(1,9):
  result = float(i)*num
  print(float(i), "*", num, "=", round(result, 2))

print("\n\nExponential Table for",num)

for i in range(1,9):
  result = float(i)**num
  print(float(i), "**", num, "=", round(result, 2))
