#using with else
i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("no break")
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("with break")
