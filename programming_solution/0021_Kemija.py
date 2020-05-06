a = input()
i = 0
while i < len(a):
    if(a[i] in ['a', 'e', 'i', 'o', 'u']):
        a = a[:i] + a[i+2:]
    i += 1
print(a)