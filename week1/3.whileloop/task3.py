#using with continue statement
i = 0
a = 'geekforgeeks'
while i <len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1