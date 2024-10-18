def solution(triangle):
    for i in range(len(triangle)-1):
        temp = triangle[i+1][:]
        for j in range(len(triangle[i])):
            triangle[i+1][j] = max(triangle[i+1][j], triangle[i][j] + temp[j])
            triangle[i+1][j+1] = max(triangle[i+1][j+1], triangle[i][j] + temp[j+1])
    return max(triangle[-1])