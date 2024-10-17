def solution(priorities, location):
    answer = 0
    processes = [x for x in range(len(priorities))]
    while True:
        process = processes.pop(0)
        priority = priorities.pop(0)
        if len(priorities) == 0:
            answer += 1
            break
        if priority < max(priorities):
            processes.append(process)
            priorities.append(priority)
        else:
            answer += 1
            if process == location:
                break
    return answer