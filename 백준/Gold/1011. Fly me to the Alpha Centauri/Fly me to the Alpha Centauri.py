N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    t = 1
    while t**2 < y-x:
        t += 1
    result = (t-1)*2
    if ((t-1)**2+t**2)//2 < (y-x):
        result += 1
    print(result)