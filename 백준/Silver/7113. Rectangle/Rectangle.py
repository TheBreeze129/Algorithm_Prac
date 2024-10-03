import sys
sys.setrecursionlimit(10001)
k=0

def rec(n, m):
    global k
    k += 1
    if n == m:
        return
    if n < m:
        m -= n
        rec(n, m)
    else:
        n -= m
        rec(n, m)
N, M = map(int, input().split())
rec(N, M)
print(k)