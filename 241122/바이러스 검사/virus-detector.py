import sys
input = sys.stdin.readline

N = int(input())
customers = list(map(int, input().split()))
lead, mate = map(int, input().split())

answer = 0

for num in customers:
    answer += 1
    num -= lead
    while num > 0:
        answer += 1
        num -= mate
print(answer)