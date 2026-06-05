#using with break statement
i = 1
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        break
    print(a[i])
    i += 1