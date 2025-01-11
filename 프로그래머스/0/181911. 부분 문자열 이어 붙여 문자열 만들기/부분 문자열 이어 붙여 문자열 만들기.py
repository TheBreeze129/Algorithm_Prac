def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        n = parts[i]
        answer += my_strings[i][n[0]:n[1]+1]
    return answer