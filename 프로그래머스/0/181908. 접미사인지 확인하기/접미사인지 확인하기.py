def solution(my_string, is_suffix):
    answer = 0
    if is_suffix in my_string:
        if is_suffix[-1] == my_string[-1]:
            answer = 1
    return answer