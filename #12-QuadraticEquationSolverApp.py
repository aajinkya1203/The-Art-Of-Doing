import math

# some introductory instructions
print("Welcome to the Quadratic Equation Solver App!")
print("\n\nA quadratic equation is of the form ax^2 + bx + c = 0\nYour solutions can be real or complex numbers.")
print("\n\nA complex number has two parts: a + bj.\nWhere a is the real portion and bj is the imaginary portion.\n")

iterate = int(input("How many equations would you like to solve today: "))
a = b = c = 0
real = imag = 0
for i in range(iterate):
    print(f"Solving equation #{i+1}\n---------------------------------------------------------------\n")
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (constant): "))

    # calculating real = -b/(2a)
    real = (-b)/(2*a)
    # calculating imag = √(b^2-4ac)/(2a)
    temp = (b**2)-(4.0*a*c)
    imag = math.sqrt(abs(temp))/(2*a)
    # displaying result
    print(f"\n\nThe solutions to {a}x^2 + {b}x + {c} = 0 are:")
    print("x1 = ({}+{}j)".format(real,imag))
    print("x2 = ({}-{}j)".format(real,imag))
    
print("Thank you for using the Quadratic Equation Solver App.")