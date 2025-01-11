n, x = map(int, input().split())
pad = [(0, 0)] * (n + 1)  # 0번 인덱스를 채우기 위한 초기화
vis = [False] * (n + 1)
    
for i in range(1, n + 1):
    pad[i] = tuple(map(int, input().split()))

dir = 1
power = 1
ans = 0
    
for reps in range(5000000):
    if 1 <= x <= n:
        # Bessie가 아직 한 번도 부수지 않은 목표물을 부수면
        if pad[x][0] == 1 and power >= pad[x][1] and not vis[x]:
            vis[x] = True
            ans += 1

        if pad[x][0] == 0:  # 점프 패드
            dir *= -1
            power += pad[x][1]

        x += dir * power
    else:
        break

print(ans)
