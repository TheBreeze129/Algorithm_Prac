N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    x = [input()[::-1] for _ in range(a)]
    for i in x:
        print(i)