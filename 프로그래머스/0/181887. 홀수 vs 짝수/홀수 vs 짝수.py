def solution(num_list):
    answer = 0
    s1 = 0
    s2 = 0
    for i in range(len(num_list)):
        if i%2 == 0:
            s1 += num_list[i]
        else:
            s2 += num_list[i]
    if s1 > s2:
        answer = s1
    else:
        answer = s2
    return answer