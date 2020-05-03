score = 0
for i in range(3):
    score += int(input())
if score < 50:
    print('F')
elif 50 <= score < 55:
    print('D')
elif 55 <= score < 60:
    print('D+')
elif 60 <= score < 65:
    print('C')
elif 65 <= score < 70:
    print('C+')
elif 70 <= score < 75:
    print('B')
elif 75 <= score < 80:
    print('B+')
else:
    print('A')
    