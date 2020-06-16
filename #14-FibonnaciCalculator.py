print("Welcome to the Fibonacci Calculator App!")

limit = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

# calculating fibonnaci sequence
fibbo = [ 0, 1 ]
ratio = [ 0, 1 ]
for i in range(2,limit+1):
    new_value = fibbo[i-1] + fibbo[i-2]
    fibbo.append(new_value)
    new_ratio = fibbo[i] / fibbo[i-1]
    ratio.append(new_ratio)

# printing the values
print("The first {} numbers of the Fibonnaci Sequence are:".format(limit))
for num in fibbo:
    print(num)

# printing the ratio
print("The corresponding Golden Ratio values are:")
for num in ratio:
    print(num)
