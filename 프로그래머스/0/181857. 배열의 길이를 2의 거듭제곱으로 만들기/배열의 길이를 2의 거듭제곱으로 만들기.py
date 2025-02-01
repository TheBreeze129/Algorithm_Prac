def solution(arr):
    answer = []
    k = 2
    if len(arr) == 1:
        return arr
    while k < len(arr):
        k *= 2
    for i in range(k-len(arr)):
        arr.append(0)
    return arr