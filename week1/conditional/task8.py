# This program converts a distance from kilometers to miles and prints the result.
kilometers = float(input("Enter distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles.")