import sys
input = sys.stdin.readline
from math import ceil

N = int(input())
customers = list(map(int, input().split()))
lead, mate = map(int, input().split())

answer = len(customers)

for num in customers:
    if num <= lead:
        continue
    num -= lead
    answer += ceil(num / mate)
print(answer)