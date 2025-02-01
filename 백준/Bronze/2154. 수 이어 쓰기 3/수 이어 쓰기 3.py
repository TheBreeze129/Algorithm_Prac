N = int(input())
print("".join([str(x) for x in range(1, N+1)]).find(str(N))+1)