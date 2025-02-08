import sys
input = sys.stdin.readline
N = int(input().strip())
b = list(map(int, input().split()))

for first in range(1, N+1):
    a = [0] * N
    a[0] = first  
    for i in range(N-1):
        a[i+1] = b[i] - a[i]
    if all(1 <= x <= N for x in a) and len(set(a)) == N:
        print(" ".join(map(str, a)))
        break