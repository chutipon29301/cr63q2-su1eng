from itertools import combinations
a = [int(input()) for _ in range(9)]
b = list(map(list, combinations(a, 7)))
s = '\n'
for c in b:
    if(sum(c) == 100):
        print(s.join(map(str, c)))
        break