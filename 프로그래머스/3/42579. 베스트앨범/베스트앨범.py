def solution(genres, plays):
    answer = []
    gg = {x:[] for x in set(genres)}
    ggg = {x:0 for x in set(genres)}
    for i in range(len(genres)):
        gg[genres[i]].append((plays[i], i))
        ggg[genres[i]] += plays[i]
    for i in gg:
        gg[i].sort(key = lambda x:(-x[0], x[1]))
    g = list(set(genres))
    g.sort(key=lambda x:ggg[x], reverse=True)
    for i in g:
        if len(gg[i]) >= 2:
            answer += [gg[i][0][1], gg[i][1][1]]
        elif len(gg[i]) == 1:
            answer.append(gg[i][0][1])
    return answer