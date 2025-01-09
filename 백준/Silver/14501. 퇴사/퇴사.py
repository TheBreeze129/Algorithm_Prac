import sys
input = sys.stdin.readline
sys.setrecursionlimit(4000)

N = int(input())
datas = {i: tuple(map(int, input().split())) for i in range(N)}


for i in datas:
    if datas[i][0]+i > N:
        datas[i] = (0, 0)

max_profit = 0


def get_max_profit(day, profit=0):
    global max_profit
    if day >= N:
        if profit > max_profit:
            max_profit = profit
        return
    if datas[day][0] == 0:
        get_max_profit(day+1, profit)
    else:
        get_max_profit(day+datas[day][0], profit+datas[day][1])
        get_max_profit(day+1, profit)


for i in range(N):
    get_max_profit(i)

print(max_profit)
