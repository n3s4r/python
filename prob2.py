import cmath

def quadratic_function(a, b, c):
    d = (b * b) - (4 * a * c)

    if d < 0:
        print("Roots are complex")
        return

    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)

    if d > 0:
        print("Roots are real")
    else:
        print("Repeated roots")

    print("Roots of the equation are:", x1, x2)


# Taking input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

quadratic_function(a, b, c)
