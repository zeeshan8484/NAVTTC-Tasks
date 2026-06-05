# This program calculates the roots of a quadratic equation given its coefficients and prints the results.
import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)
print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are:")
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")