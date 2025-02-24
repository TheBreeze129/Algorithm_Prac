from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

prefixDistinct = [0] * (N+1)
lastOcc = dict()
distinct_count = 0

for i in range(1, N+1):
    val = arr[i-1]
    if val not in lastOcc:
        distinct_count += 1
        lastOcc[val] = i
    else:
        lastOcc[val] = i
    prefixDistinct[i] = distinct_count

pos = defaultdict(list)
earliest = dict()
for i, val in enumerate(arr, start=1):
    pos[val].append(i)
    if val not in earliest:
        earliest[val] = i

answer = 0
for v, indices in pos.items():
    if len(indices) < 2:
        continue
    secondToLast = indices[-2]
    if secondToLast > 1:
        c = prefixDistinct[secondToLast - 1]
    else:
        c = 0
    if v in earliest and earliest[v] < secondToLast:
        c -= 1
    if c > 0:
        answer += c

print(answer)