import sys
input = sys.stdin.readline

N = int(input())

users = set()
cnt = 0
for _ in range(N):
    user = input().strip()
    if user == "ENTER":
        users.clear()
    elif user not in users:
        cnt += 1
        users.add(user)
print(cnt)