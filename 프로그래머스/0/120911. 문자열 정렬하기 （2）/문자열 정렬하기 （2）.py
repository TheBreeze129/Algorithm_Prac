def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_string = sorted(my_string)
    my_string = "".join(my_string)
    return my_string