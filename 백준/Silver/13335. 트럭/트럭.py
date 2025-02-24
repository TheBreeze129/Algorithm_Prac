n, w, L = map(int, input().split())
an = list(map(int, input().split()))
answer = 0
road = [0 for _ in range(w)]
while len(an) != 0:
    del road[0]
    if (sum(road) + an[0]) <= L:
        road.append(an[0])
        del an[0]
    else:
        road.append(0)
    answer += 1
print(answer+w)