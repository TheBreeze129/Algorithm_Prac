def solution(myString):
    answer = []
    myString = myString.strip('x')
    myString = myString.split('x')
    for i in myString:
        if i != "":
            answer.append(i)
    answer = sorted(answer)
    return answer

# "axxxa"

# ["a", "", "", "a"]