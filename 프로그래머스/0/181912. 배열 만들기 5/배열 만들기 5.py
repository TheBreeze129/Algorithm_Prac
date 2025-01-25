def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        t = int(i[s:s+l])
        if t > k:
            answer.append(t)
    return answer