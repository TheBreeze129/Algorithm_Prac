import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = 0
contrib = 0
cnt = 0
for i in range(n):
    contrib += cnt
    a[i] += contrib
    
    cur = -a[i]
    ans += abs(cur)
    cnt += cur
    contrib += cur
print(ans)