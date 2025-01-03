N,M = map(int,input().split())
ans = [(1, j, N, j) for j in range(2, M+1, 2)] + [(i, 1, i, M) for i in range(2, N+1, 2)]
print(len(ans))
for t in ans:
    print(*t)