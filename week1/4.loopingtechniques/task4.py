#using sorted()
num = [5, 2, 9, 1, 5, 6,5,9,2,1,5,5,6,1,2,9,5,6,1,2,9]
print("sorted list: ")
for i in sorted(num):
    print(i , end = " ")
print("\nsorted list with out duplicates: ")
for i in sorted(set(num)):
    print(i , end = " ")