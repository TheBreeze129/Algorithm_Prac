N, K = map(int, input().split())
scores = [(lambda x : [int(x[0]), int(x[1]+x[2].zfill(7)+x[3].zfill(7))])(input().split()) for _ in range(N)]
scores.sort(key=lambda x: x[1], reverse=True)
rank = 1
scores[0].append(1)
for i in range(1, N):
    rank = i + 1 if scores[i][1] != scores[i-1][1] else rank
    scores[i].append(rank)
for i in range(N):
    if scores[i][0] == K:
        print(scores[i][2])
        break