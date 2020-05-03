c = 1
for i in input():
    if i == 'A':
        if c == 1:
            c = 2
        elif c == 2:
            c = 1
    if i == 'B':
        if c == 2:
            c = 3
        elif c == 3:
            c = 2
    if i == 'C':
        if c == 3:
            c = 1
        elif c == 1:
            c = 3
print(c)