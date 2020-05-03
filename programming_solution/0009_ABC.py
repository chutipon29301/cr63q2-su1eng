[a, b, c] = sorted(list(map(int, input().split(' '))))
d = []
e = ' '
for i in input():
    if i == 'A':
        d.append(a)
    elif i == 'B':
        d.append(b)
    elif i == 'C':
        d.append(c)
print(e.join(list(map(str, d))))