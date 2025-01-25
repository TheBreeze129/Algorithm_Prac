import sys
input = sys.stdin.readline


def rotate(dir):
    dir += 1
    if dir == 4:
        dir = 0
    return dir


def next(x, y, dir):
    if dir == 0:
        x += 1
    elif dir == 1:
        y -= 1
    elif dir == 2:
        x -= 1
    else:
        y += 1
    return x, y


N = int(input())
board = [[False]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve = [d]
    for _ in range(g):
        curve += [rotate(x) for x in curve[::-1]]
    board[y][x] = True
    for dir in curve:
        x, y = next(x, y, dir)
        if x < 0 or y < 0 or x > 100 or y > 100:
            break
        board[y][x] = True

cnt = 0

for col in range(100):
    for row in range(100):
        if board[col][row] and board[col+1][row] and board[col][row+1] and board[col+1][row+1]:
            cnt += 1

print(cnt)
