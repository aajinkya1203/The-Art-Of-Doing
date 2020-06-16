import math
print("Welcome to the Factorial Calculator App!")

inputValue = int(input("What number would you like to compute the factorial of: "))

print(inputValue,"!= ",end=" ")
for i in range(1, inputValue+1):
    print(i, end="*")

# result from the math lib
print("\n\nHere is the result from the math library:")
print("\nThe factorial of {} from the math library is: {}".format(inputValue, math.factorial(inputValue)))

# manually computing factorial
result = 1
for i in range(1, inputValue+1):
    result *= i
print("\n\nHere is the result from the manual algorithm:\n")
print("The factorial of {} from the algorithm is: {}".format(inputValue, result))

print("\nTherefore, the value of {}!={}".format(inputValue, result))
