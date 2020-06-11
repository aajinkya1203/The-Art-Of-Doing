# impoting math lib for performing sqrt ops
import math as mh 

print("Welcome to the Right Triangle Solver App")

# taking input
base = float(input("What is the first leg of the triangle:"))
height = float(input("What is the second leg of the triangle:"))

# calculating area
area = 0.5 * base  * height
area = round(area, 3)
# calculating hypotenuse
temp = (base**2) + (height**2)
hypo = round(mh.sqrt(temp), 3)

print(f"For a triangle with legs of {base} and {height} the hypotenuse is {hypo}")
print(f"For a triangle with legs of {base} and {height} the area is {area}")