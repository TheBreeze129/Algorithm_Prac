def solution(clothes):
    cl = {x[1]:0 for x in clothes}
    for i in clothes:
        cl[i[1]] += 1
    temp = 1
    for num in cl.values():
        temp = temp * (num + 1)
    answer = temp - 1
    return answer