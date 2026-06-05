# This program calculates the area of a triangle given its three sides using Heron's formula and prints the result.
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle with sides {a}, {b}, and {c} is {area:.2f}.")