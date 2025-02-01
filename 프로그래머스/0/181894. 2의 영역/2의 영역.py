def solution(arr):
    a = []
    for ind, data in enumerate(arr):
        if data == 2:
            a.append(ind)
    if len(a) == 0:
        return [-1]
    return arr[a[0]:a[-1]+1]