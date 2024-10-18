def solution(triangle):
    triangle_replica = [[x for x in t] for t in triangle]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            triangle[i+1][j] = max(triangle[i+1][j], triangle[i][j] + triangle_replica[i+1][j])
            triangle[i+1][j+1] = max(triangle[i+1][j+1], triangle[i][j] + triangle_replica[i+1][j+1])
    answer = max(triangle[-1])
    return answer