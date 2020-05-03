d = list(map(int, input().split(' ')))
a = [list(map(int, input().split(' '))) for _ in range(d[0])]
b = [list(map(int, input().split(' '))) for _ in range(d[0])]
c = ' '
for i in range(len(a)):
    for j in range (len(a[i])):
        a[i][j] += b[i][j]
    print(c.join(list(map(str, a[i]))))
