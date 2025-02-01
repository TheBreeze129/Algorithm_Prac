from math import gcd
D1, D2 = map(int, input().split())
count = [[0 for _ in range(2001)] for _ in range(2001)]
for i in range(D1, D2+1):
    for j in range(1, i):
        k = gcd(i, j)
        count[j//k][i//k] = 1
print(sum(sum(count[i]) for i in range(2001))+1)