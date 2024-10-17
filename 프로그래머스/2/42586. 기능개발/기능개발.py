def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        last = 100 - progresses[i]
        temp = last // speeds[i]
        if last % speeds[i]:
            temp += 1
        days.append(temp)
    for i in range(1, len(days)):
        if days[i-1] > days[i]:
            days[i] = days[i-1]
    for i in sorted(list(set(days))):
        answer.append(days.count(i))
    return answer