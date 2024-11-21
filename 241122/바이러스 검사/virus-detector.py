import sys
input = sys.stdin.readline

N = int(input())
customers = list(map(int, input().split()))
lead, mate = map(int, input().split())

answer = 0

for num in customers:
    answer += 1
    num -= lead
    if num <= 0:
        continue
    answer += (num // mate)
    if num % mate != 0:
        answer += 1
print(answer)