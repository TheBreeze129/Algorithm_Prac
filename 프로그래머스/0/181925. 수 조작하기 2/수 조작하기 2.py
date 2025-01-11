def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        prev = numLog[i-1]
        now = numLog[i]
        if prev + 1 == now:
            answer += 'w'
        elif prev -1 == now:
            answer += 's'
        elif prev + 10 == now:
            answer += 'd'
        else:
            answer += 'a'
    return answer