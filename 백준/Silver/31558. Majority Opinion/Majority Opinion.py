import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1] or (i < len(arr) - 2 and arr[i] == arr[i + 2]):
            result.append(arr[i])
    result = sorted(list(set(result)))
    if len(result) == 0:
        result = [-1]       
    print(*result)