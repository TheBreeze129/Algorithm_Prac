def solution(s):
    answer = 0
    prev = 0
    for i in s.split():
        if i == 'Z':
            answer -= prev
        else:
            answer += int(i)
            prev = int(i)
    return answer