N,M = map(int,input().split())
p=print
r=range
a = [(1, j, N, j) for j in r(2, M+1, 2)] + [(i, 1, i, M) for i in r(2, N+1, 2)]
p(len(a))
for t in a:
    p(*t)