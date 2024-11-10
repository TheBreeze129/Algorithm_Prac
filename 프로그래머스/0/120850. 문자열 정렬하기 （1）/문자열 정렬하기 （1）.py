def solution(my_string):
    answer = []
    for i in my_string:
        if i == '0':
            answer.append(0)
        elif i == '1':
            answer.append(1)
        elif i == '2':
            answer.append(2)
        elif i == '3':
            answer.append(3)
        elif i == '4':
            answer.append(4)
        elif i == '5':
            answer.append(5)
        elif i == '6':
            answer.append(6)
        elif i == '7':
            answer.append(7)
        elif i == '8':
            answer.append(8)
        elif i == '9':
            answer.append(9)
    answer = sorted(answer)
    return answer