def dfs(i, computers, visited):
    visited[i] = True
    for ind, j in enumerate(computers[i]):
        if j and not visited[ind]:
            dfs(ind, computers, visited)

def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0 
    for i in range(n):
        if not visited[i]:
            print(i)
            answer += 1
            dfs(i, computers, visited)
    return answer

